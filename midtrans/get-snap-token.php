<?php
/**
 * MAHA LAKSHMI - Get Snap Token
 * 
 * Endpoint untuk generate Midtrans Snap Token
 * Dipanggil dari frontend untuk menampilkan popup payment
 */

require_once __DIR__ . '/../midtrans/Midtrans.php';
require_once __DIR__ . '/../midtrans/config.php';

// Set config
\Midtrans\Config::$serverKey = MIDTRANS_SERVER_KEY;
\Midtrans\Config::$isProduction = IS_PRODUCTION;
\Midtrans\Config::$isSanitized = MIDTRANS_SANITIZE;
\Midtrans\Config::$is3ds = MIDTRANS_3DS;

// Set timezone
date_default_timezone_set('Asia/Jakarta');

// Enable error reporting for debugging
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Set header
header('Content-Type: application/json');

// Handle CORS
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

// Handle preflight
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit();
}

// Only accept POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['error' => 'Method not allowed']);
    exit();
}

// Get JSON input
$input = json_decode(file_get_contents('php://input'), true);

// Validate required fields
$required_fields = ['order_id', 'amount', 'customer_name', 'product_name'];
foreach ($required_fields as $field) {
    if (empty($input[$field])) {
        http_response_code(400);
        echo json_encode(['error' => "Missing required field: {$field}"]);
        exit();
    }
}

$order_id = trim($input['order_id']);
$gross_amount = (int)$input['amount'];
$customer_name = trim($input['customer_name']);
$customer_email = isset($input['customer_email']) ? trim($input['customer_email']) : '';
$customer_phone = isset($input['customer_phone']) ? trim($input['customer_phone']) : '';
$product_name = trim($input['product_name']);

// Validate amount
if ($gross_amount < 10000) {
    http_response_code(400);
    echo json_encode(['error' => 'Minimum amount is Rp 10,000']);
    exit();
}

// Generate unique order ID if not provided
if (empty($order_id) || $order_id === 'auto') {
    $order_id = 'MLA-' . date('YmdHis') . '-' . rand(100, 999);
}

// Item details
$item_details = [
    [
        'id' => 'prod-001',
        'price' => $gross_amount,
        'quantity' => 1,
        'name' => substr($product_name, 0, 50)
    ]
];

// Customer details
$customer_details = [
    'first_name' => $customer_name,
    'last_name' => '',
    'email' => $customer_email ?: 'customer@mahalaksmi.web.id',
    'phone' => $customer_phone ?: '081234567890',
    'billing_address' => [
        'first_name' => $customer_name,
        'address' => 'Digital Product',
        'city' => 'Gianyar',
        'postal_code' => '80515',
        'phone' => $customer_phone ?: '081234567890',
        'country_code' => 'IDN'
    ],
    'shipping_address' => [
        'first_name' => $customer_name,
        'address' => 'Digital Product',
        'city' => 'Gianyar',
        'postal_code' => '80515',
        'phone' => $customer_phone ?: '081234567890',
        'country_code' => 'IDN'
    ]
];

// Transaction details
$transaction_details = [
    'order_id' => $order_id,
    'gross_amount' => $gross_amount
];

// Custom fields
$custom_fields = [
    'company' => 'MAHA LAKSHMI HOLDINGS',
    'product' => $product_name,
    'ceo' => 'i Made Purna Ananda'
];

// Build snap parameters
$snap_params = [
    'transaction_details' => $transaction_details,
    'customer_details' => $customer_details,
    'item_details' => $item_details,
    'custom_field1' => json_encode($custom_fields)
];

// Add expiry time
$expiry = [
    'start_time' => date('Y-m-d H:i:s O'),
    'unit' => 'minutes',
    'duration' => EXPIRY_MINUTES
];
$snap_params['expiry'] = $expiry;

try {
    // Get Snap Token
    $snap_token = \Midtrans\Snap::getSnapToken($snap_params);
    
    // Log success
    if (LOG_ENABLED) {
        $log = date('Y-m-d H:i:s') . " | SUCCESS | Order: {$order_id} | Amount: {$gross_amount}\n";
        file_put_contents(__DIR__ . '/midtrans.log', $log, FILE_APPEND);
    }
    
    // Return response
    echo json_encode([
        'success' => true,
        'snap_token' => $snap_token,
        'order_id' => $order_id,
        'amount' => $gross_amount,
        'message' => 'Snap token generated successfully'
    ]);
    
} catch (Exception $e) {
    // Log error
    if (LOG_ENABLED) {
        $log = date('Y-m-d H:i:s') . " | ERROR | " . $e->getMessage() . "\n";
        file_put_contents(__DIR__ . '/midtrans.log', $log, FILE_APPEND);
    }
    
    // Return error
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'error' => $e->getMessage(),
        'message' => 'Failed to generate snap token'
    ]);
}
?>
