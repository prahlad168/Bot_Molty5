# 📧 Email SMTP - Quick Start Guide

## ⚡ 5 Minutes Setup

---

## STEP 1: Buat Gmail App Password (2 menit)

1. Buka: **https://myaccount.google.com/security**

2. Aktifkan **2-Step Verification** (jika belum)

3. Buka: **https://myaccount.google.com/security** → App passwords

4. Select app: **Mail**

5. Select device: **Other (Custom name)** → ketik: **MAHA LAKSHMI**

6. Klik **Generate**

7. **COPY** password 16 karakter (format: xxxx xxxx xxxx xxxx)

---

## STEP 2: Update Config (1 menit)

Edit `automation/email-send.php`:

```php
$SMTP = [
    'host' => 'smtp.gmail.com',
    'port' => 587,
    'username' => 'mahalakshmidigital@gmail.com',  // GANTI
    'password' => 'xxxx xxxx xxxx xxxx',            // GANTI DENGAN APP PASSWORD
    'from_name' => 'MAHA LAKSHMI Digital',
    'from_email' => 'mahalakshmidigital@gmail.com'
];
```

---

## STEP 3: Test (2 menit)

```bash
# Preview only (tidak mengirim email)
php automation/email-send.php --lead=1 --dry-run

# Kirim ke lead ID 1
php automation/email-send.php --lead=1

# Kirim ke semua leads
php automation/email-send.php --all --dry-run
```

---

## 📧 Email Types

| Type | Usage |
|------|-------|
| `--type=outreach` | Initial outreach |
| `--type=followup` | Follow-up (Day 3-7) |
| `--type=final` | Final follow-up (Day 14) |
| `--type=bali_travel` | Bali Travel partnership |
| `--type=tech` | Tech solutions |

---

## 📊 Send to Leads

```bash
# Preview all leads
php automation/email-send.php --all --dry-run

# Send to all leads (outreach)
php automation/email-send.php --all

# Send follow-up to all
php automation/email-send.php --all --type=followup

# Send Bali Travel partnership
php automation/email-send.php --all --type=bali_travel
```

---

## 📋 Credentials Tracker

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📧 EMAIL CREDENTIALS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Gmail Address: mahalakshmidigital@gmail.com
App Password:   _______________
SMTP Server:   smtp.gmail.com
SMTP Port:     587

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## ⚠️ Troubleshooting

| Error | Solution |
|-------|----------|
| "Authentication failed" | Check username & app password |
| "SMTP connection failed" | Check internet connection |
| "Rate limit exceeded" | Wait 24 hours |
| "Invalid email" | Check email format |

---

## 💡 Tips

- **Rate limit Gmail:** 500 emails/day
- **Recommended:** 100-200 emails/day
- **Delay:** Script sudah ada sleep(3) antar email
- **Dry-run:** Selalu test dulu dengan `--dry-run`

---

## 🎯 Next Steps

1. ✅ Setup Gmail App Password
2. ✅ Update config
3. ✅ Test dengan dry-run
4. 🚀 Send to leads!

---

**Good luck! 📧**
