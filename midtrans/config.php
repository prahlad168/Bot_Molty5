<?php
/**
 * MAHA LAKSHMI - Midtrans Configuration
 * 
 * Setup Instructions:
 * 1. Daftar di https://dashboard.midtrans.com
 * 2. Setelah verifikasi, dapat credentials
 * 3. Ganti SB-Mid-server-xxx dan SB-Mid-client-xxx dengan credentials asli
 */

// Sandbox (Testing) Credentials
// Ganti dengan credentials production setelah testing selesai
define('MIDTRANS_SERVER_KEY', 'SB-Mid-server-xxx');
define('MIDTRANS_CLIENT_KEY', 'SB-Mid-client-xxx');

// Set true untuk production
define('IS_PRODUCTION', false);

// Midtrans Config
define('MIDTRANS_MERCHANT_ID', 'M001234');

// Enable sanitize untuk keamanan
define('MIDTRANS_SANITIZE', true);

// Enable 3D Secure
define('MIDTRANS_3DS', true);

// Payment Types
define('PAYMENT_VA', ['bank_transfer' => ['bca', 'mandiri', 'bni', 'bri', 'permata']]);
define('PAYMENT_EWALLET', ['gopay', 'ovO', 'dana', 'shopeepay']);
define('PAYMENT_CARD', ['credit_card']);
define('PAYMENT_QRIS', ['qris']);

// Bank Transfer VA
define('VA_BCA', '0000'); // Nomor VA akan di-generate otomatis
define('VA_MANDIRI', '0000');
define('VA_BNI', '0000');
define('VA_BRI', '0000');
define('VA_PERMATA', '0000');

// Expiry Time (dalam menit)
define('EXPIRY_MINUTES', 60);

// Save log
define('LOG_ENABLED', true);
define('LOG_FILE', __DIR__ . '/midtrans.log');

// Database connection untuk simpan transaksi
define('DB_HOST', 'localhost');
define('DB_USER', 'your_db_user');
define('DB_PASS', 'your_db_password');
define('DB_NAME', 'maha_lakshmi');
?>
