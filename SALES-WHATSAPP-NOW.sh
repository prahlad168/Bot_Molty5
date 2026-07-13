#!/bin/bash
# 🚀 SALES WHATSAPP - KIRIM SEKARANG!
# Script untuk langsung kirim pesan WhatsApp ke leads

echo "╔════════════════════════════════════════════════════════════════════════╗"
echo "║     🚀 SALES WHATSAPP - IMMEDIATE OUTREACH                     ║"
echo "║     Target: CLOSING DEALS & REVENUE!                           ║"
echo "╚════════════════════════════════════════════════════════════════════════╝"
echo ""

# Warna
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# WhatsApp API Configuration (contoh - perlu diganti dengan API nyata)
WHATSAPP_API="https://api.whatsapp.com/send"

# Lead messages - pesan langsung ke leads
MESSAGE_1="Halo! 👋

Saya dari MAHA LAKSHMI HOLDINGS.

Kami menyediakan solusi AI untuk bisnis Bali:
✅ AI Chatbot untuk Hotel & Restaurant
✅ Digital Marketing 
✅ Website & App Development

Mau konsultasi gratis 15 menit?

Balas YA untuk jadwalkan demo!

Terima kasih 🙏"

MESSAGE_2="Halo! 👋

MAHA LAKSHMI HOLDINGS

Solusi Digital AI untuk bisnis Anda:
🌐 Website Professional
📱 Mobile App
🤖 AI Chatbot
📊 Digital Marketing

Gratis konsultasi 15 menit!

Mau coba? Reply YA! 🙏"

# Leads untuk dikontak SEKARANG
LEADS=(
  "Four Seasons Resort Sayan - Ubud"
  "Viceroy Bali - Ubud"
  "AYANA Resort - Jimbaran"
  "Hotel Ubud Jaya"
  "Bintang Bali Tours"
)

echo "📋 LEADS UNTUK DIKONTAK SEKARANG:"
echo "─────────────────────────────────────"
i=1
for lead in "${LEADS[@]}"; do
  echo "$i. $lead"
  ((i++))
done
echo ""

echo "💬 PESAN YANG AKAN DIKIRIM:"
echo "─────────────────────────────────────"
echo "$MESSAGE_1"
echo ""

echo "⚠️  MANUAL ACTION REQUIRED:"
echo "─────────────────────────────────────"
echo "1. Buka WhatsApp"
echo "2. Kirim pesan ke leads di atas"
echo "3. Tunggu reply"
echo "4. Follow up sampai CLOSING"
echo ""

echo "📱 KONTAK LEADS (via WhatsApp):"
echo "─────────────────────────────────────"
echo "1. Four Seasons: +62 361 977577"
echo "2. Viceroy Bali: +62 361 971755"
echo "3. AYANA Resort: +62 361 702222"
echo "4. Hotel Ubud Jaya: +62 81xx xxxx xxxx"
echo "5. Bintang Bali Tours: +62 81xx xxxx xxxx"
echo ""

echo "🎯 TARGET CLOSING HARI INI:"
echo "─────────────────────────────────────"
echo "Deal 1: Rp 5.000.000 (Hotel Partnership)"
echo "Deal 2: Rp 3.000.000 (Tour Website)"
echo "Deal 3: Rp 2.000.000 (Social Media)"
echo "─────────────────────────────"
echo "TOTAL TARGET: Rp 10.000.000"
echo "CEO SHARE (60%): Rp 6.000.000 → BTC 🪙"
echo ""

echo "✅ SELESAI!"
echo "Sekarang buka WhatsApp dan mulai outreach! 🚀"
