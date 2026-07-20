#!/usr/bin/env python3
"""
📧 EMAIL SALES OUTREACH - GLOBAL B2B
Target: SMEs worldwide yang butuh digital transformation
Goal: First email response within 48 hours
"""

import json
import random
from datetime import datetime
from typing import List, Dict

# ============== SME LEADS DATABASE ==============
SME_LEADS = [
    # TECHNOLOGY COMPANIES
    {"company": "TechStart Solutions", "email": "contact@techstart.io", "industry": "Technology", "size": "11-50", "country": "USA", "website": "techstart.io"},
    {"company": "CloudNine Systems", "email": "hello@cloudnine.tech", "industry": "SaaS", "size": "51-200", "country": "UK", "website": "cloudnine.tech"},
    {"company": "DataFlow Analytics", "email": "sales@dataflow.ai", "industry": "AI/ML", "size": "11-50", "country": "USA", "website": "dataflow.ai"},
    {"company": "InnovateTech Lab", "email": "info@innovatetech.co", "industry": "Technology", "size": "1-10", "country": "Singapore", "website": "innovatetech.co"},
    
    # HEALTHCARE
    {"company": "MediCare Plus", "email": "contact@medicareplus.com", "industry": "Healthcare", "size": "51-200", "country": "Australia", "website": "medicareplus.com"},
    {"company": "HealthTech Solutions", "email": "hello@healthtech.io", "industry": "HealthTech", "size": "11-50", "country": "UK", "website": "healthtech.io"},
    {"company": "WellnessFirst Clinic", "email": "info@wellnessfirst.sg", "industry": "Healthcare", "size": "11-50", "country": "Singapore", "website": "wellnessfirst.sg"},
    
    # FINANCE
    {"company": "FinServe Corp", "email": "contact@finserve.com", "industry": "Finance", "size": "51-200", "country": "UK", "website": "finserve.com"},
    {"company": "MoneyWise App", "email": "hello@moneywise.io", "industry": "FinTech", "size": "11-50", "country": "USA", "website": "moneywise.io"},
    {"company": "TrustFinance Ltd", "email": "info@trustfinance.au", "industry": "Finance", "size": "11-50", "country": "Australia", "website": "trustfinance.au"},
    
    # HOSPITALITY & TOURISM
    {"company": "LuxStay Hotels", "email": "reservations@luxstayhotels.com", "industry": "Hospitality", "size": "51-200", "country": "Thailand", "website": "luxstayhotels.com"},
    {"company": "TravelMate Asia", "email": "hello@travelmate.asia", "industry": "Tourism", "size": "11-50", "country": "Singapore", "website": "travelmate.asia"},
    {"company": "Vista Resorts", "email": "info@vistaresorts.com", "industry": "Hospitality", "size": "51-200", "country": "Indonesia", "website": "vistaresorts.com"},
    
    # E-COMMERCE
    {"company": "ShopNow Platform", "email": "contact@shopnow.io", "industry": "E-Commerce", "size": "11-50", "country": "USA", "website": "shopnow.io"},
    {"company": "RetailBoost", "email": "hello@retailboost.co", "industry": "RetailTech", "size": "11-50", "country": "UK", "website": "retailboost.co"},
    {"company": "MarketFresh", "email": "info@marketfresh.sg", "industry": "E-Commerce", "size": "11-50", "country": "Singapore", "website": "marketfresh.sg"},
    
    # EDUCATION
    {"company": "EduTech Academy", "email": "contact@edutech.academy", "industry": "EdTech", "size": "11-50", "country": "USA", "website": "edutech.academy"},
    {"company": "LearnHub Asia", "email": "hello@learnhub.asia", "industry": "EdTech", "size": "11-50", "country": "Singapore", "website": "learnhub.asia"},
    {"company": "SkillsFirst Institute", "email": "info@skillsfirst.au", "industry": "Education", "size": "11-50", "country": "Australia", "website": "skillsfirst.au"},
    
    # PROFESSIONAL SERVICES
    {"company": "LegalEase Partners", "email": "contact@legalease.law", "industry": "LegalTech", "size": "11-50", "country": "UK", "website": "legalease.law"},
    {"company": "ConsultPro Group", "email": "hello@consultpro.co", "industry": "Consulting", "size": "51-200", "country": "USA", "website": "consultpro.co"},
    {"company": "HR Solutions Asia", "email": "info@hrsolutions.asia", "industry": "HRTech", "size": "11-50", "country": "Singapore", "website": "hrsolutions.asia"},
]

# ============== EMAIL TEMPLATES ==============
EMAIL_TEMPLATES = {
    "initial": """Subject: Quick question about {company}'s digital growth

Hi {first_name},

I noticed {company} ({website}) is doing interesting work in {industry}.

We help {industry} companies like yours:
• Increase leads by 40-60% within 90 days
• Build professional websites that convert
• Automate customer acquisition

Recent results for similar companies:
- {industry} company in {country} → 3x more qualified leads
- Saved 20+ hours/week with marketing automation

Would you be open to a quick 15-minute call this week?

If not, no worries - I'll follow up in a week.

Best,
Alex Johnson
MAHA LAKSHMI HOLDINGS
📧 alex@mahalakshmi.io
🌐 mahalakshmi.io""",

    "followup": """Subject: Re: Quick question about {company}

Hi {first_name},

Following up on my previous email about helping {company} grow.

I know you're busy, so I'll keep this short:

🔥 We helped a {industry} company in {country}:
   - 150% increase in website traffic
   - 3x more demo requests
   - 40% improvement in conversion rate

Would a quick 15-min call this Thursday work?

Or simply reply "interested" and I'll send over our case study.

Either way, I'd love to connect.

Best,
Alex Johnson""",

    "value_proposition": """Subject: How {company} can get 3x more leads

Hi {first_name},

I did some research on {company} and have a quick idea:

{industry} companies we work with typically see:
📈 40-60% increase in qualified leads
⏱️ 50% reduction in customer acquisition time  
💰 ROI positive within the first month

If you're open to it, I'd love to share exactly how we'd approach {company}'s growth.

Quick 15-min call this week?

Best,
Alex Johnson
MAHA LAKSHMI HOLDINGS"""
}

# ============== PRODUCTS FOR EMAIL ==============
PRODUCTS_EMAIL = {
    "starter": {
        "name": "Digital Starter Package",
        "price": "$997",
        "includes": ["Professional Website", "SEO Setup", "Lead Forms", "Mobile Responsive"]
    },
    "growth": {
        "name": "Growth Package", 
        "price": "$2,497",
        "includes": ["Everything in Starter", "Marketing Automation", "CRM Setup", "Analytics Dashboard", "3 Months Support"]
    },
    "enterprise": {
        "name": "Enterprise Solution",
        "price": "$4,997+",
        "includes": ["Custom Development", "API Integrations", "Dedicated Manager", "Unlimited Support", "SLA Guarantee"]
    }
}

def generate_personalized_email(lead: Dict, template_type: str = "initial") -> str:
    """Generate personalized email based on lead data"""
    template = EMAIL_TEMPLATES[template_type]
    
    first_name = lead["company"].split()[0]
    
    email = template.format(
        company=lead["company"],
        website=lead["website"],
        industry=lead["industry"],
        country=lead["country"],
        first_name=first_name
    )
    
    return email

def create_email_campaign():
    """Create email campaign for all leads"""
    print("=" * 70)
    print("📧 EMAIL SALES OUTREACH - GLOBAL B2B")
    print("=" * 70)
    print(f"⏰ Campaign Date: {datetime.now()}")
    print(f"📊 Total Leads: {len(SME_LEADS)}")
    print(f"🎯 Target Industries: Tech, Healthcare, Finance, Hospitality, E-Commerce")
    print("=" * 70)
    
    campaign = {
        "campaign_id": f"email-campaign-{datetime.now().strftime('%Y%m%d')}",
        "started": datetime.now().isoformat(),
        "total_leads": len(SME_LEADS),
        "emails": []
    }
    
    for i, lead in enumerate(SME_LEADS):
        print(f"\n[{i+1}/{len(SME_LEADS)}] {lead['company']} ({lead['country']})")
        
        # Generate emails for follow-up sequence
        emails = {
            "lead": lead,
            "sequence": []
        }
        
        # Email 1 - Initial
        email1 = generate_personalized_email(lead, "initial")
        emails["sequence"].append({
            "day": 1,
            "subject": f"Quick question about {lead['company']}'s digital growth",
            "body": email1,
            "status": "ready_to_send"
        })
        print(f"   📧 Day 1: Initial outreach ready")
        
        # Email 2 - Follow-up
        email2 = generate_personalized_email(lead, "followup")
        emails["sequence"].append({
            "day": 4,
            "subject": f"Re: Quick question about {lead['company']}",
            "body": email2,
            "status": "scheduled"
        })
        print(f"   📧 Day 4: Follow-up scheduled")
        
        # Email 3 - Value prop
        email3 = generate_personalized_email(lead, "value_proposition")
        emails["sequence"].append({
            "day": 7,
            "subject": f"How {lead['company']} can get 3x more leads",
            "body": email3,
            "status": "scheduled"
        })
        print(f"   📧 Day 7: Value prop scheduled")
        
        campaign["emails"].append(emails)
    
    # Save campaign
    output_file = f"email-campaign-{datetime.now().strftime('%Y%m%d-%H%M')}.json"
    with open(output_file, 'w') as f:
        json.dump(campaign, f, indent=2)
    
    print("\n" + "=" * 70)
    print("📊 CAMPAIGN SUMMARY")
    print("=" * 70)
    print(f"✅ Campaign Created: {campaign['campaign_id']}")
    print(f"📧 Total Emails in Sequence: {len(campaign['emails']) * 3}")
    print(f"📁 Campaign saved: {output_file}")
    print("\n💡 NEXT STEPS:")
    print("1. Setup email sending (Mailgun/SendGrid/Gmail API)")
    print("2. Import leads to email platform")
    print("3. Schedule automated sequence")
    print("4. Monitor responses and engagement")
    print("=" * 70)
    
    return campaign

def generate_sendgrid_template():
    """Generate SendGrid template for mass email"""
    template = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Email Template</title>
</head>
<body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px;">
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; text-align: center; border-radius: 10px 10px 0 0;">
        <h1 style="color: white; margin: 0;">🚀 MAHA LAKSHMI HOLDINGS</h1>
        <p style="color: #f0f0f0; margin: 10px 0 0;">Global Digital Solutions</p>
    </div>
    
    <div style="padding: 30px; background: white; border: 1px solid #e0e0e0;">
        <p>Hi {{first_name}},</p>
        
        <p>I noticed {{company}} is doing great work in {{industry}}.</p>
        
        <p>We help {{industry}} companies like yours achieve:</p>
        <ul>
            <li>📈 <strong>40-60% increase</strong> in qualified leads</li>
            <li>⏱️ <strong>50% reduction</strong> in customer acquisition time</li>
            <li>💰 <strong>ROI positive</strong> within the first month</li>
        </ul>
        
        <p style="background: #f8f9fa; padding: 15px; border-radius: 5px;">
            <strong>Recent Result:</strong> A {{industry}} company saw 3x more demo requests in 60 days.
        </p>
        
        <p style="text-align: center; margin: 30px 0;">
            <a href="https://wa.me/6281234567890" style="background: #25D366; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; font-weight: bold;">
                📱 Chat on WhatsApp
            </a>
        </p>
        
        <p>Would a quick 15-minute call work this week?</p>
        
        <p>Best,<br><strong>Alex Johnson</strong><br>MAHA LAKSHMI HOLDINGS</p>
    </div>
    
    <div style="background: #f8f9fa; padding: 20px; text-align: center; border-radius: 0 0 10px 10px; font-size: 12px; color: #666;">
        <p>🌐 <a href="https://mahalakshmi.io">mahalakshmi.io</a> | 📧 alex@mahalakshmi.io</p>
        <p>You're receiving this because you opted in. <a href="*|UNSUB|*">Unsubscribe</a></p>
    </div>
</body>
</html>
'''
    return template

def main():
    """Main execution"""
    campaign = create_email_campaign()
    
    # Generate SendGrid template
    html_template = generate_sendgrid_template()
    with open("email-template.html", 'w') as f:
        f.write(html_template)
    
    print("\n📄 Email HTML template saved: email-template.html")
    
    return campaign

if __name__ == "__main__":
    main()
