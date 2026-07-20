#!/usr/bin/env python3
"""
🤖 AI FOLLOW-UP AGENT
Automatically follows up with leads that haven't responded

Schedule:
- Day 3: First follow-up
- Day 7: Second follow-up  
- Day 14: Final follow-up

Author: GAURANGA AI System
Date: 2026-07-20
"""

import json
import csv
from datetime import datetime, timedelta, timezone
from pathlib import Path

# =======================
# CONFIGURATION
# =======================
LEADS_FILE = 'archives/LEADS-DATABASE.json'
OUTPUT_DIR = 'docs/reports'
LOG_FILE = 'followup-log.txt'

# Follow-up messages by day
MESSAGES = {
    'day3': {
        'whatsapp': """🏝️ Halo {name}! 👋

Sekadar follow up dari pesan kami sebelumnya...

Apakah Anda sudah sempat mempertimbangkan partnership dengan kami?

🌟 BENEFIT PARTNERSHIP:
✅ Commission 15% per booking
✅ Tidak ada biaya upfront
✅ Kami handle semua administrasi
✅ Marketing support included

📊 POTENTIAL REVENUE:
Contoh: 10 tamu booking tour/bulan
• Rata-rata booking: Rp 1.000.000
• Commission Anda: 15% = Rp 150.000/booking
• Potensi bulanan: Rp 1.500.000

Ada pertanyaan? Mari diskusi lebih lanjut!
📱 wa.me/6281337558787

--
Bali Travel Platform""",
        'email_subject': 'Re: Partnership Opportunity - Quick Follow Up',
        'email_body': """Halo {name},

Sekadar follow up dari pesan kami sebelumnya...

Apakah Anda sudah sempat mempertimbangkan partnership dengan kami?

🌟 BENEFIT PARTNERSHIP:
• Commission 15% per booking
• Tidak ada biaya upfront
• Kami handle semua administrasi
• Marketing support included

📊 POTENTIAL REVENUE:
Contoh: 10 tamu booking tour/bulan
• Rata-rata booking: Rp 1.000.000
• Commission Anda: 15% = Rp 150.000/booking
• Potensi bulanan: Rp 1.500.000

Ada pertanyaan? Mari diskusi lebih lanjut!

Salam,
i Made Purna Ananda
CEO, MAHA LAKSHMI Digital
WhatsApp: wa.me/6281337558787"""
    },
    'day7': {
        'whatsapp': """👋 Halo {name}!

Follow up lagi nih...

Partnership 15% commission masih tersedia lho! 🎉

Kami sudah banyak dapat response positif dari partner lain.

❓ PERTANYAAN CEPAT:
Apakah ini sesuatu yang menarik untuk {company}?

Kalau tertarik, kita bisa scheduling call 15 menit.
Kalau tidak, tidak perlu merasa bersalah - hanya ingin menawarkan kesempatan ini 😊

📱 wa.me/6281337558787

--
Bali Travel Platform""",
        'email_subject': 'Re: Partnership Opportunity - Following Up Again',
        'email_body': """Halo {name},

Follow up lagi nih...

Partnership 15% commission masih tersedia lho!

Kami sudah banyak dapat response positif dari partner lain.

❓ PERTANYAAN CEPAT:
Apakah ini sesuatu yang menarik untuk {company}?

Kalau tertarik, kita bisa scheduling call 15 menit.
Kalau tidak, tidak perlu merasa bersalah - hanya ingin menawarkan kesempatan ini.

Salam,
i Made Purna Ananda
CEO, MAHA LAKSHMI Digital
WhatsApp: wa.me/6281337558787"""
    },
    'day14': {
        'whatsapp': """⚠️ {name} - Follow Up Terakhir

Ini adalah pesan follow up TERAKHIR dari kami.

🌟 SPECIAL OFFER (Hanya minggu ini!):
✅ Commission 15%
✅ Biaya setup di-WAIVE
✅ Priority booking slots
✅ Dedicated account manager

Setelah ini, kami akan menutup list outreach kami.

Apakah Anda tertarik? Ini kesempatan terakhir!

📱 wa.me/6281337558787

Terima kasih atas waktunya! 🙏

--
Bali Travel Platform""",
        'email_subject': 'Final Follow-Up - Special Offer This Week Only',
        'email_body': """Halo {name},

Ini adalah pesan follow up TERAKHIR dari kami.

🌟 SPECIAL OFFER (Hanya minggu ini!):
• Commission 15%
• Biaya setup di-WAIVE
• Priority booking slots
• Dedicated account manager

Setelah ini, kami akan menutup list outreach kami.

Apakah Anda tertarik? Ini kesempatan terakhir!

Terima kasih atas waktunya!

Salam,
i Made Purna Ananda
CEO, MAHA LAKSHMI Digital
WhatsApp: wa.me/6281337558787"""
    }
}

# Category-specific messages
CATEGORY_MESSAGES = {
    'bali-travel': {
        'day3_whatsapp': """🏝️ Halo {name}! 👋

Follow up partnership tour Bali!

🌟 BENEFIT:
✅ 15% commission per booking
✅ No upfront cost
✅ We handle everything

📊 Contoh: 10 guests x Rp 1M = Rp 150.000 commission/bulan

Mau tahu lebih detail?
📱 wa.me/6281337558787

--
Bali Travel Platform""",
        'day7_whatsapp': """👋 Halo {name}!

Partnership tour kami masih open!

🌟 15% commission
✅ Passive income
✅ No risk

Pertanyaan: Apakah ini cocok untuk {company}?

📱 wa.me/6281337558787

--
Bali Travel Platform""",
        'day14_whatsapp': """⚠️ {name} - LAST FOLLOW UP

🌟 SPECIAL OFFER (Minggu ini SAJA!):
✅ 15% commission
✅ Setup fee WAIVED
✅ Priority slots

After this, we close the list.

Still interested?
📱 wa.me/6281337558787

--
Bali Travel Platform"""
    },
    'gianyar-tech': {
        'day3_whatsapp': """💻 Halo {name}! 👋

Follow up - Gianyar Tech Solutions!

Kami bantu bisnis AndaGo digital:
🌟 SERVICES:
• Website Development
• Digital Marketing
• AI Solutions

💰 PRICING:
• Landing Page: dari Rp 2.000.000
• Company Website: dari Rp 5.000.000
• E-commerce: dari Rp 10.000.000

Mau konsultasi gratis?
📱 wa.me/6281337558787

--
Gianyar Tech Solutions""",
        'day7_whatsapp': """👋 Halo {name}!

Gianyar Tech Solutions di sini!

💻 SERVICES:
• Website Development
• Digital Marketing  
• AI Solutions

Special price untuk early adopters!

📱 wa.me/6281337558787

--
Gianyar Tech Solutions""",
        'day14_whatsapp': """⚠️ {name} - FINAL FOLLOW UP

💻 OFFER (This week only!):
✅ Discount 20%
✅ Free consultation
✅ Priority support

After this, we close the list.
📱 wa.me/6281337558787

--
Gianyar Tech Solutions"""
    }
}

# =======================
# FUNCTIONS
# =======================

def get_current_date():
    """Get current date in Asia/Jakarta timezone"""
    return datetime.now(timezone(timedelta(hours=7)))

def load_leads():
    """Load leads from database"""
    with open(LEADS_FILE, 'r') as f:
        return json.load(f)

def save_leads(data):
    """Save leads to database"""
    with open(LEADS_FILE, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def calculate_followup_day(contacted_at, days_from_contact):
    """Calculate follow-up date based on contact date"""
    contacted = datetime.fromisoformat(contacted_at)
    followup = contacted + timedelta(days=days_from_contact)
    return followup.replace(hour=10, minute=0, second=0, microsecond=0)

def get_followup_type(contacted_at):
    """Determine which follow-up type is needed"""
    contacted = datetime.fromisoformat(contacted_at)
    today = get_current_date()
    days_passed = (today - contacted).days
    
    if days_passed >= 14:
        return 'day14'
    elif days_passed >= 7:
        return 'day7'
    elif days_passed >= 3:
        return 'day3'
    else:
        return None

def generate_followup_messages(lead, followup_type):
    """Generate personalized follow-up messages for a lead"""
    name = lead.get('name', 'there').split()[0]
    company = lead.get('company', 'your company')
    category = lead.get('category', 'bali-travel')
    
    # Get category-specific messages or default
    cat_msgs = CATEGORY_MESSAGES.get(category, CATEGORY_MESSAGES['bali-travel'])
    default_msgs = MESSAGES.get(followup_type, MESSAGES['day3'])
    
    whatsapp = cat_msgs.get(f'{followup_type}_whatsapp', default_msgs['whatsapp'])
    email_subject = default_msgs['email_subject']
    email_body = default_msgs['email_body']
    
    # Personalize messages
    whatsapp_msg = whatsapp.format(name=name, company=company)
    email_subject_msg = email_subject.format(name=name)
    email_body_msg = email_body.format(name=name, company=company)
    
    return {
        'whatsapp': whatsapp_msg,
        'email_subject': email_subject_msg,
        'email_body': email_body_msg
    }

def update_lead_followup(lead, followup_type):
    """Update lead with follow-up information"""
    now = get_current_date()
    
    # Update last_followup
    lead['last_followup'] = now.isoformat()
    
    # Calculate next follow-up
    if followup_type == 'day3':
        lead['next_followup'] = (now + timedelta(days=4)).isoformat()
        lead['followup_sequence'] = 2
    elif followup_type == 'day7':
        lead['next_followup'] = (now + timedelta(days=7)).isoformat()
        lead['followup_sequence'] = 3
    else:  # day14
        lead['next_followup'] = None  # Final follow-up
        lead['followup_sequence'] = 4
        lead['status'] = 'followup_complete'
    
    return lead

def process_followups():
    """Process all leads that need follow-up"""
    data = load_leads()
    leads = data.get('leads', [])
    
    today = get_current_date()
    results = {
        'processed': 0,
        'day3': [],
        'day7': [],
        'day14': [],
        'not_yet_due': [],
        'already_replied': []
    }
    
    followups_to_send = []
    
    for lead in leads:
        contacted_at = lead.get('contacted_at')
        replied_at = lead.get('replied_at')
        next_followup = lead.get('next_followup')
        
        # Skip if already replied
        if replied_at:
            results['already_replied'].append(lead)
            continue
        
        # Calculate days since contact
        if contacted_at:
            contacted = datetime.fromisoformat(contacted_at)
            days_passed = (today - contacted).days
            
            followup_type = get_followup_type(contacted_at)
            
            if followup_type:
                # Generate messages
                messages = generate_followup_messages(lead, followup_type)
                
                followup_data = {
                    'lead': lead,
                    'type': followup_type,
                    'days_passed': days_passed,
                    'messages': messages
                }
                
                followups_to_send.append(followup_data)
                results[followup_type].append(lead)
                results['processed'] += 1
                
                # Update lead
                update_lead_followup(lead, followup_type)
            else:
                results['not_yet_due'].append({
                    'lead': lead,
                    'days_passed': days_passed
                })
        else:
            results['not_yet_due'].append({
                'lead': lead,
                'days_passed': 0,
                'note': 'No contact date'
            })
    
    # Save updated leads
    data['leads'] = leads
    data['last_followup_run'] = today.isoformat()
    save_leads(data)
    
    return results, followups_to_send

def generate_followup_report(results, followups_to_send):
    """Generate follow-up report"""
    today = get_current_date()
    
    report = f"""# 📊 FOLLOW-UP AGENT REPORT

**Generated:** {today.strftime('%Y-%m-%d %H:%M:%S')} WIB  
**Agent:** GAURANGA AI Follow-up Agent

---

## 📋 EXECUTIVE SUMMARY

| Metric | Value |
|--------|-------|
| **Total Leads Processed** | {results['processed']} |
| **Day 3 Follow-ups** | {len(results['day3'])} |
| **Day 7 Follow-ups** | {len(results['day7'])} |
| **Day 14 Follow-ups** | {len(results['day14'])} |
| **Already Replied** | {len(results['already_replied'])} |
| **Not Yet Due** | {len(results['not_yet_due'])} |

---

## 📧 FOLLOW-UPS TO SEND

"""
    
    for i, fu in enumerate(followups_to_send, 1):
        lead = fu['lead']
        ftype = fu['type']
        days = fu['days_passed']
        msgs = fu['messages']
        
        report += f"""### {i}. {lead['name']}

| Field | Value |
|-------|-------|
| **ID** | {lead['id']} |
| **Category** | {lead.get('category', 'N/A')} |
| **Follow-up Type** | {ftype.upper()} (Day {days}) |
| **Company** | {lead.get('company', 'N/A')} |
| **Email** | {lead.get('email', 'N/A')} |
| **WhatsApp** | wa.me/{lead.get('whatsapp', 'N/A')} |

#### WhatsApp Message:
```
{msgs['whatsapp']}
```

#### Email:
- **Subject:** {msgs['email_subject']}
- **Body:** (See email template)

---

"""
    
    # Summary by category
    report += f"""## 📊 FOLLOW-UPS BY CATEGORY

| Category | Day 3 | Day 7 | Day 14 | Total |
|----------|-------|-------|--------|-------|
"""
    
    categories = {}
    for fu in followups_to_send:
        cat = fu['lead'].get('category', 'unknown')
        if cat not in categories:
            categories[cat] = {'day3': 0, 'day7': 0, 'day14': 0}
        categories[cat][fu['type']] += 1
    
    for cat, counts in categories.items():
        report += f"| {cat} | {counts['day3']} | {counts['day7']} | {counts['day14']} | {sum(counts.values())} |\n"
    
    report += f"""
---

## 🚀 NEXT ACTIONS

1. **Send WhatsApp messages** to all leads in the list above
2. **Send emails** with personalized templates
3. **Wait for responses** and update lead status
4. **Schedule Day 7 follow-ups** for leads that don't respond

---

## 📅 FOLLOW-UP SCHEDULE

| Day | Date | Leads |
|-----|------|-------|
| Day 3 | {today.strftime('%Y-%m-%d')} | {len(results['day3'])} leads |
| Day 7 | {(today + timedelta(days=4)).strftime('%Y-%m-%d')} | Pending |
| Day 14 | {(today + timedelta(days=11)).strftime('%Y-%m-%d')} | Pending |

---

**Report Generated by:** GAURANGA AI Follow-up Agent  
**Status:** ✅ COMPLETE
"""
    
    return report

def log_followup(results):
    """Log follow-up run to file"""
    today = get_current_date()
    log_entry = f"""
[{today.strftime('%Y-%m-%d %H:%M:%S')}] FOLLOW-UP AGENT RUN
Processed: {results['processed']}
Day 3: {len(results['day3'])}
Day 7: {len(results['day7'])}
Day 14: {len(results['day14'])}
---
"""
    
    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)

def main():
    """Main execution"""
    print("=" * 60)
    print("🤖 AI FOLLOW-UP AGENT - MAHA LAKSHMI")
    print("=" * 60)
    print()
    
    # Process follow-ups
    results, followups = process_followups()
    
    # Generate report
    report = generate_followup_report(results, followups)
    
    # Save report
    today = get_current_date()
    report_file = f"{OUTPUT_DIR}/FOLLOWUP-REPORT-{today.strftime('%Y-%m-%d')}.md"
    
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    with open(report_file, 'w') as f:
        f.write(report)
    
    # Log
    log_followup(results)
    
    # Print summary
    print("✅ FOLLOW-UP AGENT COMPLETE")
    print()
    print("📊 RESULTS:")
    print(f"   • Total Processed: {results['processed']}")
    print(f"   • Day 3 Follow-ups: {len(results['day3'])}")
    print(f"   • Day 7 Follow-ups: {len(results['day7'])}")
    print(f"   • Day 14 Follow-ups: {len(results['day14'])}")
    print()
    print(f"📄 Report saved to: {report_file}")
    print()
    
    # Print follow-ups
    if followups:
        print("📋 FOLLOW-UPS TO SEND:")
        for fu in followups[:5]:  # Show first 5
            lead = fu['lead']
            print(f"   • {lead['name']} ({fu['type']}) - {lead.get('email', 'No email')}")
        if len(followups) > 5:
            print(f"   ... and {len(followups) - 5} more")
    
    print()
    print("=" * 60)
    
    return report

if __name__ == '__main__':
    main()
