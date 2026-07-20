# 📧 Email SMTP Setup Guide - MAHA LAKSHMI

## 🎯 Tujuan
Setup Email SMTP agar AI agents bisa auto-send email ke leads secara otomatis.

---

## 📋 Prerequisites

- [ ] **Email Domain** (gmail, outlook, atau domain sendiri)
- [ ] **App Password** (untuk Gmail)
- [ ] **Leads Database** dengan email addresses

---

## 🔧 STEP 1: Gmail SMTP (Gratis)

### A. Enable 2-Factor Authentication

1. Buka https://myaccount.google.com
2. Klik **Security**
3. Aktifkan **2-Step Verification**

### B. Generate App Password

1. Buka https://myaccount.google.com/security
2. Cari **App passwords**
3. Select app: **Mail**
4. Select device: **Other (Custom name)**
5. Masukkan: **MAHA LAKSHMI**
6. Klik **Generate**
7. **COPY PASSWORD** (16 karakter, format: xxxx xxxx xxxx xxxx)

### C. Email Credentials

```
Email: mahalakshmidigital@gmail.com
App Password: xxxx xxxx xxxx xxxx
SMTP Server: smtp.gmail.com
SMTP Port: 587
```

---

## 🔧 STEP 2: Outlook/Hotmail SMTP (Gratis)

```
Email: your_email@outlook.com
Password: your_password
SMTP Server: smtp-mail.outlook.com
SMTP Port: 587
```

---

## 🔧 STEP 3: Domain Email (Professional)

### Untuk: mahalakshmi.web.id

1. Setup MX records di domain registrar
2. Buat email: info@mahalakshmi.web.id
3. Gunakan SMTP dari hosting provider

### SMTP Configuration:

```
SMTP Server: mail.mahalakshmi.web.id
SMTP Port: 587
Username: info@mahalakshmi.web.id
Password: [hosting password]
Encryption: TLS
```

---

## 📧 Email Templates untuk Leads

### Template 1: Initial Outreach

```
SUBJECT: Partnership Opportunity - Digital Transformation

Hi [NAME],

I'm reaching out from MAHA LAKSHMI Digital Holdings, 
an Indonesian tech company specializing in:

• Software Development
• Digital Marketing  
• AI Automation
• E-Commerce Solutions

We're expanding our reach and would love to discuss how 
we can help [COMPANY] with digital transformation.

Would you be open to a 15-minute call this week?

Best regards,
i Made Purna Ananda
CEO, MAHA LAKSHMI Digital Holdings
WhatsApp: +62 813 3755 8787
```

### Template 2: Follow-up

```
SUBJECT: Re: Partnership Opportunity

Hi [NAME],

Just following up on my previous email.

Have you had a chance to consider our proposal?

We're currently offering special rates for early partners.

Let me know if you'd like to schedule a call.

Best,
```

### Template 3: Bali Travel Partnership

```
SUBJECT: Partnership Opportunity - Bali Travel Platform

Hi [NAME],

I'm from Bali Travel Platform, a leading travel 
technology company in Indonesia.

We're looking for hotel and villa partners to 
collaborate on exclusive tour packages.

BENEFITS:
✓ 15% commission per booking
✓ No upfront costs
✓ Professional licensed guides
✓ Real-time booking system

Would you be interested in learning more?

Best regards,
Bali Travel Platform
WhatsApp: +62 813 3755 8787
```

### Template 4: Tech Solutions

```
SUBJECT: Digital Solutions for [COMPANY]

Hi [NAME],

I came across [COMPANY] and was impressed by your work.

MAHA LAKSHMI Digital offers:

SOFTWARE DEVELOPMENT:
• Website Development - from Rp 2.000.000
• Mobile Apps - from Rp 15.000.000
• Custom Software - Custom pricing

DIGITAL MARKETING:
• SEO & Content - from Rp 2.500.000/month
• Social Media - from Rp 3.000.000/month
• Google Ads - from Rp 2.000.000/month

AI SOLUTIONS:
• Chatbots - from Rp 5.000.000
• Automation - from Rp 15.000.000

Would you be open to a free consultation?

Best regards,
i Made Purna Ananda
WhatsApp: +62 813 3755 8787
```

---

## 🚀 Quick Test - Send Email

### Test dengan curl:

```bash
curl -X POST "https://api.sendgrid.com/v3/mail/send" \
-H "Authorization: Bearer $SENDGRID_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "personalizations": [{"to": [{"email": "test@example.com"}]}],
  "from": {"email": "info@mahalakshmi.web.id"},
  "subject": "Test Email",
  "content": [{"type": "text/plain", "value": "Hello from MAHA LAKSHMI!"}]
}'
```

---

## ✅ Checklist

- [ ] Email account created
- [ ] 2FA enabled (Gmail)
- [ ] App password generated
- [ ] SMTP credentials saved
- [ ] Test email sent successfully
- [ ] Email templates ready

---

## 📞 Recommended Email Services

| Provider | Cost | Best For |
|----------|------|----------|
| **Gmail** | Free | Testing, small scale |
| **Outlook** | Free | Testing, small scale |
| **SendGrid** | Free (100/day) | Automation |
| **Mailgun** | Free (5K/month) | High volume |
| **Amazon SES** | Very cheap | Production |

---

**Last Updated:** 2026-07-20
**Status:** 🔧 Setup Required
