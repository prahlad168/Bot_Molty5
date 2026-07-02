# Payangan Hospital - Agent Workspace

## 📋 Overview

Repository ini berisi website RS Payangan Hospital dan konfigurasi automasi untuk deployment otomatis.

---

## 🏥 Project Info

| Field | Value |
|-------|-------|
| **Project** | Payangan Hospital Management System |
| **Repository** | `prahlad168/Payangan-Hospital` |
| **Domain** | `https://payanganhospital.gianyarkab.go.id/` |
| **Hosting** | Idwebhost (cPanel) |
| **Username cPanel** | `payangan` |

---

## 📁 Project Structure

```
├── index.html              # Homepage
├── about.html              # About page
├── dokter.html             # Doctor list
├── igd.html                # IGD/Emergency
├── kontak.html             # Contact page
├── progress/
│   └── index.html         # Progress dashboard
├── img/                    # Images folder
├── webhook.php             # Auto-deploy webhook script
└── ... (other hospital pages)
```

---

## 🤖 Available Skills

### 1. Webhook Auto-Deploy
**File:** `.agents/skills/webhook-auto-deploy.md`

Setup webhook untuk auto-deploy dari GitHub ke hosting Idwebhost.

**Yang sudah configured:**
- ✅ Webhook URL: `https://payanganhospital.gianyarkab.go.id/webhook.php`
- ✅ GitHub webhook active
- ✅ Auto-deploy working

### 2. OpenHands Daily Report
**File:** `.agents/skills/openhands-daily-report.md`

Automation untuk laporan progress harian otomatis jam 6 pagi WIB.

**Yang sudah configured:**
- ✅ Automation ID: `2e4d4f38-1c7c-4437-b25b-7d52f35d0ab7`
- ✅ Schedule: `0 6 * * *` (Asia/Jakarta)
- ✅ Output: `progress/daily-report-YYYY-MM-DD.md`

---

## 🚀 Deployment Flow

```
┌─────────────────┐
│  GitHub Push    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  GitHub         │
│  Webhook        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐     ┌──────────────────┐
│  Idwebhost      │────▶│  Website Updated │
│  webhook.php    │     │  ✅ Success      │
└─────────────────┘     └──────────────────┘
```

---

## 📅 Automation Schedule

| Task | Schedule | Output |
|------|----------|--------|
| Daily Progress Report | Setiap jam 6:00 pagi WIB | `progress/daily-report-*.md` |
| Progress Dashboard | Setiap push | `progress/index.html` |

---

## 🔧 Quick Commands

### Test Webhook:
```
https://payanganhospital.gianyarkab.go.id/webhook.php
```

### Trigger Automation Manually:
```bash
curl -X POST "https://app.all-hands.dev/api/automation/v1/2e4d4f38-1c7c-4437-b25b-7d52f35d0ab7/dispatch" \
  -H "Authorization: Bearer ${OPENHANDS_API_KEY}"
```

### Check Automation Status:
```bash
curl "https://app.all-hands.dev/api/automation/v1/2e4d4f38-1c7c-4437-b25b-7d52f35d0ab7" \
  -H "Authorization: Bearer ${OPENHANDS_API_KEY}"
```

---

## 📝 For Future Development

### Adding New Pages:
1. Create HTML file di repository
2. Push ke GitHub
3. Hosting auto-update via webhook

### Modifying Automation:
1. Edit prompt di OpenHands dashboard
2. Atau update via API

### Checking Logs:
- Webhook log: `/home/payangan/public_html/webhook.log`
- OpenHands runs: Via dashboard

---

## 🔒 Security Notes

- Webhook secret: Tidak dipakai (kosong) untuk simplicity
- Untuk production: Tambahkan secret verification
- GitHub token: Gunakan read-only access jika memungkinkan

---

## 📞 Contact

- **GitHub Owner:** prahlad168
- **Domain Admin:** Team Idwebhost

---

## ✅ Status

| Component | Status |
|-----------|--------|
| GitHub Repository | ✅ Active |
| Hosting Connected | ✅ Connected |
| Webhook | ✅ Working |
| Daily Automation | ✅ Active |
| Auto-Deploy | ✅ Ready |

---

**Last Updated:** 2026-07-02
