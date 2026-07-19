#!/usr/bin/env python3
"""
🚀 MASTER SALES EXECUTION SYSTEM
Complete automation for global sales
"""

import json
import time
from datetime import datetime

# =====================
# CONFIGURATION
# =====================
CONFIG = {
    "ceo_name": "[CEO_NAME_REDACTED]",
    "ceo_alias": "[CEO_ALIAS_REDACTED]",
    "whatsapp": "[PHONE_REDACTED]",
    "email": "[EMAIL_REDACTED]",
    "bank": "BCA",
    "bank_account": "[BANK_ACCOUNT]",
    "target_weekly": 500,
    "target_monthly": 2000
}

# =====================
# VALIDATED LEADS
# =====================
LEADS = [
    {
        "id": 1,
        "name": "Friendly Bali Tour",
        "company": "Tour Operator",
        "country": "Indonesia",
        "contact": "+62 853 3375 1528",
        "type": "WhatsApp",
        "value": 400,
        "service": "Video Content, Website, Social Media"
    },
    {
        "id": 2,
        "name": "The Ubud Village Resort",
        "company": "Resort",
        "country": "Indonesia",
        "contact": "+62 361 978 444",
        "type": "WhatsApp",
        "value": 500,
        "service": "Video Content, Social Media"
    },
    {
        "id": 3,
        "name": "Villa Semana",
        "company": "Resort",
        "country": "Indonesia",
        "contact": "info@villasemana.com",
        "type": "Email",
        "value": 400,
        "service": "Graphic Design, Social Media"
    },
    {
        "id": 4,
        "name": "Lion City Digital",
        "company": "Digital Agency",
        "country": "Singapore",
        "contact": "marcus@lioncitydigital.com",
        "type": "Email",
        "value": 800,
        "service": "Partnership, Video Editing"
    },
    {
        "id": 5,
        "name": "Adventure Indonesia",
        "company": "Tour DMC",
        "country": "Indonesia",
        "contact": "info@adventureindonesia.com",
        "type": "Email",
        "value": 600,
        "service": "Video, Website, SEO"
    }
]

# =====================
# WHATSAPP MESSAGES
# =====================
WHATSAPP_TEMPLATES = {
    "partnership": """🏝️ HALO! Partnership Tour dari Bali Travel! 🇮🇩

Kami tawarkan COMMISSION 15% per booking!

✅ Tanpa modal
✅ Tanpa stock
✅ Guides ready
✅ Booking system ready

Contoh: Booking 10 guests = Rp 1.500.000 untuk Anda!

Hubungi sekarang:
📱 wa.me/6281337558787

--
Bali Travel Platform""",

    "video_content": """Hi [NAME]!

Saya freelance video editor & content creator dari Bali.

Saya specialize di hospitality businesses. Bisa bantu bikin:
🎬 Video promo untuk Instagram/TikTok
📸 Content untuk website
🎨 Social media graphics

Portfolio: [YOUR_LINK]

Mau diskusi 5 menit? 📱

Terima kasih! 🙏""",

    "agency_partnership": """Hi [NAME]!

Saya freelance video editor based di Bali dengan experience di tourism & hospitality.

Open untuk partnership dengan agencies untuk overflow work.

Skills:
- Video editing (Premiere, DaVinci, CapCut)
- Motion graphics
- Social media content

Interested? Mari discuss! 📱"""
}

# =====================
# EMAIL TEMPLATES
# =====================
EMAIL_TEMPLATES = {
    "hotel_outreach": {
        "subject": "Partnership Opportunity for Your Resort",
        "body": """Hi,

I noticed [COMPANY] is doing great work in Bali's hospitality industry.

I'm a freelance video editor and content creator specializing in hotels and travel businesses. I help properties like yours create engaging content for social media, websites, and marketing materials.

Would you be open to a quick 15-minute call this week to discuss how we might work together?

Best regards,
[YOUR_NAME]
[YOUR_EMAIL]
[YOUR_PHONE]"""
    },
    
    "agency_partnership": {
        "subject": "Potential Partnership - Video Editor from Bali",
        "body": """Hi,

I came across [COMPANY] and I'm impressed by your work in [LOCATION]'s digital space.

I'm a freelance video editor based in Bali with experience working with travel and hospitality clients. I'm interested in exploring potential partnership opportunities where I could support your overflow work.

My skills:
- Video editing (Premiere Pro, DaVinci Resolve, CapCut)
- Motion graphics
- Social media content creation

Would you be open to a quick call to discuss?

Best regards,
[YOUR_NAME]
[PORTFOLIO_LINK]"""
    }
}

# =====================
# EXECUTION FUNCTIONS
# =====================
def print_header():
    print("""
╔════════════════════════════════════════════════════════════════╗
║     🚀 MASTER SALES EXECUTION SYSTEM                      ║
║     MAHA LAKSHMI HOLDINGS - GLOBAL SALES                 ║
╚════════════════════════════════════════════════════════════════╝
""")

def print_section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")

def generate_whatsapp_message(lead, template_type="video_content"):
    template = WHATSAPP_TEMPLATES[template_type]
    message = template.replace("[NAME]", lead["name"])
    message = message.replace("[YOUR_LINK]", "[YOUR_PORTFOLIO_LINK]")
    return message

def generate_email(lead, template_type):
    template = EMAIL_TEMPLATES[template_type]
    email = {
        "to": lead["contact"],
        "subject": template["subject"].replace("[COMPANY]", lead["company"]),
        "body": template["body"]
            .replace("[COMPANY]", lead["company"])
            .replace("[LOCATION]", lead["country"])
            .replace("[YOUR_NAME]", CONFIG["ceo_alias"])
            .replace("[YOUR_EMAIL]", CONFIG["email"])
            .replace("[YOUR_PHONE]", CONFIG["whatsapp"])
            .replace("[PORTFOLIO_LINK]", "[YOUR_PORTFOLIO_LINK]")
    }
    return email

def execute_outreach():
    """Execute all outreach actions"""
    print_section("📱 WHATSAPP OUTREACH")
    
    whatsapp_leads = [l for l in LEADS if l["type"] == "WhatsApp"]
    
    for i, lead in enumerate(whatsapp_leads, 1):
        message = generate_whatsapp_message(lead, "video_content")
        print(f"💬 WhatsApp #{i}")
        print(f"   To: {lead['name']} ({lead['contact']})")
        print(f"   Company: {lead['company']}")
        print(f"   Service: {lead['service']}")
        print(f"   Status: ✅ READY TO SEND")
        print(f"   Message:\n{'-'*40}\n{message[:100]}...\n{'-'*40}")
        print()

def execute_email_outreach():
    """Execute email outreach"""
    print_section("📧 EMAIL OUTREACH")
    
    email_leads = [l for l in LEADS if l["type"] == "Email"]
    
    for i, lead in enumerate(email_leads, 1):
        email = generate_email(lead, "hotel_outreach")
        print(f"📧 Email #{i}")
        print(f"   To: {email['to']}")
        print(f"   Subject: {email['subject']}")
        print(f"   Status: ✅ READY TO SEND")
        print()

def generate_fiverr_gigs():
    """Generate Fiverr gig configurations"""
    print_section("🎬 FIVERR GIGS READY")
    
    gigs = [
        {
            "title": "I will edit professional videos for YouTube, TikTok, and social media",
            "category": "Video & Animation > Video Editing",
            "price_basic": 25,
            "price_standard": 50,
            "price_premium": 100,
            "delivery_basic": "2 days",
            "delivery_standard": "3 days",
            "delivery_premium": "5 days"
        },
        {
            "title": "I will create stunning graphics for social media and marketing",
            "category": "Graphics & Design > Social Media Design",
            "price_basic": 30,
            "price_standard": 75,
            "price_premium": 150,
            "delivery_basic": "2 days",
            "delivery_standard": "4 days",
            "delivery_premium": "7 days"
        },
        {
            "title": "I will write compelling content for your website and blog",
            "category": "Writing & Translation > Articles & Blog Posts",
            "price_basic": 25,
            "price_standard": 75,
            "price_premium": 150,
            "delivery_basic": "2 days",
            "delivery_standard": "4 days",
            "delivery_premium": "7 days"
        }
    ]
    
    for i, gig in enumerate(gigs, 1):
        print(f"🎯 Gig #{i}: {gig['title']}")
        print(f"   Category: {gig['category']}")
        print(f"   Basic: ${gig['price_basic']} ({gig['delivery_basic']})")
        print(f"   Standard: ${gig['price_standard']} ({gig['delivery_standard']})")
        print(f"   Premium: ${gig['price_premium']} ({gig['delivery_premium']})")
        print(f"   Status: ✅ READY TO CREATE")
        print()

def generate_upwork_profile():
    """Generate Upwork profile configuration"""
    print_section("💼 UPWORK PROFILE READY")
    
    profile = {
        "title": "Video Editor | Graphic Designer | Content Creator",
        "overview": """I help tourism businesses, hotels, and travel companies create professional content that drives engagement and sales.

With expertise in video editing, graphic design, and content creation, I deliver high-quality work on time.

My Services:
• Video Editing (YouTube, TikTok, Reels, Promos)
• Graphic Design (Logos, Social Media, Marketing Materials)
• Content Writing (Blog posts, Website copy, Newsletters)
• Social Media Management

I have a fast turnaround time and excellent communication.

Let's discuss your project!""",
        "hourly_rate": 15,
        "skills": ["Video Editing", "Graphic Design", "Content Writing", "Social Media", "Tourism", "Hospitality"]
    }
    
    print(f"📝 Title: {profile['title']}")
    print(f"💰 Hourly Rate: ${profile['hourly_rate']}/hr")
    print(f"📋 Skills: {', '.join(profile['skills'])}")
    print(f"   Status: ✅ READY TO CREATE")
    print()

def print_tracking_sheet():
    """Generate tracking spreadsheet"""
    print_section("📊 TRACKING SHEET")
    
    print("""
┌────────────────────────────────────────────────────────────────────┐
│  # │ Company              │ Type    │ Contact           │ Status    │
├────────────────────────────────────────────────────────────────────┤
│  1 │ Friendly Bali Tour  │ WhatsApp│ +62 853 3375 1528│ ⏳       │
│  2 │ The Ubud Village    │ WhatsApp│ +62 361 978 444  │ ⏳       │
│  3 │ Villa Semana         │ Email   │ info@villasemana  │ ⏳       │
│  4 │ Lion City Digital   │ Email   │ marcus@lioncity  │ ⏳       │
│  5 │ Adventure Indonesia  │ Email   │ info@adventure   │ ⏳       │
└────────────────────────────────────────────────────────────────────┘
""")

def print_revenue_target():
    """Print revenue targets"""
    print_section("💰 REVENUE TARGETS")
    
    print(f"""
┌────────────────────────────────────────────────────────────────────┐
│                    💰 REVENUE TARGETS                             │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  TODAY:                                                           │
│  ├── WhatsApp Sent: 5                                            │
│  ├── Emails Sent: 5                                             │
│  └── Revenue: $0                                                │
│                                                                    │
│  THIS WEEK:                                                       │
│  ├── Target: $500-1000                                          │
│  ├── Fiverr Orders: 3-5 @ $50-75 = $150-375                    │
│  ├── Upwork Jobs: 2-3 @ $50-100 = $100-300                     │
│  └── Direct Sales: 1-2 @ $100-200 = $100-400                   │
│                                                                    │
│  CEO SHARE (60%):                                                │
│  ├── $500 × 60% = $300 → BCA {CONFIG['bank_account']}          │
│  └── $1000 × 60% = $600 → BCA {CONFIG['bank_account']}          │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
""")

def print_action_plan():
    """Print action plan"""
    print_section("🚀 ACTION PLAN - EXECUTE NOW")
    
    print("""
╔════════════════════════════════════════════════════════════════╗
║                    ✅ TODO LIST                             ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  ☐ Step 1: Create Fiverr Account (15 min)                  ║
║     → https://www.fiverr.com                                ║
║                                                                ║
║  ☐ Step 2: Create Upwork Account (15 min)                  ║
║     → https://www.upwork.com                                ║
║                                                                ║
║  ☐ Step 3: Create 3 Gigs on Fiverr (30 min)                ║
║     → Video Editing, Graphic Design, Content Writing         ║
║                                                                ║
║  ☐ Step 4: Send WhatsApp Messages (20 min)                  ║
║     → Use templates above                                    ║
║                                                                ║
║  ☐ Step 5: Send Emails (20 min)                           ║
║     → Use templates above                                    ║
║                                                                ║
║  ☐ Step 6: Apply Jobs on Upwork (30 min)                   ║
║     → Search: video editing, graphic design                   ║
║                                                                ║
║  ☐ Step 7: Follow Up in 24 Hours (30 min)                  ║
║     → Check responses, reply within 1 hour                   ║
║                                                                ║
║  ─────────────────────────────────────────────────────────  ║
║                                                                ║
║  ⏱️ Total Time: ~2.5 hours                                ║
║  🎯 Target: $500-1000 this week                           ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
""")

def print_quick_links():
    """Print quick links"""
    print_section("🔗 QUICK LINKS")
    
    print("""
┌────────────────────────────────────────────────────────────────────┐
│  📱 FIVERR:      https://www.fiverr.com                           │
│  💼 UPWORK:     https://www.upwork.com                           │
│  🔗 LINKEDIN:    https://linkedin.com                            │
│  📱 WHATSAPP:    https://wa.me/6281337558787                     │
│  📧 EMAIL:       mail.google.com                                  │
└────────────────────────────────────────────────────────────────────┘
""")

# =====================
# MAIN EXECUTION
# =====================
def main():
    print_header()
    
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"👑 CEO: {CONFIG['ceo_alias']}")
    print(f"🏦 Bank: {CONFIG['bank']} {CONFIG['bank_account']}")
    print(f"🎯 Weekly Target: ${CONFIG['target_weekly']}")
    print(f"🎯 Monthly Target: ${CONFIG['target_monthly']}")
    
    # Execute all
    execute_outreach()
    execute_email_outreach()
    generate_fiverr_gigs()
    generate_upwork_profile()
    print_tracking_sheet()
    print_revenue_target()
    print_action_plan()
    print_quick_links()
    
    print_section("✅ EXECUTION SUMMARY")
    print(f"""
╔════════════════════════════════════════════════════════════════╗
║                    ✅ READY TO EXECUTE                       ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  ✅ WhatsApp Messages: 2 ready                               ║
║  ✅ Email Templates: 2 ready                                ║
║  ✅ Fiverr Gigs: 3 ready                                    ║
║  ✅ Upwork Profile: Ready                                    ║
║  ✅ Tracking Sheet: Ready                                   ║
║                                                                ║
║  📋 NEXT ACTIONS:                                            ║
║     1. Go to Fiverr.com → Create Account → Create Gigs      ║
║     2. Go to Upwork.com → Create Account → Apply Jobs       ║
║     3. Send WhatsApp messages using templates above          ║
║     4. Send emails using templates above                      ║
║     5. Follow up in 24 hours                                ║
║                                                                ║
║  💰 TARGET: $500-1000 this week                            ║
║     → CEO Share (60%): $300-600 to BCA                     ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
    """)
    
    print("\n🔥 TIADA KATA TERLAMBAT! HARI INI KITA JUAL! 🔥\n")

if __name__ == "__main__":
    main()
