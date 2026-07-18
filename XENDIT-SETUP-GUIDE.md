# 💳 XENDIT SETUP GUIDE
## 🇮🇩 Payment Gateway untuk Indonesia (dan Asia Tenggara)

**Status:** Ready for Setup
**Last Updated:** 18 Juli 2026

---

## 📋 DAFTAR ISI

1. [Apa itu Xendit?](#1-apa-itu-xendit)
2. [Pendaftaran](#2-pendaftaran)
3. [Setup Dashboard](#3-setup-dashboard)
4. [Integration](#4-integration)
5. [Testing](#5-testing)
6. [Agent Instructions](#6-agent-instructions)

---

## 1️⃣ APA ITU XENDIT?

```
CUSTOMER BAYAR                    UANG MASUK
    │                                  ▲
    │    ┌───────────────┐            │
    ├───►│   XENDIT     │────────────┘
    │    │  (Perantara)  │      Langsung ke
    │    └───────────────┘      Rekening Anda (H+1)
    │           │
    │           ▼
    │    POTONG FEE (2-2.5%)
    │
    ▼
PRODUK / JASA
```

### ✅ Benefits:
- Terima: GoPay, OVO, QRIS, VA Bank, Credit Card, Alfamart
- Dana masuk ke rekening Anda (H+1)
- Tidak ada uang ditahan
- API sangat mudah
- Onboarding cepat (1-2 jam approve!)
- Focus di Indonesia & Asia Tenggara
- Support bahasa Indonesia! 🇮🇩

---

## 2️⃣ PENDAFTARAN

### Step-by-Step:

```
📱 CARA DAFTAR XENDIT

1️⃣ Buka Browser
   ➜ https://dashboard.xendit.co

2️⃣ Klik "Daftar Gratis"

3️⃣ Pilih Tipe Akun:
   ├─ Personal / Freelancer
   └─ Business / Company ← Pilih ini

4️⃣ Isi Form Registrasi:
   ├─ Email: [email-perusahaan@domain.com]
   ├─ Password: [buat password kuat]
   ├─ Confirm Password: [ulangi password]
   └─ Klik "Daftar"

5️⃣ Verifikasi Email
   ➜ Buka email → Klik link verifikasi

6️⃣ Login ke Dashboard

7️⃣ Lengkapi Data Bisnis:
   
   📋 DATA PERUSAHAAN:
   ├─ Business Name: MAHA LAKSHMI HOLDINGS
   ├─ Business Type: Private Limited (PT)
   ├─ Industry: Technology / Digital Services
   ├─ Website: [website-anda.com]
   ├─ Business Description: Digital products and services
   └─ Expected Monthly Volume: [estimate]

   📋 DATA PEMILIK:
   ├─ Full Name: [Nama Lengkap]
   ├─ Email: [email]
   ├─ Phone: [nomor HP]
   └─ ID Number: [NIK/KTP]

   📋 DATA REKENING:
   ├─ Bank: [BCA / Mandiri / BNI / BRI]
   ├─ Account Number: [nomor rekening]
   └─ Account Holder: [nama pemilik rekening]

8️⃣ Upload Dokumen:
   ├─ KTP/SIM/Paspor
   ├─ NPWP (jika ada)
   └─ SIUP/TDP (jika company)

9️⃣ Submit & Tunggu Approval
   ⏱️ Biasanya approve dalam 1-2 jam!
```

### ⚠️ Dokumen yang Dibutuhkan:

| Dokumen | Untuk | Wajib? |
|---------|-------|--------|
| Email | Akun | ✅ Ya |
| Nomor HP | Verifikasi | ✅ Ya |
| KTP/SIM | Identitas | ✅ Ya |
| NPWP | Pajak | Opsional |
| Rekening Bank | Terima dana | ✅ Ya |
| Foto Diri + KTP | KYC | ✅ Ya |

---

## 3️⃣ SETUP DASHBOARD

### Setelah Login & Approved:

```
🎯 SETUP DASHBOARD XENDIT

A. AKTIVASI METODE BAYAR
   ➜ Settings → Payment Methods
   
   🇮🇩 INDONESIA:
   ├─ ✅ GoPay (ON)
   ├─ ✅ OVO (ON)
   ├─ ✅ QRIS (ON)
   ├─ ✅ Dana (ON)
   ├─ ✅ LinkAja (ON)
   ├─ ✅ Alfamart (ON)
   └─ ✅ Credit Card (ON)
   
   🏦 VIRTUAL ACCOUNT:
   ├─ ✅ BCA Virtual Account
   ├─ ✅ Mandiri Virtual Account
   ├─ ✅ BNI Virtual Account
   ├─ ✅ BRI Virtual Account
   ├─ ✅ Permata Virtual Account
   └─ ✅ Maybank Virtual Account

B. SETUP NOTIFICATIONS
   ➜ Settings → Notifications
   
   ├─ ✅ Email notification (ON)
   ├─ ✅ SMS notification (ON)
   ├─ ✅ Webhook (untuk API)
   └─ URL: https://yoursite.com/webhook

C. API KEYS
   ➜ Settings → API Keys
   
   ┌─────────────────────────────────────────────────┐
   │  PRODUCTION KEY:                                 │
   │  YOUR_XENDIT_LIVE_KEY         │
   │                                                  │
   │  TEST KEY (Development):                         │
   │  YOUR_XENDIT_DEV_KEY      │
   └─────────────────────────────────────────────────┘

D. WITHDRAWAL SETTINGS
   ➜ Settings → Payout
   
   ├─ Auto withdrawal: ON
   ├─ Schedule: Daily (H+1)
   └─ Bank Account: [your bank account]
```

---

## 4️⃣ AMBIL API KEYS

### Untuk Integration:

```
🔑 API KEYS

1️⃣ Login ke Xendit Dashboard
   ➜ https://dashboard.xendit.co

2️⃣ Pergi ke: Settings → API Keys

3️⃣ Pilih Environment:

   DEVELOPMENT (Testing):
   ┌─────────────────────────────────────────────────┐
   │  API Key: YOUR_XENDIT_DEV_KEY          │
   │  Callback URL: https://your-site.com/callback   │
   └─────────────────────────────────────────────────┘

   PRODUCTION (Real Money):
   ┌─────────────────────────────────────────────────┐
   │  API Key: YOUR_XENDIT_LIVE_KEY                 │
   │  Callback URL: https://your-site.com/callback   │
   └─────────────────────────────────────────────────┘

⚠️ PENTING:
- YOUR_XENDIT_DEV_KEY = untuk testing (sandbox)
- YOUR_XENDIT_LIVE_KEY = untuk production (REAL money)
- GANTI ke LIVE KEY saat mau go live!
```

---

## 5️⃣ INTEGRATION

### Opsi 1: Xendit Payment Link (Tanpa Coding!)

```
💳 PAYMENT LINK - PALING MUDAH

1️⃣ Buka: https://dashboard.xendit.co/payment-links

2️⃣ Klik "+ New Payment Link"

3️⃣ Isi Form:
   ┌─────────────────────────────────────────────────┐
   │  Basic Info:                                     │
   │  ├─ Name: [Nama Produk]                        │
   │  ├─ Description: [Deskripsi]                   │
   │  └─ Currency: IDR                               │
   │                                                  │
   │  Pricing:                                       │
   │  ├─ Amount: [Harga dalam Rupiah]               │
   │  └─ Minimal Amount: [minimum]                   │
   │                                                  │
   │  Payment Methods:                                │
   │  ├─ ☐ GoPay                                    │
   │  ├─ ☐ OVO                                     │
   │  ├─ ☐ QRIS                                    │
   │  ├─ ☐ Credit Card                             │
   │  ├─ ☐ Virtual Account                         │
   │  └─ ☐ Alfamart                                │
   │                                                  │
   │  Settings:                                       │
   │  ├─ Expiry: 24 hours                           │
   │  └─ ☐ Allow Multiple Use                       │
   └─────────────────────────────────────────────────┘

4️⃣ Klik "Create Payment Link"

5️⃣ Copy Link:
   - Link пример: https://checkout.xendit.co/web/xxxxx

6️⃣ Kirim ke Customer via WhatsApp

✅ SELESAI! Gak perlu coding!
```

---

### Opsi 2: WhatsApp + Xendit (Paling Simpel)

```
📱 WHATSAPP FLOW

1️⃣ Agent buat Xendit Payment Link (via dashboard)

2️⃣ Kirim ke Customer via WhatsApp:
   
   "Hai Kak! 👋
   
   Pembayaran untuk [PRODUK]:
   💰 Harga: Rp [HARGA]
   
   Bayar via link ini:
   [XENDIT_PAYMENT_LINK]
   
   Bisa bayar pake:
   ✅ GoPay
   ✅ OVO
   ✅ QRIS
   ✅ Transfer Bank
   ✅ Kartu Kredit
   ✅ Alfamart
   
   Setelah bayar, produk langsung dikirim! 🎉"

3️⃣ Customer klik link → Bayar

4️⃣ Xendit proses → Dana masuk rekening (H+1)

5️⃣ Agent dapat notifikasi

6️⃣ Kirim produk ke customer
```

---

### Opsi 3: WordPress + Xendit Plugin

```
📦 WORDPRESS SETUP

1️⃣ Install Plugin:
   ➜ Plugins → Add New
   ➜ Search: "Xendit WooCommerce"
   ➜ Install & Activate

2️⃣ Configure:
   ➜ WooCommerce → Settings → Payments
   ➜ Xendit
   
   ┌─────────────────────────────────────────────────┐
   │  Xendit Settings:                               │
   │  ├─ Enable/Disable: ON                        │
   │  ├─ API Key: [YOUR_XENDIT_LIVE_KEY]                 │
   │  ├─ Callback Key: [from Xendit dashboard]      │
   │  ├─ Prefix: [ORDER_]                           │
   │  └─ Due Date: 24 hours                        │
   │                                                  │
   │  Payment Methods:                                │
   │  ├─ ☑ Credit Card                             │
   │  ├─ ☑ GoPay                                    │
   │  ├─ ☑ OVO                                     │
   │  ├─ ☑ QRIS                                    │
   │  ├─ ☑ BCA VA                                 │
   │  ├─ ☑ Mandiri VA                              │
   │  ├─ ☑ BNI VA                                 │
   │  ├─ ☑ BRI VA                                 │
   │  └─ ☑ Alfamart                                │
   └─────────────────────────────────────────────────┘

3️⃣ Save

4️⃣ Test dengan Test Mode

5️⃣ Go Live → Ganti ke Live API Key
```

---

### Opsi 4: Direct API Integration

```javascript
// Contoh Integration (Node.js)

const xendit = require('xendit-node');

const x = new xendit({
  secretKey: 'YOUR_XENDIT_DEV_KEY' // Ganti dengan API key Anda
});

const { PaymentRequest } = x;

// Buat Payment Request
async function createPayment() {
  try {
    const resp = await PaymentRequest.create({
      amount: 100000, // Rp 100,000
      currency: 'IDR',
      paymentMethod: {
        type: 'EWALLET',
        ewallet: {
          channelCode: 'GCASH', // atau 'OVO', 'DANA', dll
          channelProperties: {
            successReturnUrl: 'https://yoursite.com/success',
            failureReturnUrl: 'https://yoursite.com/failed'
          }
        }
      },
      customer: {
        givenNames: 'John Doe',
        email: 'john@example.com'
      },
      metadata: {
        orderId: 'ORDER-123'
      }
    });
    
    console.log('Payment URL:', resp.actions.mobileWebCheckoutUrl);
  } catch (e) {
    console.error('Error:', e.message);
  }
}

createPayment();
```

---

## 6️⃣ TESTING

### Test dengan Development Mode:

```
🧪 TESTING CHECKLIST

1️⃣ Gunakan Development Key:
   ➜ Settings → API Keys
   ➜ Use: YOUR_XENDIT_DEV_KEY

2️⃣ Test Payment Methods:

   ┌────────────────────────────────────────────────────┐
   │  TEST CARD (Credit Card):                          │
   │  Number: 4000 0000 0000 0000                      │
   │  CVV: 123                                         │
   │  Expiry: 12/2025                                   │
   │  Result: Should succeed                           │
   └────────────────────────────────────────────────────┘

   ┌────────────────────────────────────────────────────┐
   │  TEST EWALLET:                                    │
   │  Skip to payment page in sandbox                  │
   │  Use "SUCCEEDED" button to simulate success       │
   └────────────────────────────────────────────────────┘

   ┌────────────────────────────────────────────────────┐
   │  TEST VIRTUAL ACCOUNT:                            │
   │  Use test VA number provided by Xendit             │
   └────────────────────────────────────────────────────┘

3️⃣ Cek di Dashboard:
   ➜ Transactions → List
   ➜ Filter: Test Transactions
   ➜ Verify status: SUCCEEDED
```

---

## 7️⃣ AGENT INSTRUCTIONS

### Untuk Tim Agent:

```
🤖 INSTRUKSI UNTUK AGENT

A. BUAT PAYMENT LINK (Xendit Dashboard)

   1. Buka: https://dashboard.xendit.co
   2. Pergi ke: Payment Links
   3. Klik "+ New Payment Link"
   4. Isi:
      - Nama produk
      - Harga
      - Metode bayar (pilih semua)
   5. Copy link
   6. Kirim ke customer via WhatsApp

B. MONITORING PEMBAYARAN

   1. Buka Xendit Dashboard
   2. Pergi ke: Transactions
   3. Filter:
      ├─ Date
      ├─ Status
      └─ Payment Method
   4. Status:
      ├─ PENDING = Belum dibayar
      ├─ SUCCEEDED = ✅ SUDAH DIBAYAR
      ├─ FAILED = ❌ GAGAL
      └─ EXPIRED = Link expired

C. JIKA PAID:
   1. Kirim produk ke customer
   2. Update revenue tracker
   3. Kirim laporan ke CEO

D. JIKA PENDING > 24 JAM:
   1. Follow up customer
   2. Tanya sudah transfer belum
   3. Jika belum, generate new link
```

---

## 8️⃣ FLOW LENGKAP

```
╔══════════════════════════════════════════════════════════════════════╗
║                    XENDIT PAYMENT FLOW                          ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  1. AGENT PROMOSIKAN PRODUK                                        ║
║     │                                                                ║
║     ▼                                                                ║
║  2. CUSTOMER INTERES                                                 ║
║     │                                                                ║
║     ▼                                                                ║
║  3. AGENT BUAT PAYMENT LINK (Xendit Dashboard)                     ║
║     │                                                                ║
║     ▼                                                                ║
║  4. AGENT KIRIM LINK via WhatsApp                                 ║
║     │                                                                ║
║     ▼                                                                ║
║  5. CUSTOMER BUKA LINK                                              ║
║     │                                                                ║
║     ▼                                                                ║
║  6. CUSTOMER PILIH METODE BAYAR                                     ║
║     │                                                                ║
║     ├─ 💚 GoPay                                                      ║
║     ├─ 🟣 OVO                                                       ║
║     ├─ ⬜ QRIS                                                      ║
║     ├─ 💳 Kartu Kredit                                              ║
║     ├─ 🏦 Transfer VA                                               ║
║     └─ 🏪 Alfamart                                                  ║
║     │                                                                ║
║     ▼                                                                ║
║  7. CUSTOMER BAYAR                                                  ║
║     │                                                                ║
║     ▼                                                                ║
║  8. XENDIT VERIFIKASI (1-60 detik)                                ║
║     │                                                                ║
║     ▼                                                                ║
║  9. 💰 DANA MASUK REKENING (H+1)                                  ║
║     │                                                                ║
║     ▼                                                                ║
║  10. AGENT DAPAT NOTIFIKASI EMAIL/WHATSAPP                        ║
║     │                                                                ║
║     ▼                                                                ║
║  11. AGENT KIRIM PRODUK                                           ║
║     │                                                                ║
║     ▼                                                                ║
║  12. ✅ SELESAI                                                    ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## 9️⃣ BIAYA

```
╔════════════════════════════════════════════════════════════════════╗
║                    BIAYA XENDIT                               ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  💳 Credit Card     : 2.5% per transaksi                       ║
║  💚 GoPay           : 2.0% per transaksi                       ║
║  🟣 OVO             : 2.0% per transaksi                       ║
║  ⬜ QRIS            : 0.5% per transaksi                       ║
║  📱 DANA/Linka      : 2.0% per transaksi                       ║
║  🏦 Virtual Account : 1.5% per transaksi                       ║
║  🏪 Alfamart        : 2.5% per transaksi                       ║
║                                                                    ║
║  📝 Biaya Bulanan   : GRATIS                                   ║
║  📊 Setup Fee       : GRATIS                                   ║
║  📈 Penalty Fee     : GRATIS                                   ║
║  📦 Minimum         : Rp 10.000                               ║
║                                                                    ║
║  💡 Contoh:                                                       ║
║     Customer bayar Rp 100.000 via GoPay:                        ║
║     Xendit fee: Rp 2.000 (2%)                                 ║
║     Anda terima: Rp 98.000                                    ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
```

---

## 🔟 METODE BAYAR YANG TERSEDIA

```
╔════════════════════════════════════════════════════════════════════╗
║                METODE BAYAR XENDIT                           ║
╠════════════════════════════════════════════════════════════════════╣
║                                                                    ║
║  💚 EWALLET (Paling Populer):                                   ║
║  ├── GoPay                                                       ║
║  ├── OVO                                                         ║
║  ├── DANA                                                        ║
║  ├── LinkAja                                                     ║
║  └── ShopeePay                                                   ║
║                                                                    ║
║  ⬜ QRIS (Universal):                                            ║
║  └── Scan dari semua bank/e-wallet                              ║
║                                                                    ║
║  💳 KARTU:                                                       ║
║  ├── Visa                                                        ║
║  ├── Mastercard                                                  ║
║  └── JCB                                                         ║
║                                                                    ║
║  🏦 VIRTUAL ACCOUNT:                                            ║
║  ├── BCA                                                         ║
║  ├── Mandiri                                                     ║
║  ├── BNI                                                        ║
║  ├── BRI                                                        ║
║  ├── Permata                                                    ║
║  └── Maybank                                                    ║
║                                                                    ║
║  🏪 RETAIL:                                                       ║
║  ├── Alfamart                                                   ║
║  └── Indomaret                                                  ║
║                                                                    ║
║  📱 OTHERS:                                                       ║
║  └── Akulaku                                                     ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
```

---

## 🔐 SECURITY

```
✅ AMAN:
├─ PCI DSS Level 1 compliant
├─ 256-bit encryption
├─ 2FA untuk dashboard
├─ Tokenization untuk card data
└─ Fraud detection built-in

❌ JANGAN:
├─ Simpan card data di server sendiri
├─ Share API key via chat
├─ Hardcode keys di code
└─ Use development key di production
```

---

## 📞 SUPPORT

```
❓ XENDIT SUPPORT

📧 Email: support@xendit.co
📞 Phone: 021-8066-0666
💬 WhatsApp: +62-812-xxxx-xxxx (via dashboard)
📖 Docs: https://docs.xendit.co
📱 App: Xendit Business (Android/iOS)
🌐 Website: https://xendit.co
```

---

## 📋 TODO LIST

```
□ 1. Daftar Xendit: dashboard.xendit.co
□ 2. Verifikasi email & HP
□ 3. Upload dokumen KYC
□ 4. Tunggu approval (1-2 jam biasanya)
□ 5. Setup payment methods
□ 6. Generate first payment link
□ 7. Test dengan development key
□ 8. Go Live → Ganti ke live key
□ 9. Training agent
□ 10. Monitor transactions
```

---

## 📚 REFERENCES

- **Register:** https://dashboard.xendit.co/register
- **Docs:** https://docs.xendit.co
- **Payment Links:** https://dashboard.xendit.co/payment-links
- **Dashboard:** https://dashboard.xendit.co
- **Support:** support@xendit.co

---

## 💡 TIPS

```
💡 PRO TIPS:

1. GUNAKAN PAYMENT LINK DULU
   - Tidak perlu coding
   - Langsung bisa pakai
   - Setup dalam 5 menit

2. ENABLE SEMUA METODE BAYAR
   - Biar customer pilih sendiri
   - Lebih banyak conversion

3. SET EXPIRY 24 JAM
   - Link tidak expired terlalu cepat
   - Tapi juga tidak terlalu lama

4. AUTO WITHDRAWAL
   - Aktifkan agar dana langsung masuk
   - Tidak perlu manual tarik

5. WHATSAPP NOTIFICATION
   - Aktifkan agar dapat notifikasi
   - Langsung tahu kalau ada pembayaran
```

---

**Created:** 18 Juli 2026
**Status:** Ready for Setup
**For:** MAHA LAKSHMI HOLDINGS

---

*"Bayar mudah dari seluruh Indonesia dengan Xendit!"* 🇮🇩💳
