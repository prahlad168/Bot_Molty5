# 📱 WhatsApp Business API - Complete Setup Guide

## 🎯 Untuk: Pak Pur (i Made Purna Ananda)
## 📅 Date: 2026-07-20

---

## 📋 Prerequisites

Sebelum mulai, pastikan Pak Pur punya:

- [ ] **Meta Account** (Facebook account yang sudah verified)
- [ ] **HP/Laptop** dengan browser
- [ ] **Phone number dedicated** untuk WhatsApp Business (belum dipake untuk WhatsApp biasa)
- [ ] **Email aktif** untuk verification

---

## 🔧 STEP 1: Create Meta Business Account

### Buka Meta Business Portal
1. Buka browser → kunjungi: **https://business.facebook.com**

2. Klik **"Create Account"**

3. Isi form:
   ```
   Business Name: MAHA LAKSHMI Digital
   First Name: i Made Purna
   Last Name: Ananda
   Email: [email Pak Pur]
   ```

4. Klik **Submit**

5. **Check email** → Klik link verification

✅ **Result:** Meta Business Account created!

---

## 🔧 STEP 2: Get WhatsApp Business API Access

### A. Daftar WhatsApp Business Platform

1. Buka: **https://business.facebook.com**

2. Klik **WhatsApp** di sidebar kiri

3. Klik **"Get Started"**

4. Pilih business account yang sudah dibuat

### B. Verify Phone Number

1. Klik **"Add Phone Number"**

2. Pilih **Indonesia** (+62)

3. Masukkan nomor: **813 3755 8787**
   - Format: 81337558877 (tanpa spasi)

4. Klik **Next**

5. **Tunggu SMS** → masukkan kode verification

6. ✅ **Phone number verified!**

### C. Setup Business Profile

1. Klik **"Edit Business Profile"**

2. Isi:
   ```
   Business Name: MAHA LAKSHMI Digital
   Description: Digital Solutions Company
   Address: Gianyar, Bali, Indonesia
   Industry: Technology
   ```

3. Klik **Save**

---

## 🔧 STEP 3: Get API Credentials

### A. Create Meta App

1. Buka: **https://developers.facebook.com**

2. Klik **"My Apps"** → **"Create App"**

3. Pilih **"Business"** → Klik **Next**

4. Isi:
   ```
   App Name: MAHA LAKSHMI WhatsApp
   App Contact Email: [email Pak Pur]
   ```

5. Klik **Create App**

### B. Add WhatsApp Product

1. Di App Dashboard → Klik **"Add Products"**

2. Cari **WhatsApp** → Klik **"Set Up"**

3. Klik **"API Setup"**

4. Pilih WhatsApp Business Account yang sudah dibuat

5. ✅ **WhatsApp product added!**

### C. Get Credentials

1. Di sidebar → Klik **WhatsApp** → **API Setup**

2. Scroll ke **"Your access tokens"**

3. Copy **Temporary Access Token** (akan expire dalam 24 jam)

4. Copy **Phone Number ID**

5. Copy **WhatsApp Business Account ID**

6. **SAVE SEMUA CREDENTIALS INI!**

---

## 🔧 STEP 4: Setup Webhook (untuk Auto-Reply)

### A. Persiapan Webhook URL

1. Pak Pur butuh **hosting dengan PHP**

2. Upload file `webhook-whatsapp.php` ke hosting

3. Webhook URL akan seperti:
   ```
   https://mahalaksmi.web.id/webhook-whatsapp.php
   ```

### B. Configure Webhook di Meta

1. Di WhatsApp API Setup → Cari **"Webhook"**

2. Klik **"Configure Webhook"**

3. Isi:
   ```
   Callback URL: https://mahalaksmi.web.id/webhook-whatsapp.php
   Verify Token: maha_lakshmi_verify_token_2026
   ```

4. Klik **Verify and Save**

5. ✅ **Webhook configured!**

---

## 🔧 STEP 5: Update Config Files

### Edit automation/whatsapp-send.php

```php
$CONFIG = [
    'phone_number_id' => 'PASTE_PHONE_NUMBER_ID_DISINI',
    'access_token' => 'PASTE_ACCESS_TOKEN_DISINI',
    'leads_file' => 'archives/LEADS-DATABASE.json',
    'log_file' => 'whatsapp-send-log.txt'
];
```

### Edit automation/webhook-whatsapp.php

```php
$VERIFY_TOKEN = "maha_lakshmi_verify_token_2026";
$ACCESS_TOKEN = "PASTE_ACCESS_TOKEN_DISINI";
$PHONE_NUMBER_ID = "PASTE_PHONE_NUMBER_ID_DISINI";
```

---

## 🔧 STEP 6: Test WhatsApp API

### A. Test dengan curl (Terminal)

```bash
curl -X POST "https://graph.facebook.com/v18.0/PHONE_NUMBER_ID/messages" \
-H "Authorization: Bearer ACCESS_TOKEN" \
-H "Content-Type: application/json" \
-d '{
    "messaging_product": "whatsapp",
    "to": "6281337558787",
    "type": "text",
    "text": {
        "body": "Test dari MAHA LAKSHMI! 🤖"
    }
}'
```

### B. Test dengan Script

```bash
# Preview only (dry-run)
php automation/whatsapp-send.php --lead=1 --dry-run

# Send to specific lead
php automation/whatsapp-send.php --lead=1

# Send to all leads
php automation/whatsapp-send.php --all
```

---

## 🔧 STEP 7: Generate Permanent Access Token

### A. Get Permanent Token

1. Buka: **https://developers.facebook.com**

2. Di App Dashboard → **Tools** → **Graph API Explorer**

3. Select App: MAHA LAKSHMI WhatsApp

4. Permissions: Tambahkan `whatsapp_business_management`

5. Klik **Generate Access Token**

6. **Approve permissions** di popup

7. Copy **Permanent Access Token**

### B. Update Config dengan Permanent Token

Update `whatsapp-send.php` dan `webhook-whatsapp.php` dengan permanent token.

---

## 📞 Test Auto-Reply

### Kirim pesan ke WhatsApp number:

1. Buka WhatsApp di HP
2. Kirim pesan ke **+62 813 3755 8787**
3. Ketik: **"halo"** atau **"hai"**
4. Harus dapat auto-reply!

---

## ⚠️ Troubleshooting

### Error: "Phone number not registered"
```
Solution: Verifikasi phone number lagi di WhatsApp Business
```

### Error: "Access token expired"
```
Solution: Generate permanent access token (Step 7)
```

### Error: "Webhook verification failed"
```
Solution: 
1. Check webhook URL accessible
2. Verify token match
3. Check PHP version (need 7.4+)
```

### Error: "Rate limit exceeded"
```
Solution: Tambah delay antar messages (sleep 5 detik)
```

---

## 💰 Biaya

| Item | Biaya | Notes |
|------|-------|-------|
| WhatsApp Business App | **FREE** | Dari Meta |
| Phone Number | Pak Pur punya | 813 3755 8787 |
| Hosting (untuk webhook) | ~Rp 50.000/bulan | Opsional |
| **Total Start** | **FREE** | Except hosting |

---

## 📊 Timeline

| Step | Time Needed |
|------|-----------|
| Step 1-3 | 15-30 menit |
| Step 4 | 10 menit |
| Step 5-6 | 10 menit |
| **Total** | **~1 jam** |

---

## ✅ Checklist Complete

- [ ] Meta Business Account created
- [ ] WhatsApp Business registered
- [ ] Phone number verified
- [ ] App created di Meta Developer
- [ ] WhatsApp product added
- [ ] Credentials saved
- [ ] Webhook configured
- [ ] Config files updated
- [ ] Test message sent successfully
- [ ] Auto-reply working

---

## 📞 Help & Support

- **Meta WhatsApp Business**: https://developers.facebook.com/docs/whatsapp
- **WhatsApp Business API**: https://business.whatsapp.com
- **Support**: Di Meta Developer Console

---

## 🎉 Success Criteria

WhatsApp Business API berhasil jika:

1. ✅ Bisa send message via API
2. ✅ Auto-reply berfungsi
3. ✅ AI agents bisa send ke leads
4. ✅ Lead response bisa di-handle

---

**Good luck, Pak Pur! 🇮🇩**

**Last Updated:** 2026-07-20
**Version:** 1.0
