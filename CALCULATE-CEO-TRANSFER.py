#!/usr/bin/env python3
"""
CEO REVENUE TRANSFER CALCULATOR
MAHA LAKSHMI HOLDINGS

WARNING: Private keys should NEVER be stored in code!
Use environment variables for sensitive data.

Environment Variables Required:
- COMPANY_WALLET_PRIVATE_KEY: Private key for company wallet
- COMPANY_WALLET_ADDRESS: Company wallet address
"""

import json
import os
from datetime import datetime

# ============== WALLET ADDRESSES ==============
COMPANY_WALLET = "3f2918fc0610877b66d4bCF7fAb740916VxQlbjqHHz1ejP8A9t9gYo2zXJ7H6Kj"
CEO_WALLET = "1H3FZkKsX6jgTuqA23fduLVtxL7MrtgWe2"
BTC_PRICE_USD = 67000  # Approximate BTC price
BTC_PRICE_IDR = BTC_PRICE_USD * 16500

# ============== LOAD DATA ==============
def load_revenue_data():
    """Load revenue from tracker"""
    try:
        with open('ceo-revenue-share/02-revenue-tracker.json', 'r') as f:
            return json.load(f)
    except:
        return None

def load_config():
    """Load configuration"""
    try:
        with open('ceo-revenue-share/01-config.json', 'r') as f:
            return json.load(f)
    except:
        return None

# ============== CALCULATE TRANSFER ==============
def calculate_ceo_transfer():
    """Calculate CEO transfer based on actual revenue"""
    
    print("╔════════════════════════════════════════════════════════════════════════╗")
    print("║     💰 CEO REVENUE TRANSFER CALCULATION                         ║")
    print("║     MAHA LAKSHMI HOLDINGS                                       ║")
    print("╚════════════════════════════════════════════════════════════════════════╝")
    print()
    
    # Load data
    data = load_revenue_data()
    config = load_config()
    
    # Get actual revenue
    if data and 'monthly_summary' in data:
        if '2026-07' in data['monthly_summary']:
            monthly = data['monthly_summary']['2026-07']
            total_revenue = monthly.get('total_revenue', 0)
        else:
            total_revenue = data['monthly_summary'].get('total_revenue', 0)
    else:
        total_revenue = 0
    
    # Get transactions
    transactions = data.get('transactions', []) if data else []
    
    # Calculate CEO share (60%)
    ceo_percentage = config['distribution']['ceo_share_percent'] if config and 'distribution' in config else 60
    ceo_share_idr = total_revenue * (ceo_percentage / 100)
    ceo_share_btc = ceo_share_idr / BTC_PRICE_IDR
    
    # Output
    print(f"📅 Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M')} UTC")
    print()
    print("─" * 70)
    print()
    
    print("📊 REAL TRANSACTIONS:")
    print(f"   Total Transactions: {len(transactions)}")
    for t in transactions:
        print(f"   - {t.get('date', 'N/A')}: {t.get('description', 'N/A')} - Rp {t.get('amount', 0):,.0f}")
    print()
    
    print("💰 TOTAL REVENUE:")
    print(f"   Total: Rp {total_revenue:,.0f}")
    print()
    
    print("👑 CEO SHARE CALCULATION:")
    print(f"   Percentage: {ceo_percentage}%")
    print(f"   CEO Share (IDR): Rp {ceo_share_idr:,.0f}")
    print(f"   CEO Share (BTC): {ceo_share_btc:.8f} BTC")
    print()
    
    print("─" * 70)
    print()
    
    print("🪙 WALLET INFORMATION:")
    print()
    print("   📦 COMPANY WALLET (Tempat revenue masuk):")
    print(f"   Address: {COMPANY_WALLET}")
    print("   Platform: Tokocrypto")
    print("   Purpose: Penerimaan revenue perusahaan")
    print()
    
    print("   👑 CEO WALLET (Tempat transfer 60% profit):")
    print(f"   Address: {CEO_WALLET}")
    print("   Platform: Tokocrypto")
    print("   Purpose: Penerimaan 60% profit CEO")
    print()
    
    print("─" * 70)
    print()
    
    print("🔄 MONEY FLOW:")
    print("   1. Customer Bayar → COMPANY WALLET")
    print("   2. Company Terima BTC")
    print("   3. Hitung Profit (Revenue - Expenses)")
    print(f"   4. Transfer 60% ({ceo_share_btc:.8f} BTC) → CEO WALLET")
    print()
    
    print("═" * 70)
    print()
    
    if total_revenue > 0:
        print("✅ READY TO TRANSFER:")
        print(f"   Amount: {ceo_share_btc:.8f} BTC")
        print(f"   From: {COMPANY_WALLET}")
        print(f"   To: {CEO_WALLET}")
        print()
        print("   🔔 MANUAL ACTION: Buka Tokocrypto, login ke company wallet,")
        print("      transfer BTC ke CEO wallet!")
    else:
        print("⚠️ BELUM ADA REVENUE UNTUK DITRANSFER!")
        print("   Revenue di tracker: Rp 0")
        print("   Butuh actual payment dari customer terlebih dahulu.")
    print()
    print("═" * 70)
    
    # Save transfer instruction
    transfer_data = {
        "calculated_at": datetime.now().isoformat(),
        "total_revenue": total_revenue,
        "ceo_percentage": ceo_percentage,
        "ceo_share_idr": ceo_share_idr,
        "ceo_share_btc": ceo_share_btc,
        "btc_price_usd": BTC_PRICE_USD,
        "btc_price_idr": BTC_PRICE_IDR,
        "company_wallet": COMPANY_WALLET,
        "ceo_wallet": CEO_WALLET,
        "status": "READY" if total_revenue > 0 else "NO_REVENUE"
    }
    
    with open('ceo-revenue-share/latest-transfer.json', 'w') as f:
        json.dump(transfer_data, f, indent=2)
    
    return transfer_data

# ============== MAIN ==============
if __name__ == "__main__":
    calculate_ceo_transfer()
