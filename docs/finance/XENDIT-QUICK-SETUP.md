# 💳 XENDIT PAYMENT SETUP GUIDE

## ⚡ QUICK SETUP - 3 LANGKAH

### Step 1: Daftar Xendit (5 menit)
```
🌐 Buka: https://dashboard.xendit.co/register
📧 Masukkan email & password
✅ Verifikasi email
```

### Step 2: Submit Dokumen (10 menit)
```
📋 Dokumen yang dibutuhkan:
- KTP (atas nama sendiri)
- NPWP (jika ada)
- Foto selfie dengan KTP
- Rekening bank aktif

⏰ Approval: 1-2 hari kerja
```

### Step 3: Get API Key (1 menit)
```
1. Login ke dashboard.xendit.co
2. Menu: Settings → API Keys
3. Copy "Production API Key"
4. Simpan aman!
```

---

## 🔧 INTEGRATION

### Option A: PHP (Server-side)
```php
<?php
// xendit-config.php
define('XENDIT_API_KEY', 'xnd_live_xxxxxxxxxxxxx');

function createInvoice($order_id, $amount, $email, $description) {
    $ch = curl_init('https://api.xendit.co/v2/invoices');
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query([
        'external_id' => $order_id,
        'amount' => $amount,
        'payer_email' => $email,
        'description' => $description,
        'payment_methods' => ['OVO', 'DANA', 'LINKAJA', 'BCA', 'MANDIRI', 'BNI', 'BRI', 'QRIS']
    ]));
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Authorization: Basic ' . base64_encode(XENDIT_API_KEY . ':')
    ]);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    return json_decode(curl_exec($ch), true);
}
?>
```

### Option B: HTML Button (Simple)
```html
<!-- Taruh di website -->
<button onclick="payWithXendit()">Bayar Sekarang</button>

<script src="https://js.xendit.co/xendit.js"></script>
<script>
Xendit.setPublishableKey('xnd_public_xxxxx');

function payWithXendit() {
    Xendit.card.createToken({
        amount: 1000000,
        currency: 'IDR',
        card_number: '4000000000000002',
        card_exp_month: '12',
        card_exp_year: '2025',
        card_cvn: '123',
        is_multiple_use: false,
        description: 'Bali Travel Tour'
    }, response => {
        if (response.error) {
            alert(response.error.message);
        } else {
            // Kirim response.token ke server
            console.log(response.token);
        }
    });
}
</script>
```

---

## 📱 XENDIT FEATURES

| Feature | Description |
|---------|-------------|
| 💳 Virtual Account | BCA, Mandiri, BNI, BRI, Permata |
| 📱 E-Wallet | OVO, DANA, LinkAja, ShopeePay |
| 📲 QRIS | Semua bank + e-wallet |
| 💳 Credit Card | Visa, Mastercard, JCB |
| 🏪 Convenience Store | Alfamart, Indomaret |

---

## 💰 FEE STRUCTURE

| Payment Method | Fee |
|---------------|-----|
| Virtual Account | 2.5% |
| E-Wallet | 2.5% |
| QRIS | 1.5% |
| Credit Card | 2.9% |

---

## 🎯 QUICK ACTION CHECKLIST

- [ ] Daftar di https://dashboard.xendit.co/register
- [ ] Submit KTP & dokumen
- [ ] Tunggu approval (1-2 hari)
- [ ] Get API Key
- [ ] Test payment di sandbox
- [ ] Go live!

---

## 📞 Support Xendit
- 📧 Email: support@xendit.co
- 💬 WhatsApp: +62 21 3000 9999
- 🌐 Docs: https://docs.xendit.co

---

**Created:** 2026-07-19
**Status:** 📋 READY TO SETUP
