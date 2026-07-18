<?php
/**
 * MAHA LAKSHMI - Midtrans Notification Handler
 * 
 * Endpoint untuk menerima callback dari Midtrans
 * Akan dipanggil otomatis setelah customer melakukan pembayaran
 */

require_once __DIR__ . '/../midtrans/Midtrans.php';
require_once __DIR__ . '/../midtrans/config.php';

// Set config
\Midtrans\Config::$serverKey = MIDTRANS_SERVER_KEY;
\Midtrans\Config::$isProduction = IS_PRODUCTION;

// Set timezone
date_default_timezone_set('Asia/Jakarta');

// Enable error reporting
error_reporting(E_ALL);
ini_set('display_errors', 0);

// Set header
header('Content-Type: application/json');

// Log all requests
if (LOG_ENABLED) {
    $log = "\n\n" . str_repeat("=", 50) . "\n";
    $log .= date('Y-m-d H:i:s') . " | NOTIFICATION RECEIVED\n";
    $log .= "IP: " . $_SERVER['REMOTE_ADDR'] . "\n";
    $log .= "Method: " . $_SERVER['REQUEST_METHOD'] . "\n";
    file_put_contents(__DIR__ . '/midtrans.log', $log, FILE_APPEND);
}

// Handle GET request (for testing)
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    echo json_encode([
        'status' => 'ok',
        'message' => 'Midtrans notification endpoint is active',
        'timestamp' => date('Y-m-d H:i:s')
    ]);
    exit();
}

// Only accept POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['error' => 'Method not allowed']);
    exit();
}

// Get notification body
$input = file_get_contents('php://input');
$notification = json_decode($input, true);

if (LOG_ENABLED) {
    $log = date('Y-m-d H:i:s') . " | RAW: " . $input . "\n";
    file_put_contents(__DIR__ . '/midtrans.log', $log, FILE_APPEND);
}

// Validate notification
if (empty($notification)) {
    http_response_code(400);
    echo json_encode(['error' => 'Invalid notification']);
    exit();
}

// Get transaction status
$order_id = isset($notification['order_id']) ? $notification['order_id'] : '';
$transaction_status = isset($notification['transaction_status']) ? $notification['transaction_status'] : '';
$status_code = isset($notification['status_code']) ? $notification['status_code'] : '';
$gross_amount = isset($notification['gross_amount']) ? $notification['gross_amount'] : 0;
$payment_type = isset($notification['payment_type']) ? $notification['payment_type'] : '';
$transaction_id = isset($notification['transaction_id']) ? $notification['transaction_id'] : '';
$va_number = isset($notification['va_numbers'][0]['va_number']) ? $notification['va_numbers'][0]['va_number'] : '';
$fraud_status = isset($notification['fraud_status']) ? $notification['fraud_status'] : '';

// Log received data
if (LOG_ENABLED) {
    $log = date('Y-m-d H:i:s') . " | ORDER: {$order_id} | STATUS: {$transaction_status} | AMOUNT: {$gross_amount}\n";
    file_put_contents(__DIR__ . '/midtrans.log', $log, FILE_APPEND);
}

// Process based on transaction status
$result = [
    'success' => false,
    'message' => '',
    'action' => ''
];

try {
    switch ($transaction_status) {
        case 'capture':
            // Credit card transaction is captured
            if ($fraud_status == 'challenge') {
                // Handle challenge
                $result['success'] = true;
                $result['message'] = 'Transaction is challenged, review required';
                $result['action'] = 'review';
            } else {
                // Accept transaction
                $result['success'] = true;
                $result['message'] = 'Transaction successful - Payment captured';
                $result['action'] = 'accept';
            }
            break;
            
        case 'settlement':
            // Payment is successful
            $result['success'] = true;
            $result['message'] = 'Transaction successful - Payment settled';
            $result['action'] = 'accept';
            
            // TODO: Save to database
            // TODO: Send confirmation email
            // TODO: Trigger GAURANGA AI notification
            // TODO: Update revenue tracker
            
            // Log to file
            if (LOG_ENABLED) {
                $log = date('Y-m-d H:i:s') . " | SETTLEMENT | Order: {$order_id} | Amount: {$gross_amount} | VA: {$va_number}\n";
                file_put_contents(__DIR__ . '/settlement.log', $log, FILE_APPEND);
                
                // Also save to JSON for easy reading
                $settlement_file = __DIR__ . '/settlements/' . date('Y-m') . '.json';
                if (!is_dir(__DIR__ . '/settlements')) {
                    mkdir(__DIR__ . '/settlements', 0755, true);
                }
                $settlements = file_exists($settlement_file) ? json_decode(file_get_contents($settlement_file), true) : [];
                $settlements[] = [
                    'order_id' => $order_id,
                    'amount' => $gross_amount,
                    'payment_type' => $payment_type,
                    'transaction_id' => $transaction_id,
                    'va_number' => $va_number,
                    'timestamp' => date('Y-m-d H:i:s'),
                    'status' => 'settled'
                ];
                file_put_contents($settlement_file, json_encode($settlements, JSON_PRETTY_PRINT));
            }
            break;
            
        case 'pending':
            // Waiting for payment
            $result['success'] = true;
            $result['message'] = 'Waiting for payment - Customer has not paid yet';
            $result['action'] = 'wait';
            break;
            
        case 'deny':
            // Transaction denied
            $result['success'] = false;
            $result['message'] = 'Transaction denied';
            $result['action'] = 'deny';
            break;
            
        case 'cancel':
            // Transaction cancelled
            $result['success'] = false;
            $result['message'] = 'Transaction cancelled';
            $result['action'] = 'cancel';
            break;
            
        case 'expire':
            // Transaction expired
            $result['success'] = false;
            $result['message'] = 'Transaction expired - Payment deadline passed';
            $result['action'] = 'expire';
            break;
            
        case 'refund':
            // Refund initiated
            $result['success'] = true;
            $result['message'] = 'Refund processed';
            $result['action'] = 'refund';
            break;
            
        default:
            $result['message'] = 'Unknown transaction status';
            $result['action'] = 'unknown';
    }
    
    // Send response to Midtrans
    http_response_code(200);
    echo json_encode([
        'success' => true,
        'order_id' => $order_id,
        'transaction_status' => $transaction_status,
        'message' => $result['message']
    ]);
    
} catch (Exception $e) {
    // Log error
    if (LOG_ENABLED) {
        $log = date('Y-m-d H:i:s') . " | ERROR: " . $e->getMessage() . "\n";
        file_put_contents(__DIR__ . '/midtrans.log', $log, FILE_APPEND);
    }
    
    // Send error response
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'error' => $e->getMessage()
    ]);
}
?>
