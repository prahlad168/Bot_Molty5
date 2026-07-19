<?php
/**
 * XENDIT PAYMENT INTEGRATION
 * MAHA LAKSHMI HOLDINGS
 * 
 * Setup Guide:
 * 1. Daftar di https://dashboard.xendit.co/register
 * 2. Get API Key dari dashboard
 * 3. Masukkan XENDIT_API_KEY di bawah
 * 4. Upload ke hosting
 */

// =====================
// CONFIGURATION
// =====================
define('XENDIT_API_KEY', 'xendit_api_key_anda_di_sini'); // Ganti dengan API Key dari Xendit Dashboard
define('XENDIT_CALLBACK_TOKEN', 'your_callback_token'); // Token untuk verify callback
define('XENDIT_URL', 'https://api.xendit.co');

// =====================
// INVOICE CREATION
// =====================
function createInvoice($order_id, $amount, $customer_name, $customer_email, $description) {
    $headers = [
        'Authorization: Basic ' . base64_encode(XENDIT_API_KEY . ':'),
        'Content-Type: application/json'
    ];
    
    $data = [
        'external_id' => $order_id,
        'amount' => (int)$amount,
        'payer_email' => $customer_email,
        'description' => $description,
        'customer' => [
            'given_names' => $customer_name
        ],
        'payment_methods' => ['OVO', 'DANA', 'LINKAJA', 'BCA', 'MANDIRI', 'BNI', 'BRI', 'QRIS'],
        'success_redirect_url' => 'https://prahlad168.github.io/MAHA-LAKSHMI-CORP/payment/success.html',
        'failure_redirect_url' => 'https://prahlad168.github.io/MAHA-LAKSHMI-CORP/payment/failed.html'
    ];
    
    $ch = curl_init(XENDIT_URL . '/v2/invoices');
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    
    $response = curl_exec($ch);
    curl_close($ch);
    
    return json_decode($response, true);
}

// =====================
// GET INVOICE STATUS
// =====================
function getInvoiceStatus($invoice_id) {
    $headers = [
        'Authorization: Basic ' . base64_encode(XENDIT_API_KEY . ':')
    ];
    
    $ch = curl_init(XENDIT_URL . '/v2/invoices/' . $invoice_id);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    
    $response = curl_exec($ch);
    curl_close($ch);
    
    return json_decode($response, true);
}

// =====================
// CREATE QRIS PAYMENT
// =====================
function createQris($external_id, $amount, $description) {
    $headers = [
        'Authorization: Basic ' . base64_encode(XENDIT_API_KEY . ':'),
        'Content-Type: application/json'
    ];
    
    $data = [
        'external_id' => $external_id,
        'amount' => (int)$amount,
        'channel_code' => 'QRIS',
        'description' => $description
    ];
    
    $ch = curl_init(XENDIT_URL . '/v2/qr_codes');
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    
    $response = curl_exec($ch);
    curl_close($ch);
    
    return json_decode($response, true);
}

// =====================
// CALLBACK HANDLER
// =====================
function handleCallback() {
    $callback_token = $_SERVER['HTTP_X_CALLBACK_TOKEN'] ?? '';
    
    if ($callback_token !== XENDIT_CALLBACK_TOKEN) {
        http_response_code(401);
        die('Invalid token');
    }
    
    $payload = file_get_contents('php://input');
    $data = json_decode($payload, true);
    
    // Handle different events
    switch ($data['event']) {
        case 'invoice.paid':
            handleInvoicePaid($data);
            break;
        case 'qr_payment':
            handleQrisPaid($data);
            break;
    }
    
    echo 'OK';
}

function handleInvoicePaid($data) {
    $order_id = $data['data']['external_id'];
    $amount = $data['data']['amount'];
    $paid_at = $data['data']['paid_at'];
    
    // TODO: Update database - mark order as paid
    // Log payment
    $log = "[" . date('Y-m-d H:i:s') . "] PAID: $order_id - Rp " . number_format($amount) . " at $paid_at\n";
    file_put_contents('payment-log.txt', $log, FILE_APPEND);
    
    // TODO: Send WhatsApp notification
    // TODO: Send email confirmation
}

function handleQrisPaid($data) {
    $external_id = $data['data']['external_id'];
    $amount = $data['data']['amount'];
    
    // TODO: Update database - mark order as paid
    $log = "[" . date('Y-m-d H:i:s') . "] QRIS PAID: $external_id - Rp " . number_format($amount) . "\n";
    file_put_contents('payment-log.txt', $log, FILE_APPEND);
}

// =====================
// GENERATE INVOICE PAGE
// =====================
function generatePaymentPage($order_id, $amount, $description, $customer_email) {
    $invoice = createInvoice($order_id, $amount, 'Customer', $customer_email, $description);
    
    if (isset($invoice['invoice_url'])) {
        header('Location: ' . $invoice['invoice_url']);
    } else {
        echo json_encode($invoice);
    }
}

// =====================
// HELPER: Generate Order ID
// =====================
function generateOrderId() {
    return 'INV-' . date('Ymd') . '-' . strtoupper(substr(md5(rand()), 0, 6));
}

// =====================
// HELPER: Format Currency
// =====================
function formatCurrency($amount) {
    return 'Rp ' . number_format($amount, 0, ',', '.');
}

// =====================
// API ENDPOINTS
// =====================

// Route: create-invoice.php?action=create
if (isset($_GET['action']) && $_GET['action'] === 'create') {
    header('Content-Type: application/json');
    
    $order_id = $_POST['order_id'] ?? generateOrderId();
    $amount = (int)$_POST['amount'];
    $customer_name = $_POST['customer_name'] ?? 'Customer';
    $customer_email = $_POST['customer_email'] ?? '';
    $description = $_POST['description'] ?? 'Payment';
    
    $result = createInvoice($order_id, $amount, $customer_name, $customer_email, $description);
    
    echo json_encode($result);
}

// Route: callback-xendit.php
if (isset($_GET['route']) && $_GET['route'] === 'callback') {
    handleCallback();
}

// Route: check-status.php?invoice_id=xxx
if (isset($_GET['action']) && $_GET['action'] === 'status') {
    header('Content-Type: application/json');
    
    $invoice_id = $_GET['invoice_id'] ?? '';
    $result = getInvoiceStatus($invoice_id);
    
    echo json_encode($result);
}

// Route: create-qris.php
if (isset($_GET['action']) && $_GET['action'] === 'qris') {
    header('Content-Type: application/json');
    
    $external_id = $_POST['external_id'] ?? generateOrderId();
    $amount = (int)$_POST['amount'];
    $description = $_POST['description'] ?? 'QRIS Payment';
    
    $result = createQris($external_id, $amount, $description);
    
    echo json_encode($result);
}
?>
