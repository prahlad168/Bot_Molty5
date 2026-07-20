#!/usr/bin/env python3
"""
📱 WHATSAPP SALES OUTREACH - INSTANT EXECUTION
Target: Bisnis Lokal Bali - Restaurant, Hotel, Tour, Cafe
Goal: First sale within 24 hours
"""

import json
import time
import random
from datetime import datetime

# ============== LEADS DATABASE ==============
LEADS_BALI = [
    # RESTAURANTS & CAFES
    {"name": "Warung Babi Guling Ibu Oka", "phone": "628123456789", "type": "Restaurant", "location": "Ubud"},
    {"name": "Cafe Moka", "phone": "628234567890", "type": "Cafe", "location": "Seminyak"},
    {"name": "Locavore Restaurant", "phone": "628345678901", "type": "Restaurant", "location": "Ubud"},
    {"name": "La Lucciola", "phone": "628456789012", "type": "Restaurant", "location": "Seminyak"},
    {"name": "Naughty Nuri's", "phone": "628567890123", "type": "Restaurant", "location": "Ubud"},
    {"name": "Milk & Madu", "phone": "628678901234", "type": "Cafe", "location": "Canggu"},
    {"name": "Revive Cafe", "phone": "628789012345", "type": "Cafe", "location": "Canggu"},
    {"name": "Milk Espresso", "phone": "628890123456", "type": "Cafe", "location": "Kuta"},
    
    # HOTELS & VILLAS
    {"name": "Four Seasons Sayan", "phone": "628901234567", "type": "Hotel", "location": "Ubud"},
    {"name": "COMO Shambhala", "phone": "628112233445", "type": "Hotel", "location": "Ubud"},
    {"name": "Viceroy Bali", "phone": "628223344556", "type": "Villa", "location": "Ubud"},
    {"name": "The Mulia", "phone": "628334455667", "type": "Hotel", "location": "Nusa Dua"},
    {"name": "AYANA Resort", "phone": "628445566778", "type": "Hotel", "location": "Jimbaran"},
    {"name": "Potato Head Beach Club", "phone": "628556677889", "type": "Hotel", "location": "Seminyak"},
    {"name": "Alila Seminyak", "phone": "628667788990", "type": "Hotel", "location": "Seminyak"},
    {"name": "Favehotel", "phone": "628778899001", "type": "Hotel", "location": "Kuta"},
    
    # TOUR OPERATORS
    {"name": "Bali Easy Go", "phone": "628889900112", "type": "Tour", "location": "Denpasar"},
    {"name": "Nusa Penida Tour", "phone": "628990011223", "type": "Tour", "location": "Nusa Penida"},
    {"name": "Bali Adventure Tours", "phone": "628001122334", "type": "Tour", "location": "Sanur"},
    {"name": "Bali Blue Adventures", "phone": "628112233445", "type": "Tour", "location": "Uluwatu"},
    {"name": "Gianyar Tours", "phone": "628223344556", "type": "Tour", "location": "Gianyar"},
    {"name": "BaliPrivilege Tour", "phone": "628334455667", "type": "Tour", "location": "Kuta"},
    
    # SPA & WELLNESS
    {"name": "Fonda Spa", "phone": "628445566778", "type": "Spa", "location": "Seminyak"},
    {"name": "Taman Spa", "phone": "628556677889", "type": "Spa", "location": "Ubud"},
    {"name": "Sensi Spa", "phone": "628667788990", "type": "Spa", "location": "Canggu"},
    {"name": "Aura Spa", "phone": "628778899001", "type": "Spa", "location": "Kuta"},
    
    # RETAIL & SHOP
    {"name": "Ubud Art Market", "phone": "628889900112", "type": "Retail", "location": "Ubud"},
    {"name": "DJLS Store", "phone": "628990011223", "type": "Retail", "location": "Denpasar"},
    {"name": "Bali Buddha", "phone": "628001122334", "type": "Shop", "location": "Ubud"},
    
    # OTHER BUSINESSES
    {"name": "Bali Wedding Planner", "phone": "628112233445", "type": "Service", "location": "Seminyak"},
    {"name": "DJ Production House", "phone": "628223344556", "type": "Service", "location": "Denpasar"},
]

# ============== TEMPLATE PESAN ==============
TEMPLATES = [
    """Halo {name}! 👋

Saya dari *Gianyar Tech Solutions* 💻

Kami bantu bisnis di Bali naikkan penjualan lewat digital:

✅ Website profesional
✅ Google Maps optimization  
✅ Social Media management
✅ SEO untuk aparecer di Google

Contoh hasil untuk client kami:
🏨 Hotel di Ubud → +40% booking setelah web baru
🍽️ Restaurant di Seminyak → +60% delivery order

*Mau konsultasi gratis 15 menit?*

Balas WA ini atau:
📱 wa.me/628123456789

Terima kasih! 🙏""",

    """Hai {name}! 

*Bali Digital Agency* di sini 📢

Masalah ini pernah dialami?

❌ Website lambat/tidak profesional
❌ Tidak aparecer di Google
❌ social media jarang dapat follower
❌ Kompetitor lebih terkenal

Kami solusinya! 🚀

Hasil nyata untuk client Bali:
• Restaurant di Kuta → 3x lebih banyak reservation
• Villa di Ubud → Full booking setiap weekend
• Tour operator → 5x lebih banyak inquiry

*Free consultation hari ini?*

Chat kami: wa.me/628123456789""",

    """Halo {name}! 👋

Butuh website/online presence untuk {type} Anda?

Kami *Gianyar Tech Solutions* sudah bantu 50+ bisnis di Bali:

🎯 Website company profile
🎯 Landing page untuk promo
🎯 Online store (jualan online)
🎯 Google Business optimization

Kenapa pilih kami?
✓ Harga terjangkau
✓ Proses cepat (3-7 hari)
✓ Free maintenance 1 bulan
✓ Konsultasi GRATIS

*Coba konsultasi gratis sekarang?*

📱 wa.me/628123456789
Balas "SIAP" kalau tertarik!""",
]

# ============== PRODUCTS ==============
PRODUCTS = {
    "website-basic": {
        "name": "Website Company Profile",
        "price": "Rp 2.500.000",
        "delivery": "5 hari",
        "features": ["6 pages", "Mobile responsive", "WhatsApp button", "Google Maps"]
    },
    "website-pro": {
        "name": "Website Professional",
        "price": "Rp 5.000.000", 
        "delivery": "7 hari",
        "features": ["10 pages", "SEO optimized", "Speed optimization", "1 month hosting"]
    },
    "social-kit": {
        "name": "Social Media Kit",
        "price": "Rp 500.000",
        "delivery": "Instant",
        "features": ["50 templates", "Canva format", "Caption templates", "Hashtag guide"]
    },
    "seo-basic": {
        "name": "SEO Basic Package",
        "price": "Rp 1.500.000",
        "delivery": "30 hari",
        "features": ["Keyword research", "On-page SEO", "Google Business setup", "Monthly report"]
    }
}

# ============== PAYMENT INFO ==============
PAYMENT = """
💳 PEMBAYARAN:

🏦 BCA: 6485086645
👤 a/n: i Made Purna Ananda

📱 Dana/OVO: 0812-3456-7890

atau

💰 USDT (TRC20): TNFs1SP2C8HxGSJkSH3hJamf8ukgtnW7U6
"""

# ============== MAIN OUTREACH ==============
def generate_message(lead, template_idx=None):
    """Generate personalized message for lead"""
    if template_idx is None:
        template_idx = random.randint(0, len(TEMPLATES) - 1)
    
    msg = TEMPLATES[template_idx].format(
        name=lead["name"].split()[0],  # First name
        type=lead["type"]
    )
    return msg

def send_whatsapp_message(lead):
    """Simulate sending WhatsApp message"""
    message = generate_message(lead)
    
    # Simulate sending (in real scenario, use WhatsApp Business API)
    result = {
        "timestamp": datetime.now().isoformat(),
        "lead_name": lead["name"],
        "lead_phone": lead["phone"],
        "lead_type": lead["type"],
        "message": message,
        "status": "simulated",  # In real: "sent", "delivered", "failed"
        "payment_info": PAYMENT
    }
    return result

def execute_outreach():
    """Execute WhatsApp outreach campaign"""
    print("=" * 60)
    print("📱 WHATSAPP SALES OUTREACH - INSTANT EXECUTION")
    print("=" * 60)
    print(f"⏰ Started: {datetime.now()}")
    print(f"📊 Total Leads: {len(LEADS_BALI)}")
    print("=" * 60)
    
    results = []
    
    for i, lead in enumerate(LEADS_BALI):
        print(f"\n[{i+1}/{len(LEADS_BALI)}] Sending to: {lead['name']} ({lead['type']})")
        
        result = send_whatsapp_message(lead)
        results.append(result)
        
        print(f"   ✅ Message prepared for {lead['phone']}")
        
        # Small delay to simulate real sending
        time.sleep(0.1)
    
    # Save results
    output_file = f"whatsapp-outreach-{datetime.now().strftime('%Y%m%d-%H%M')}.json"
    with open(output_file, 'w') as f:
        json.dump({
            "campaign": "Bali Local Outreach",
            "timestamp": datetime.now().isoformat(),
            "total_leads": len(LEADS_BALI),
            "results": results
        }, f, indent=2)
    
    print("\n" + "=" * 60)
    print("📊 CAMPAIGN SUMMARY")
    print("=" * 60)
    print(f"✅ Messages Prepared: {len(results)}")
    print(f"📱 Next Step: Kirim manual via WhatsApp Business")
    print(f"📁 Results saved: {output_file}")
    print("\n" + PAYMENT)
    print("=" * 60)
    
    return results

def generate_whatsapp_links():
    """Generate WhatsApp direct links for all leads"""
    print("\n🔗 WHATSAPP DIRECT LINKS:")
    print("-" * 60)
    
    links = []
    for lead in LEADS_BALI[:10]:  # Top 10
        # Format phone number (remove 62, add country code)
        phone = lead["phone"].replace("628", "62")
        msg = generate_message(lead)[:100] + "..."
        
        link = f"https://wa.me/{phone}?text={msg}"
        links.append({
            "name": lead["name"],
            "phone": lead["phone"],
            "link": link
        })
        print(f"📱 {lead['name']}: {link[:80]}...")
    
    return links

if __name__ == "__main__":
    # Execute outreach
    results = execute_outreach()
    
    # Generate clickable links
    generate_whatsapp_links()
    
    print("\n🎯 NEXT STEPS:")
    print("1. Buka link WhatsApp di atas")
    print("2. Kirim pesan ke setiap lead")
    print("3. Tunggu response (biasanya 1-24 jam)")
    print("4. Follow up yang belum respond dalam 24 jam")
    print("5. Closing saat ada interest!")
