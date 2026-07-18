# 💳 MIDTRANS SETUP - Complete Guide

## 🇮🇩 Payment Gateway untuk Indonesia

**Status:** Setup Required
**Last Updated:** 18 Juli 2026

---

## 📋 DAFTAR ISI

1. [Apa itu Midtrans?](#apa-itu-midtrans)
2. [Pendaftaran](#pendaftaran)
3. [Setup Dashboard](#setup-dashboard)
4. [Integration](#integration)
5. [Testing](#testing)
6. [Agent Instructions](#agent-instructions)

---

## 1️⃣ APA ITU MIDTRANS?

```
CUSTOMER BAYAR                    UANG MASUK
    │                                  ▲
    │    ┌───────────────┐            │
    ├───►│   MIDTRANS    │────────────┘
    │    │  (Perantara)  │      Langsung ke
    │    └───────────────┘      Rekening Anda
    │           │
    │           ▼
    │    POTONG FEE (1-2%)
    │
    ▼
PRODUK/DIVISI
```

### ✅ Benefits:
- Terima: GoPay, OVO, QRIS, VA Bank, Kartu Kredit
- Dana masuk langsung ke rekening Anda (H+1)
- Tidak ada uang ditahan
- 100% Legal & Terpercaya

---

## 2️⃣ PENDAFTARAN

### Step-by-Step:

```
📱 CARA DAFTAR MIDTRANS

1️⃣ Buka Browser
   ➜ https://dashboard.midtrans.com

2️⃣ Klik "Daftar Sekarang"

3️⃣ Isi Form:
   ├─ Email: [email-perusahaan@domain.com]
   ├─ Password: [buat password kuat]
   └─ No HP: [nomor aktif]

4️⃣ Verifikasi Email
   ➜ Buka email → Klik link verifikasi

5️⃣ Login ke Dashboard

6️⃣ Lengkapi Data Bisnis:
   ├─ Nama Perusahaan: MAHA LAKSHMI HOLDINGS
   ├─ Jenis Bisnis: Teknologi / Digital
   ├─ Alamat: [alamat lengkap]
   ├─ NPWP: [nomor NPWP]
   └─ Rekening Bank: [untuk terima dana]
```

### ⚠️ Dokumen yang Dibutuhkan:

| Dokumen | Untuk | Status |
|---------|-------|--------|
| KTP Pemilik | Verifikasi identitas | Siapkan |
| NPWP | Legalitas bisnis | Siapkan |
| Rekening Bank | Terima dana | Siapkan |
| Logo Company | Branding | Opsional |

---

## 3️⃣ SETUP DASHBOARD

### Setelah Login, Lakukan Ini:

```
🎯 SETUP DASHBOARD MIDTRANS

A. CONFIGURATION → PAYMENT ACTIVATION
   ├─ ✅ GoPay (ON)
   ├─ ✅ OVO (ON)
   ├─ ✅ QRIS (ON)
   ├─ ✅ Bank Transfer VA (ON)
   │    ├─ BCA Virtual Account
   │    ├─ Mandiri Virtual Account
   │    ├─ BNI Virtual Account
   │    └─ BRI Virtual Account
   └─ ✅ Credit Card (ON)

B. CONFIGURATION → SNAP PREFERENCE
   ├─ Enable Snap (untuk popup pembayaran)
   └─ Set expiry time: 24 hours

C. CONFIGURATION → NOTIFICATION
   ├─ Enable HTTP Notification
   └─ URL: [akan diisi setelah setup website]
```

---

## 4️⃣ AMBIL API KEYS

### Untuk Integration:

```
🔑 API KEYS (Production)

1️⃣ Login ke Dashboard Midtrans
   ➜ https://dashboard.midtrans.com

2️⃣ Pilih Environment: "Production"

3️⃣ Pergi ke: Settings → Access Keys

4️⃣ Copy:
   ┌─────────────────────────────────────────────┐
   │  Server Key: [isi-dengan-server-key-anda]   │
   │  Client Key: [isi-dengan-client-key-anda]  │
   └─────────────────────────────────────────────┘

5️⃣ Simpan dengan AMAN (jangan share sembarangan)
```

### Test/Sandbox Keys (Untuk Development):

```
🔑 API KEYS (Sandbox - Testing)

1️⃣ Pergi ke: Settings → Access Keys

2️⃣ Pilih Environment: "Sandbox"

3️⃣ Copy:
   ┌─────────────────────────────────────────────┐
   │  Server Key: [isi-dengan-sandbox-server-key]│
   │  Client Key: [isi-dengan-sandbox-client-key]│
   └─────────────────────────────────────────────┘

⚠️ GUNAKAN SANDBOX UNTUK TESTING SAJA!
⚠️ GANTI KE PRODUCTION KEY SAAT MAU LIVE
```

---

## 5️⃣ INTEGRATION

### Opsi Integration:

```
╔════════════════════════════════════════════════════════════════╗
║                    PILIHAN INTEGRASI                     ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  1️⃣ SNAP (MUDAH - RECOMMENDED)                            ║
║     ├── Popup pembayaran sederhana                            ║
║     ├── Cocok untuk: Landing Page, Website                  ║
║     └── Setup: 30 menit                                     ║
║                                                                ║
║  2️⃣ DIRECT API (ADVANCED)                                  ║
║     ├── Integrasi custom                                     ║
║     ├── Cocok untuk: App Mobile                             ║
║     └── Setup: 2-4 jam                                     ║
║                                                                ║
║  3️⃣ WORDPRESS/WOOCOMMERCE PLUGIN                           ║
║     ├── Kalau pakai WordPress                               ║
║     ├── Install plugin                                      ║
║     └── Setup: 15 menit                                    ║
║                                                                ║
║  4️⃣ WHATSAPP LINK (PALING MUDAH)                          ║
║     ├── Tanpa website                                       ║
║     ├── Kirim link pembayaran via WA                       ║
║     └── Setup: 5 menit                                     ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
```

---

### Opsi 1: SNAP (Popup - Recommended)

```html
<!-- Include Midtrans Snap JS -->
<script src="https://app.midtrans.com/snap/snap.js" 
        data-client-key="[YOUR_CLIENT_KEY]"></script>

<!-- Button Pembayaran -->
<button id="pay-button">Bayar Sekarang</button>

<!-- Script -->
<script>
document.getElementById('pay-button').onclick = function() {
    // Ambil snap_token dari server Anda
    snap.pay('[SNAP_TOKEN]', {
        onSuccess: function(result) {
            // Pembayaran berhasil
            alert('Pembayaran berhasil!');
            console.log(result);
        },
        onPending: function(result) {
            // Menunggu pembayaran
            alert('Silakan selesaikan pembayaran');
        },
        onError: function(result) {
            // Error
            alert('Pembayaran gagal');
        }
    });
};
</script>
```

---

### Opsi 2: WHATSAPP LINK (Paling Mudah - Tidak Perlu Website)

```html
<!-- Link Pembayaran Midtrans via WhatsApp -->
<a href="https://wa.me/[NOMOR_HP]?text=
Hai,%20saya%20mau%20beli%20[NAMA_PRODUK]%20seharga%20Rp%20[HARGA]

Bisa%20bayar%20via%20link%20ini:
[MIDTRANS_PAYMENT_LINK]

Metode%20bayar:
-%20GoPay
-%20OVO
-%20QRIS
-%20Kartu%20Kredit
-%20Transfer%20Bank

Terima%20kasih!"
class="btn">Bayar via WhatsApp</a>
```

---

### Opsi 3: WordPress + WooCommerce

```
📦 WORDPRESS SETUP

1️⃣ Install Plugin:
   ➜ Plugins → Add New
   ➜ Search: "Midtrans WooCommerce"
   ➜ Install & Activate

2️⃣ Configure:
   ➜ WooCommerce → Settings → Payments
   ➜ Enable Midtrans
   ➜ Masukkan Server Key & Client Key
   ➜ Save

3️⃣ Test:
   ➜ Buat produk dummy
   ➜ Checkout dengan test payment
   ➜ Verifikasi berhasil

4️⃣ Go Live:
   ➜ Ganti Sandbox Key → Production Key
   ➜ Enable "Production Mode"
```

---

## 6️⃣ TESTING

### Test dengan Sandbox:

```
🧪 TESTING CHECKLIST

1️⃣ Login Sandbox
   ➜ https://dashboard.sandbox.midtrans.com

2️⃣ Enable Test Mode di website

3️⃣ Test Transactions:
   ├─ ✅ Test GoPay
   ├─ ✅ Test OVO
   ├─ ✅ Test QRIS (scan dengan aplikasi)
   ├─ ✅ Test VA Bank
   └─ ✅ Test Credit Card

4️⃣ Cek Notification:
   ➜ Settings → Notification URL
   ➜ Pastikan URL bisa diakses

5️⃣ Cek Dashboard:
   ➜ Transactions → List
   ➜ Lihat apakah test transaction muncul
```

### Test Card Numbers:

```
💳 KARTU TEST (Credit Card)

Success:      4811 1111 1111 1114
Failed:       4111 1111 1111 1111

CVV: 任意 3 digits
Expiry: Any future date
```

---

## 7️⃣ AGENT INSTRUCTIONS

### Untuk Tim Agent:

```
🤖 INSTRUKSI UNTUK AGENT

A. MEMBERIKAN LINK PEMBAYARAN KE CUSTOMER

   1. Customer pilih produk
   2. Agent generate payment link via Midtrans
   3. Kirim link ke customer via WhatsApp
   4. Customer klik link → Bayar
   5. Midtrans proses → Dana masuk rekening
   6. Agent dapat notifikasi
   7. Produk dikirim ke customer

B. MONITORING PEMBAYARAN

   1. Buka Midtrans Dashboard
   2. Pergi ke: Transactions → List
   3. Filter by: Date / Status / Payment Type
   4. Status:
      ├─ Pending = Belum dibayar
      ├─ Settlement = Sudah dibayar ✅
      └─ Expire = Link kadaluarsa

C. LAPORAN KE CEO

   1. Agent catat semua transaksi
   2. Update revenue tracker
   3. Kirim laporan harian ke CEO
```

---

## 8️⃣ FLOW LENGKAP

```
╔══════════════════════════════════════════════════════════════════════╗
║                    ALUR PEMBAYARAN LENGKAP                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  1. AGENT PROMOSIKAN PRODUK                                         ║
║     │                                                                ║
║     ▼                                                                ║
║  2. CUSTOMER INTERES                                                 ║
║     │                                                                ║
║     ▼                                                                ║
║  3. AGENT KIRIM PAYMENT LINK (Midtrans)                            ║
║     │                                                                ║
║     ▼                                                                ║
║  4. CUSTOMER BUKA LINK                                              ║
║     │                                                                ║
║     ▼                                                                ║
║  5. CUSTOMER PILIH METODE BAYAR                                     ║
║     │                                                                ║
║     ├─ GoPay                                                         ║
║     ├─ OVO                                                           ║
║     ├─ QRIS                                                         ║
║     ├─ Kartu Kredit                                                 ║
║     └─ Transfer VA Bank                                              ║
║     │                                                                ║
║     ▼                                                                ║
║  6. CUSTOMER BAYAR                                                  ║
║     │                                                                ║
║     ▼                                                                ║
║  7. MIDTRANS VERIFIKASI (1-60 detik)                               ║
║     │                                                                ║
║     ▼                                                                ║
║  8. 💰 DANA MASUK REKENING PERUSAHAAN (H+1)                        ║
║     │                                                                ║
║     ▼                                                                ║
║  9. AGENT NOTIFIKASI: "Pembayaran berhasil!"                        ║
║     │                                                                ║
║     ▼                                                                ║
║  10. AGENT KIRIM PRODUK/JASA KE CUSTOMER                           ║
║     │                                                                ║
║     ▼                                                                ║
║  11. ✅ TRANSAKSI SELESAI                                           ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## 9️⃣ TROUBLESHOOTING

### Common Issues:

| Issue | Solution |
|-------|----------|
| Payment not received | Cek H+1, mungkin masih proses |
| Link expired | Generate new link, default 24 jam |
| Customer can't pay | Pastikan link sudah benar |
| Not getting notification | Check Notification URL |
| Test mode not working | Verify Sandbox keys |

### Contact Midtrans:

```
📞 MIDTRANS SUPPORT

Email:  support@midtrans.com
Phone:  021-5678-1234
Chat:   Dashboard → Help Center
```

---

## 🔐 SECURITY

### Best Practices:

```
✅ AMAN:
├─ Jangan share Server Key
├─ Simpan API keys di .env file
├─ Use HTTPS untuk semua endpoint
└─ Enable 2FA di dashboard

❌ JANGAN:
├─ Hardcode keys di code
├─ Share keys via chat/email
└─ Use Sandbox key di Production
```

---

## 📞 NEXT STEPS

```
📋 TODO LIST

□ 1. Daftar Midtrans (jika belum)
□ 2. Lengkapi verifikasi bisnis
□ 3. Ambil Production API Keys
□ 4. Enable payment methods
□ 5. Setup di website/landing page
□ 6. Test dengan sandbox
□ 7. Go Live!
□ 8. Training agent
□ 9. Monitor & optimize
```

---

## 💰 BIAYA

```
╔════════════════════════════════════════════════════════════════╗
║                    BIAYA MIDTRANS                           ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  💳 Credit Card     : 2.9% + Rp 2.500 per transaksi          ║
║  💰 GoPay / OVO     : 2.5% per transaksi                     ║
║  📱 QRIS            : 0.5% per transaksi                     ║
║  🏦 Virtual Account : 1.5% per transaksi                     ║
║                                                                ║
║  📝 Biaya Bulanan   : GRATIS                               ║
║  📊 Setup Fee       : GRATIS                               ║
║  📈 Penalty Fee     : GRATIS                               ║
║                                                                ║
║  ⚠️ Minimum transaksi: Rp 1.000                              ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
```

---

## 📚 REFERENCES

- **Dashboard:** https://dashboard.midtrans.com
- **Docs:** https://docs.midtrans.com
- **Support:** support@midtrans.com
- **Guide:** https://midtrans.com/payment

---

**Created:** 18 Juli 2026
**Status:** Ready for Setup
**For:** MAHA LAKSHMI HOLDINGS

---

*"Setup Midtrans = Customer bisa bayar dengan nyaman!"* 💳
