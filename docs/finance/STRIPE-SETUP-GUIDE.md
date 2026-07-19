# 💳 STRIPE SETUP GUIDE
## 🌍 Payment Gateway untuk Global / International

**Status:** Ready for Setup
**Last Updated:** 18 Juli 2026

---

## 📋 DAFTAR ISI

1. [Apa itu Stripe?](#1-apa-itu-stripe)
2. [Pendaftaran](#2-pendaftaran)
3. [Setup Dashboard](#3-setup-dashboard)
4. [Integration](#4-integration)
5. [Testing](#5-testing)
6. [Agent Instructions](#6-agent-instructions)

---

## 1️⃣ APA ITU STRIPE?

```
CUSTOMER BAYAR                    UANG MASUK
    │                                  ▲
    │    ┌───────────────┐            │
    ├───►│    STRIPE    │────────────┘
    │    │  (Perantara)  │      Langsung ke
    │    └───────────────┘      Rekening Bank Anda
    │           │
    │           ▼
    │    POTONG FEE (2.9% + 30¢)
    │
    ▼
PRODUK / JASA
```

### ✅ Benefits:
- Terima: Visa, Mastercard, AMEX, Apple Pay, Google Pay
- Dana masuk ke rekening bank lokal (H+2)
- Tidak ada uang ditahan
- API paling mudah di industry
- 100% Legal & Global trusted

---

## 2️⃣ PENDAFTARAN

### Step-by-Step:

```
🌐 CARA DAFTAR STRIPE

1️⃣ Buka Browser
   ➜ https://dashboard.stripe.com/register

2️⃣ Klik "Get Started"

3️⃣ Isi Form:
   ├─ Email: [email-perusahaan@domain.com]
   ├─ Password: [buat password kuat]
   └─ Continue

4️⃣ Verifikasi Email
   ➜ Buka email → Klik link verifikasi

5️⃣ Lengkapi Profile:
   ├─ Full Name: [Nama Lengkap]
   ├─ Business Profile:
   │   ├─ Business Type: Company / Individual
   │   ├─ Business Name: MAHA LAKSHMI HOLDINGS
   │   ├─ Website: [website-anda.com]
   │   └─ Industry: Software / Services
   └─ Address: [Alamat Lengkap]

6️⃣ Tambahkan Bank Account:
   ├─ Pilih Country: Indonesia
   ├─ Routing Number: [isi]
   ├─ Account Number: [isi]
   └─ Simpan
```

### ⚠️ Dokumen yang Dibutuhkan:

| Dokumen | Untuk | Status |
|---------|-------|--------|
| Email | Akun | Siapkan |
| Bank Account | Terima dana | Siapkan |
| Website/Business | Verification | Opsional (bisa add nanti) |
| ID Verification | KYC | Butuh untuk payout penuh |

---

## 3️⃣ SETUP DASHBOARD

### Setelah Login:

```
🎯 SETUP DASHBOARD STRIPE

A. PAYMENT METHODS
   ➜ Settings → Payment Methods
   ├─ ✅ Enable Credit/Debit Cards
   ├─ ✅ Enable Apple Pay
   ├─ ✅ Enable Google Pay
   └─ ✅ Enable Link (Stripe's payment solution)

B. CUSTOMER PORTAL
   ➜ Settings → Customer Portal
   ├─ Enable invoice generation
   └─ Enable billing portal

C. WEBHOOK (untuk notifikasi)
   ➜ Developers → Webhooks
   ├─ Add Endpoint
   ├─ URL: https://your-server.com/webhook
   └─ Events: payment_intent.succeeded

D. API KEYS
   ➜ Developers → API Keys
   ├─ Publishable key (untuk frontend)
   └─ Secret key (untuk backend)
```

---

## 4️⃣ AMBIL API KEYS

### Untuk Integration:

```
🔑 API KEYS

1️⃣ Login ke Stripe Dashboard
   ➜ https://dashboard.stripe.com

2️⃣ Pergi ke: Developers → API Keys

3️⃣ Copy Keys:

   ┌─────────────────────────────────────────────────┐
   │  PUBLISHABLE KEY (Frontend/JavaScript):        │
   │  pk_live_YOUR_KEY_HERE        │
   │  pk_test_YOUR_KEY_HERE        │
   └─────────────────────────────────────────────────┘

   ┌─────────────────────────────────────────────────┐
   │  SECRET KEY (Backend/PHP/Python):               │
   │  sk_live_YOUR_KEY_HERE         │
   │  sk_test_YOUR_KEY_HERE         │
   └─────────────────────────────────────────────────┘

⚠️ PENTING:
- pk_test_YOUR_KEY_HERE = untuk testing (sandbox)
- pk_live_YOUR_KEY_HERE = untuk production (REAL money)
- JANGAN share secret key!
```

---

## 5️⃣ INTEGRATION

### Opsi 1: Stripe Checkout (Paling Mudah)

```html
<!-- Include Stripe.js -->
<script src="https://js.stripe.com/v3/"></script>

<!-- Button -->
<button id="checkout-button">Pay Now</button>

<script>
const stripe = Stripe('pk_test_YOUR_KEY_HERE');

document.getElementById('checkout-button').addEventListener('click', function() {
    // Redirect ke Stripe Checkout
    stripe.redirectToCheckout({
        lineItems: [{
            price: 'price_xxxxx', // Product ID dari Stripe
            quantity: 1,
        }],
        mode: 'payment',
        successUrl: 'https://yoursite.com/success',
        cancelUrl: 'https://yoursite.com/canceled',
    })
    .then(function(result) {
        if (result.error) {
            alert(result.error.message);
        }
    });
});
</script>
```

---

### Opsi 2: Stripe Payment Link (Tanpa Coding!)

```
💳 STRIPE PAYMENT LINK - PALING MUDAH

1️⃣ Buka: https://dashboard.stripe.com/payment-links

2️⃣ Klik "+ New"
   - Product: Create New
   - Name: [Nama Produk]
   - Price: [Harga dalam USD]
   - Currency: USD (atau sesuai)

3️⃣ Copy Payment Link
   - Link пример: https://buy.stripe.com/xxxxxxx

4️⃣ Kirim ke Customer
   - Via WhatsApp/Email
   - Customer klik → Bayar langsung

✅ SELESAI! Tidak perlu coding!
```

---

### Opsi 3: WordPress + Stripe Plugin

```
📦 WORDPRESS SETUP

1️⃣ Install Plugin:
   ➜ Plugins → Add New
   ➜ Search: "WP Simple Pay"
   ➜ Install & Activate

   ATAU

   ➜ Search: "Stripe for WooCommerce"
   ➜ Install & Activate

2️⃣ Configure:
   ➜ Settings → WP Simple Pay
   ➜ Masukkan Stripe API Keys
   ├─ Publishable Key
   └─ Secret Key

3️⃣ Create Payment Form:
   ➜ Simple Pay → Add New
   ➜ Customize form
   ➜ Save

4️⃣ Test:
   ➜ Use Stripe test cards
   ➜ Verify payment works

5️⃣ Go Live:
   ➜ Ganti Test Keys → Live Keys
```

---

## 5️⃣ TESTING

### Test dengan Test Mode:

```
🧪 TESTING CHECKLIST

1️⃣ Gunakan Test Mode:
   ➜ Dashboard → Test Mode (toggle di atas)

2️⃣ Test Cards:

   ┌────────────────────────────────────────────────────┐
   │  SUCCESS Cards:                                    │
   │  ├── 4242 4242 4242 4242 (Visa)                  │
   │  ├── 5555 5555 5555 4444 (Mastercard)            │
   │  └── 3782 8224 6310 005 (AMEX)                   │
   │                                                     │
   │  CVV: Any 3 digits                                │
   │  Expiry: Any future date                          │
   │  ZIP: Any 5 digits                                │
   └────────────────────────────────────────────────────┘

   ┌────────────────────────────────────────────────────┐
   │  FAIL Cards:                                       │
   │  ├── 4000 0000 0000 0002 (Declined)               │
   │  ├── 4000 0000 0000 9995 (Insufficient Funds)    │
   │  └── 4000 0000 0000 3228 (3D Secure required)    │
   └────────────────────────────────────────────────────┘

3️⃣ Cek di Dashboard:
   ➜ Payments → List
   ➜ Lihat test transactions
```

---

## 6️⃣ AGENT INSTRUCTIONS

### Untuk Tim Agent:

```
🤖 INSTRUKSI UNTUK AGENT

A. MEMBERIKAN PAYMENT LINK KE CUSTOMER (INTERNASIONAL)

   1. Customer pilih produk
   2. Agent generate Stripe Payment Link
   3. Kirim link ke customer via WhatsApp/Email
   4. Customer klik → Bayar dengan kartu kredit
   5. Stripe proses → Dana masuk rekening (H+2)
   6. Agent dapat notifikasi email
   7. Produk dikirim ke customer

B. MONITORING PEMBAYARAN

   1. Buka Stripe Dashboard
   2. Pergi ke: Payments
   3. Filter by: Date / Status
   4. Status:
      ├─ Succeeded = ✅ SUDAH DIBAYAR
      ├─ Pending = ⏳ PROSES
      └─ Failed = ❌ GAGAL

C. LAPORAN KE CEO

   1. Agent catat semua transaksi Stripe
   2. Update revenue tracker
   3. Kirim laporan harian
```

---

## 7️⃣ FLOW LENGKAP

```
╔══════════════════════════════════════════════════════════════════════╗
║                    STRIPE PAYMENT FLOW                         ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  1. AGENT PROMOSIKAN PRODUK (International Customer)                ║
║     │                                                                ║
║     ▼                                                                ║
║  2. CUSTOMER INTERES                                                 ║
║     │                                                                ║
║     ▼                                                                ║
║  3. AGENT KIRIM STRIPE PAYMENT LINK                               ║
║     │                                                                ║
║     ▼                                                                ║
║  4. CUSTOMER BUKA LINK                                              ║
║     │                                                                ║
║     ▼                                                                ║
║  5. CUSTOMER MASUKKAN KARTU KREDIT                                ║
║     │                                                                ║
║     ▼                                                                ║
║  6. STRIPE PROSES (1-60 detik)                                    ║
║     │                                                                ║
║     ▼                                                                ║
║  7. 💰 DANA MASUK REKENING (H+2)                                  ║
║     │                                                                ║
║     ▼                                                                ║
║  8. AGENT NOTIFIKASI: "Payment received!"                         ║
║     │                                                                ║
║     ▼                                                                ║
║  9. AGENT KIRIM PRODUK                                            ║
║     │                                                                ║
║     ▼                                                                ║
║  10. ✅ SELESAI                                                   ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## 8️⃣ BIAYA

```
╔════════════════════════════════════════════════════════════════════╗
║                    BIAYA STRIPE                               ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  💳 Credit Card     : 2.9% + $0.30 per transaction              ║
║  💳 International   : + 1% additional                            ║
║  💰 ACH Transfer    : 0.8% (max $5)                            ║
║  📱 Wallets        : Same as card                              ║
║                                                                    ║
║  📝 Biaya Bulanan  : GRATIS                                   ║
║  📊 Setup Fee      : GRATIS                                   ║
║  📈 Minimum        : Tidak ada                                ║
║                                                                    ║
║  💡 Contoh:                                                       ║
║     Customer bayar $100:                                        ║
║     Stripe fee: $2.90 + $0.30 = $3.20                         ║
║     Anda terima: $96.80                                        ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
```

---

## 9️⃣ NEGARA YANG DIDUKUNG

```
🌍 STRIPE SUPPORT 135+ NEGARA

Americas:
✅ USA, Canada, Mexico, Brazil, Argentina, dll

Europe:
✅ UK, Germany, France, Netherlands, Spain, Italy, dll

Asia Pacific:
✅ Australia, New Zealand, Singapore, Hong Kong, Japan, dll

Southeast Asia:
✅ Indonesia ✅, Malaysia, Thailand, Philippines, Vietnam, dll

Africa:
✅ South Africa, Kenya, Nigeria, dll

Middle East:
✅ UAE, Saudi Arabia, Israel, dll

⚠️ Note: Indonesia supported, tapi payout ke bank lokal butuh verifikasi tambahan
```

---

## 🔐 SECURITY

```
✅ AMAN:
├─ PCI DSS Level 1 compliant
├─ Encryption 256-bit
├─ 2FA untuk dashboard
└─ Tokenization untuk card data

❌ JANGAN:
├─ Simpan card data di server sendiri
├─ Share secret key
├─ Hardcode keys di code
└─ Use test key di production
```

---

## 📞 SUPPORT

```
❓ STRIPE SUPPORT

📧 Email: support@stripe.com
📖 Docs: https://stripe.com/docs
💬 Chat: Dashboard → Help → Chat
📝 Forum: https://community.stripe.com
```

---

## 📋 TODO LIST

```
□ 1. Daftar Stripe: stripe.com/register
□ 2. Verifikasi email & identity
□ 3. Tambahkan bank account
□ 4. Enable payment methods
□ 5. Test dengan sandbox
□ 6. Go Live!
□ 7. Training agent
□ 8. Monitor transactions
```

---

## 📚 REFERENCES

- **Register:** https://dashboard.stripe.com/register
- **Docs:** https://stripe.com/docs
- **Payment Links:** https://dashboard.stripe.com/payment-links
- **Dashboard:** https://dashboard.stripe.com

---

**Created:** 18 Juli 2026
**Status:** Ready for Setup
**For:** MAHA LAKSHMI HOLDINGS

---

*"Terima pembayaran global dengan Stripe!"* 🌍💳
