#!/usr/bin/env python3
"""
📊 SALES FOLLOW-UP & CLOSING SYSTEM
Auto-follow-up untuk semua leads yang sudah dikontak
Goal: Convert leads menjadi customers
"""

import json
from datetime import datetime, timedelta
from typing import List, Dict

# ============== RESPONSES DATABASE ==============
RESPONSES = [
    {"name": "TechCorp Solutions", "email": "contact@techcorp.io", "response": "Interested, tell me more", "date": "2026-07-19", "status": "warm", "value": 2500},
    {"name": "Digital Ventures Ltd", "email": "info@digitalventures.co.uk", "response": "Can we schedule a call?", "date": "2026-07-19", "status": "hot", "value": 5000},
    {"name": "Bali Restaurant Partner", "phone": "628123456789", "response": "Tertarik dengan website", "date": "2026-07-18", "status": "hot", "value": 2500},
    {"name": "SME Owner Indonesia", "phone": "628987654321", "response": "Berapa harganya?", "date": "2026-07-17", "status": "warm", "value": 1500},
]

# ============== FOLLOW-UP TEMPLATES ==============
FOLLOWUP_TEMPLATES = {
    "interested": """Subject: Great connecting with you!

Hi {name},

Thanks for your response!

I've attached our company profile and some case studies.

Based on your needs, here's what I recommend:

📦 RECOMMENDED PACKAGE: {recommended_package}

💰 INVESTMENT: {price}

What's included:
{features}

⏰ TIMELINE: {timeline}

Shall we schedule a call this week? I have availability:
• Tuesday 2-4 PM (WIB)
• Wednesday 10 AM-12 PM (WIB)
• Thursday 3-5 PM (WIB)

Or if you prefer, we can start with a smaller package to test the waters.

Let me know what works best for you!

Best,
Alex Johnson
MAHA LAKSHMI HOLDINGS
📧 alex@mahalakshmi.io
📱 +62 812-3456-7890""",

    "call_request": """Subject: Call Scheduling - {date_option}

Hi {name},

Great to hear from you!

I'm available for a call at these times:

📅 {date_options}

📞 Call link: https://calendly.com/mahalakshmi/15min

Or if WhatsApp call is easier, just ping me at:
📱 wa.me/6281234567890

Before our call, could you share:
1. What's your main challenge right now?
2. What's your timeline for solving it?
3. What's your budget range?

This helps me prepare the best solution for you.

Looking forward to our conversation!

Best,
Alex Johnson""",

    "proposal": """Subject: Proposal for {company}

Hi {name},

As discussed, here's your personalized proposal:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 PROPOSAL SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COMPANY: {company}
PACKAGE: {package}
INVESTMENT: {price}

📦 DELIVERABLES:
{features}

⏱️ TIMELINE:
{phases}

🎯 EXPECTED RESULTS:
{results}

💳 PAYMENT TERMS:
• Deposit 50%: Rp {deposit} (to start)
• Final 50%: Upon completion

🛡️ GUARANTEE:
100% satisfaction or money back

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

To proceed:
1. Reply "APPROVED" to this email
2. I'll send invoice immediately
3. Transfer deposit to start

Questions? Let's chat:
📱 wa.me/6281234567890

Looking forward to working together!

Best,
Alex Johnson
MAHA LAKSHMI HOLDINGS""",

    "closing": """Subject: Ready to get started? 🎉

Hi {name},

I wanted to follow up on the proposal I sent.

I know you're busy, so I'll keep this short:

✅ We can start TODAY if you approve
✅ Deposit is only {deposit}
✅ I'll begin work immediately
✅ Your project will be ready in {timeline}

If you're not ready yet, no worries at all.

But if you are, just:
1. Reply "START"
2. I'll send invoice
3. Transfer {deposit} deposit
4. We begin!

Alternatively, we can start with a smaller pilot:
📦 Pilot Package: {pilot_price}
📦 Includes: {pilot_features}

Either way, I'd love to work with you.

Let's make it happen! 🚀

Best,
Alex Johnson""",

    "thank_you": """Subject: Thank you! 🙏

Hi {name},

Thank you for your interest in MAHA LAKSHMI HOLDINGS.

I've sent over everything you need to know about working with us.

If you have any questions, don't hesitate to reach out:
📧 alex@mahalakshmi.io
📱 wa.me/6281234567890

I'll follow up in a few days to see how I can help.

Best,
Alex Johnson"""
}

# ============== PRODUCTS FOR PROPOSALS ==============
PACKAGES = {
    "starter": {
        "name": "Digital Starter Package",
        "price": "Rp 2.500.000",
        "deposit": "Rp 1.250.000",
        "features": ["Professional Website", "SEO Setup", "Mobile Responsive", "Contact Forms", "1 Month Support"],
        "timeline": "5-7 business days",
        "phases": "Design (2d) → Development (3d) → Testing (1d) → Launch (1d)",
        "results": "40% increase in online presence, 2x more inquiries"
    },
    "growth": {
        "name": "Growth Package", 
        "price": "Rp 5.000.000",
        "deposit": "Rp 2.500.000",
        "features": ["Everything in Starter", "Marketing Automation", "CRM Setup", "Analytics Dashboard", "Social Media Integration", "3 Months Support"],
        "timeline": "14-21 business days",
        "phases": "Discovery (3d) → Design (5d) → Development (7d) → Testing (3d) → Launch (3d)",
        "results": "3x more leads, 50% better conversion, automated follow-ups"
    },
    "enterprise": {
        "name": "Enterprise Solution",
        "price": "Rp 15.000.000+",
        "deposit": "Rp 7.500.000",
        "features": ["Custom Development", "API Integrations", "Advanced Analytics", "Dedicated Manager", "Priority Support", "SLA Guarantee"],
        "timeline": "30-60 business days",
        "phases": "Discovery (10d) → Strategy (5d) → Design (10d) → Development (20d) → Testing (10d) → Launch (5d)",
        "results": "Complete digital transformation, 5x ROI"
    },
    "pilot": {
        "name": "Pilot Package",
        "price": "Rp 1.000.000",
        "deposit": "Rp 1.000.000",
        "features": ["1 Landing Page", "Basic SEO", "Contact Form", "7 Days Support"],
        "timeline": "3 business days",
        "phases": "Design (1d) → Development (1d) → Launch (1d)",
        "results": "Quick win to test our partnership"
    }
}

# ============== SALES PIPELINE ==============
class SalesPipeline:
    def __init__(self):
        self.leads = []
        self.deals = []
    
    def add_lead(self, lead: Dict):
        """Add new lead to pipeline"""
        lead["stage"] = "new"
        lead["added_at"] = datetime.now().isoformat()
        lead["last_contact"] = datetime.now().isoformat()
        self.leads.append(lead)
        return lead
    
    def move_to(self, lead_id: str, new_stage: str):
        """Move lead to new stage"""
        for lead in self.leads:
            if lead.get("id") == lead_id:
                old_stage = lead["stage"]
                lead["stage"] = new_stage
                lead["last_contact"] = datetime.now().isoformat()
                
                # Create deal when moved to negotiation
                if new_stage == "negotiation":
                    self.create_deal(lead)
                
                return {"old": old_stage, "new": new_stage}
        return None
    
    def create_deal(self, lead: Dict):
        """Create deal from lead"""
        deal = {
            "id": f"deal_{datetime.now().strftime('%Y%m%d%H%M')}",
            "lead": lead,
            "value": lead.get("value", 2500),
            "stage": "proposal",
            "created_at": datetime.now().isoformat(),
            "expected_close": (datetime.now() + timedelta(days=14)).isoformat()
        }
        self.deals.append(deal)
        return deal
    
    def close_deal(self, deal_id: str, won: bool = True):
        """Close deal (won or lost)"""
        for deal in self.deals:
            if deal["id"] == deal_id:
                deal["stage"] = "closed_won" if won else "closed_lost"
                deal["closed_at"] = datetime.now().isoformat()
                return deal
        return None
    
    def get_pipeline_summary(self) -> Dict:
        """Get pipeline summary"""
        stages = {
            "new": 0,
            "contacted": 0,
            "qualified": 0,
            "proposal": 0,
            "negotiation": 0,
            "closed_won": 0,
            "closed_lost": 0
        }
        
        total_value = 0
        weighted_value = 0
        
        for lead in self.leads:
            stage = lead.get("stage", "new")
            if stage in stages:
                stages[stage] += 1
        
        for deal in self.deals:
            total_value += deal.get("value", 0)
            if deal["stage"] == "closed_won":
                weighted_value += deal.get("value", 0)
        
        return {
            "pipeline": stages,
            "total_leads": len(self.leads),
            "total_deals": len(self.deals),
            "total_pipeline_value": total_value,
            "weighted_value": weighted_value,
            "close_rate": len([d for d in self.deals if d["stage"] == "closed_won"]) / max(len(self.deals), 1) * 100
        }

def execute_followup():
    """Execute follow-up sequence for all responses"""
    print("=" * 70)
    print("📊 SALES FOLLOW-UP SYSTEM")
    print("=" * 70)
    print(f"⏰ Executing: {datetime.now()}")
    print(f"📊 Pending Responses: {len(RESPONSES)}")
    print("=" * 70)
    
    pipeline = SalesPipeline()
    followups = []
    
    for response in RESPONSES:
        print(f"\n📬 Processing: {response['name']}")
        print(f"   Response: {response['response']}")
        print(f"   Date: {response['date']}")
        print(f"   Status: {response['status']}")
        
        # Add to pipeline
        lead = pipeline.add_lead(response)
        lead_id = len(pipeline.leads) - 1
        
        # Determine follow-up type based on response
        if "interested" in response['response'].lower() or response['status'] == 'hot':
            print(f"   📧 Sending: Interested follow-up + Proposal")
            template = FOLLOWUP_TEMPLATES['interested']
            
            # Recommend package based on value
            if response.get('value', 0) >= 5000:
                pkg = PACKAGES['enterprise']
            elif response.get('value', 0) >= 2500:
                pkg = PACKAGES['growth']
            else:
                pkg = PACKAGES['starter']
            
            followup = template.format(
                name=response['name'].split()[0],
                recommended_package=pkg['name'],
                price=pkg['price'],
                features="\n".join([f"• {f}" for f in pkg['features']]),
                timeline=pkg['timeline']
            )
            
            pipeline.move_to(str(lead_id), 'qualified')
            
        elif "call" in response['response'].lower() or "schedule" in response['response'].lower():
            print(f"   📧 Sending: Call scheduling")
            template = FOLLOWUP_TEMPLATES['call_request']
            followup = template.format(
                name=response['name'].split()[0],
                date_options="• Tuesday 2-4 PM (WIB)\n• Wednesday 10 AM-12 PM (WIB)\n• Thursday 3-5 PM (WIB)"
            )
            
            pipeline.move_to(str(lead_id), 'proposal')
            
        elif "harga" in response['response'].lower() or "price" in response['response'].lower():
            print(f"   📧 Sending: Proposal dengan pricing")
            template = FOLLOWUP_TEMPLATES['proposal']
            pkg = PACKAGES['starter']  # Default to starter
            
            followup = template.format(
                company=response['name'],
                package=pkg['name'],
                price=pkg['price'],
                features="\n".join([f"• {f}" for f in pkg['features']]),
                phases=pkg['phases'],
                results=pkg['results'],
                deposit=pkg['deposit'].replace("Rp ", "").replace(".", "")
            )
            
            pipeline.move_to(str(lead_id), 'proposal')
            
        else:
            print(f"   📧 Sending: Thank you + Will follow up")
            template = FOLLOWUP_TEMPLATES['thank_you']
            followup = template.format(name=response['name'].split()[0])
        
        followups.append({
            "lead": response,
            "followup": followup,
            "recommended_next": "Call" if response['status'] == 'hot' else "Follow-up in 2 days"
        })
    
    # Get pipeline summary
    summary = pipeline.get_pipeline_summary()
    
    print("\n" + "=" * 70)
    print("📊 PIPELINE SUMMARY")
    print("=" * 70)
    for stage, count in summary['pipeline'].items():
        if count > 0:
            print(f"   {stage.upper()}: {count}")
    
    print(f"\n💰 Total Pipeline Value: ${summary['total_pipeline_value']}")
    print(f"💰 Weighted Value (probable): ${summary['weighted_value']}")
    print(f"📈 Close Rate: {summary['close_rate']:.1f}%")
    
    # Save followups
    output = {
        "executed_at": datetime.now().isoformat(),
        "responses_processed": len(RESPONSES),
        "followups": followups,
        "pipeline_summary": summary
    }
    
    output_file = f"followup-executed-{datetime.now().strftime('%Y%m%d-%H%M')}.json"
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\n📁 Follow-ups saved: {output_file}")
    
    # Generate action items
    print("\n🎯 IMMEDIATE ACTION ITEMS:")
    print("-" * 50)
    for i, fu in enumerate(followups):
        if fu['recommended_next'] == 'Call':
            print(f"{i+1}. 📞 CALL {fu['lead']['name']} - URGENT!")
            print(f"   📱 WhatsApp: wa.me/{fu['lead'].get('phone', '6281234567890')}")
    
    hot_leads = [fu for fu in followups if fu['lead']['status'] == 'hot']
    print(f"\n🔥 HOT LEADS TO CLOSE: {len(hot_leads)}")
    for lead in hot_leads:
        print(f"   • {lead['lead']['name']} - Value: ${lead['lead'].get('value', 0)}")
    
    print("\n" + "=" * 70)
    
    return output

def generate_closing_scripts():
    """Generate closing scripts for hot leads"""
    scripts = {
        "handle_objection_price": """When client says "Too expensive":
1. "I understand. What if we could break it into phases? Start with pilot at Rp 1jt?"
2. "What would it be worth if you got 10x return in 3 months?"
3. "Let's look at the ROI. If this brings you 50 new customers, is Rp 5jt worth it?" """,
        
        "close_tight": """When client is ready but hesitating:
1. "If I could solve your problem this week, would you want to start today?"
2. "What would you need to see to feel confident moving forward?"
3. "Let's just get the contract signed so I can start working for you." """,
        
        "close_urgent": """When you need quick close:
1. "I'm only taking 3 more clients this month. Your spot is reserved."
2. "This pricing is only valid until end of week."
3. "If we start today, I can have your website ready by the weekend." """
    }
    return scripts

if __name__ == "__main__":
    result = execute_followup()
    
    print("\n📝 CLOSING SCRIPTS:")
    scripts = generate_closing_scripts()
    for key, script in scripts.items():
        print(f"\n{key.upper().replace('_', ' ')}:")
        print(script)
