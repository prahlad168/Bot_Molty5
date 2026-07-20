# ✅ WhatsApp Business API - Quick Checklist

## 📋 10 Steps to Go Live

---

### 🟢 PHASE 1: Account Setup (15 min)

- [ ] **Step 1:** Buka https://business.facebook.com
- [ ] **Step 2:** Klik "Create Account"
- [ ] **Step 3:** Isi:
  ```
  Business Name: MAHA LAKSHMI Digital
  Email: [email Pak Pur]
  ```
- [ ] **Step 4:** Verify email

---

### 🟢 PHASE 2: WhatsApp Business (15 min)

- [ ] **Step 5:** Di WhatsApp section → Klik "Get Started"
- [ ] **Step 6:** Klik "Add Phone Number"
- [ ] **Step 7:** Masukkan: **813 3755 8787**
- [ ] **Step 8:** Verify via SMS (kode 6 digit)

---

### 🟢 PHASE 3: API Setup (20 min)

- [ ] **Step 9:** Buka https://developers.facebook.com
- [ ] **Step 10:** Klik "Create App" → Pilih "Business"
- [ ] **Step 11:** App Name: **MAHA LAKSHMI WhatsApp**
- [ ] **Step 12:** Di sidebar → Add Product → WhatsApp
- [ ] **Step 13:** Copy credentials:
  ```
  Phone Number ID: _______________
  Access Token: _______________
  WhatsApp Business Account ID: _______________
  ```

---

### 🟢 PHASE 4: Update Config (5 min)

- [ ] **Step 14:** Edit `automation/whatsapp-send.php`
  ```php
  'phone_number_id' => 'PASTE_ID_DISINI',
  'access_token' => 'PASTE_TOKEN_DISINI',
  ```

- [ ] **Step 15:** Edit `automation/webhook-whatsapp.php`
  ```php
  $ACCESS_TOKEN = "PASTE_TOKEN_DISINI";
  $PHONE_NUMBER_ID = "PASTE_ID_DISINI";
  ```

---

### 🟢 PHASE 5: Test (5 min)

- [ ] **Step 16:** Test send message:
  ```bash
  php automation/whatsapp-send.php --lead=1 --dry-run
  ```

- [ ] **Step 17:** Kirim "halo" ke WhatsApp 813 3755 8787
- [ ] **Step 18:** Harus dapat auto-reply!

---

## 🎯 CREDENTIALS TRACKER

Copy dan isi credentials di bawah ini:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📱 WHATSAPP BUSINESS CREDENTIALS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Phone Number:        +62 813 3755 8787
Phone Number ID:    _______________________________
                    (Di WhatsApp API Setup page)

Access Token:       _______________________________
                    (Di Graph API Explorer)

WhatsApp Business Account ID:
                    _______________________________
                    (Di WhatsApp API Setup page)

Verify Token:       maha_lakshmi_verify_token_2026

Webhook URL:        https://[domain-anda].com/webhook-whatsapp.php

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## ⚡ QUICK TEST COMMANDS

### Test 1: Dry Run
```bash
php automation/whatsapp-send.php --lead=1 --dry-run
```

### Test 2: Send to Lead 1
```bash
php automation/whatsapp-send.php --lead=1
```

### Test 3: Send to All Leads
```bash
php automation/whatsapp-send.php --all
```

### Test 4: Follow-up Sequence
```bash
php automation/whatsapp-send.php --all --type=followup_day3
```

---

## 📱 AUTO-REPLY TEST

WhatsApp number: **+62 813 3755 8787**

| Test Message | Expected Response |
|-------------|------------------|
| `halo` | Welcome menu |
| `hai` | Welcome menu |
| `1` | Software services |
| `2` | Digital marketing |
| `3` | AI solutions |
| `4` | E-commerce |
| `partnership` | Partnership info |
| `harga` | Price list |

---

## 🚨 COMMON ISSUES

| Error | Solution |
|-------|---------|
| "Phone not registered" | Verify phone number again |
| "Token expired" | Generate permanent token |
| "Webhook failed" | Check URL & verify token match |
| "Rate limit" | Wait 24 hours or add delay |

---

## 📞 Need Help?

- **Documentation:** https://developers.facebook.com/docs/whatsapp
- **Support:** https://developers.facebook.com/support

---

**🎉 Selamat! WhatsApp API akan active setelah semua steps selesai!**
