#!/usr/bin/env python3
"""
💰 REVENUE SAVE AGENT
Save every payment received, track all revenue

Usage:
    python3 revenue_save.py --amount 500 --source "Four Seasons" --method USDT
    python3 revenue_save.py --amount 8000000 --source "Bali Hotel" --method IDR
"""

import json
import sys
from datetime import datetime
from pathlib import Path

# Paths
REVENUE_DIR = Path(__file__).parent
TRACKER_FILE = REVENUE_DIR / "REVENUE-TRACKER.json"
LOG_FILE = REVENUE_DIR / "revenue_log.txt"

# USD to IDR rate
USD_TO_IDR = 16000

def log(msg):
    """Log to console and file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {msg}"
    print(log_entry)
    with open(LOG_FILE, "a") as f:
        f.write(log_entry + "\n")

def load_tracker():
    """Load revenue tracker"""
    if TRACKER_FILE.exists():
        with open(TRACKER_FILE) as f:
            return json.load(f)
    return get_default_tracker()

def save_tracker(data):
    """Save revenue tracker"""
    with open(TRACKER_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_default_tracker():
    """Default tracker structure"""
    return {
        "tracker": {
            "created": datetime.now().strftime("%Y-%m-%d"),
            "last_updated": datetime.now().isoformat(),
            "version": "1.0.0",
            "ceo": "i Made Purna Ananda",
            "usdt_wallet": "TNFs1SP2C8HxGSJkSH3hJamf8ukgtnW7U6",
            "bca_account": "6485086645"
        },
        "totals": {
            "all_time": {"total_revenue_usd": 0, "total_revenue_idr": 0, "total_transactions": 0, "total_profit_80": 0},
            "this_month": {"month": datetime.now().strftime("%Y-%m"), "total_revenue_usd": 0, "total_revenue_idr": 0, "total_transactions": 0, "total_profit_80": 0},
            "this_week": {"week_start": datetime.now().strftime("%Y-%m-%d"), "total_revenue_usd": 0, "total_revenue_idr": 0, "total_transactions": 0, "total_profit_80": 0},
            "today": {"date": datetime.now().strftime("%Y-%m-%d"), "total_revenue_usd": 0, "total_revenue_idr": 0, "total_transactions": 0, "total_profit_80": 0}
        },
        "transactions": []
    }

def add_revenue(amount, source, method="USDT", currency="USD", client="", service="", invoice=""):
    """Add new revenue entry"""
    tracker = load_tracker()
    
    # Calculate amounts
    if currency == "USD":
        amount_usd = amount
        amount_idr = amount * USD_TO_IDR
    else:
        amount_usd = amount / USD_TO_IDR
        amount_idr = amount
    
    # Profit calculations (80% to CEO)
    profit_80 = amount_usd * 0.80
    profit_80_idr = profit_80 * USD_TO_IDR
    
    # Create transaction
    transaction = {
        "id": f"REV-{datetime.now().strftime('%Y%m%d')}-{len(tracker['transactions']) + 1:03d}",
        "timestamp": datetime.now().isoformat(),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "source": source,
        "client": client,
        "service": service,
        "invoice": invoice,
        "amount_usd": round(amount_usd, 2),
        "amount_idr": int(amount_idr),
        "payment_method": method,
        "profit_80": round(profit_80, 2),
        "profit_80_idr": int(profit_80_idr),
        "status": "RECEIVED"
    }
    
    # Add to transactions
    tracker["transactions"].append(transaction)
    
    # Update totals
    tracker["totals"]["all_time"]["total_revenue_usd"] += amount_usd
    tracker["totals"]["all_time"]["total_revenue_idr"] += amount_idr
    tracker["totals"]["all_time"]["total_transactions"] += 1
    tracker["totals"]["all_time"]["total_profit_80"] += profit_80
    
    tracker["totals"]["this_month"]["total_revenue_usd"] += amount_usd
    tracker["totals"]["this_month"]["total_revenue_idr"] += amount_idr
    tracker["totals"]["this_month"]["total_transactions"] += 1
    tracker["totals"]["this_month"]["total_profit_80"] += profit_80
    
    tracker["totals"]["this_week"]["total_revenue_usd"] += amount_usd
    tracker["totals"]["this_week"]["total_revenue_idr"] += amount_idr
    tracker["totals"]["this_week"]["total_transactions"] += 1
    tracker["totals"]["this_week"]["total_profit_80"] += profit_80
    
    tracker["totals"]["today"]["total_revenue_usd"] += amount_usd
    tracker["totals"]["today"]["total_revenue_idr"] += amount_idr
    tracker["totals"]["today"]["total_transactions"] += 1
    tracker["totals"]["today"]["total_profit_80"] += profit_80
    
    tracker["tracker"]["last_updated"] = datetime.now().isoformat()
    
    # Save
    save_tracker(tracker)
    
    return transaction

def show_summary():
    """Show revenue summary"""
    tracker = load_tracker()
    totals = tracker["totals"]
    
    print("\n" + "="*60)
    print("💰 REVENUE SUMMARY - MAHA LAKSHMI HOLDINGS")
    print("="*60)
    print(f"\n📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"👑 CEO: {tracker['tracker']['ceo']}")
    
    print("\n📊 TODAY:")
    print(f"   Revenue: ${totals['today']['total_revenue_usd']:.2f}")
    print(f"   Transactions: {totals['today']['total_transactions']}")
    print(f"   Profit (80%): ${totals['today']['total_profit_80']:.2f}")
    
    print("\n📊 THIS WEEK:")
    print(f"   Revenue: ${totals['this_week']['total_revenue_usd']:.2f}")
    print(f"   Transactions: {totals['this_week']['total_transactions']}")
    print(f"   Profit (80%): ${totals['this_week']['total_profit_80']:.2f}")
    
    print("\n📊 THIS MONTH:")
    print(f"   Revenue: ${totals['this_month']['total_revenue_usd']:.2f}")
    print(f"   Transactions: {totals['this_month']['total_transactions']}")
    print(f"   Profit (80%): ${totals['this_month']['total_profit_80']:.2f}")
    
    print("\n📊 ALL TIME:")
    print(f"   Revenue: ${totals['all_time']['total_revenue_usd']:.2f}")
    print(f"   Transactions: {totals['all_time']['total_transactions']}")
    print(f"   Profit (80%): ${totals['all_time']['total_profit_80']:.2f}")
    
    print("\n💳 PAYMENT INFO:")
    print(f"   USDT Wallet: {tracker['tracker']['usdt_wallet']}")
    print(f"   BCA Account: {tracker['tracker']['bca_account']}")
    
    print("\n" + "="*60)

def show_transactions(limit=10):
    """Show recent transactions"""
    tracker = load_tracker()
    transactions = tracker["transactions"][-limit:]
    
    print("\n📋 RECENT TRANSACTIONS:")
    for t in reversed(transactions):
        print(f"\n   {t['id']}")
        print(f"   {t['date']} - {t['source']}")
        print(f"   ${t['amount_usd']:.2f} ({t['payment_method']})")
        print(f"   Profit: ${t['profit_80']:.2f}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="💰 Revenue Save Agent")
    parser.add_argument("--amount", type=float, help="Amount in USD or IDR")
    parser.add_argument("--source", type=str, help="Source/client name")
    parser.add_argument("--method", type=str, default="USDT", help="Payment method (USDT/BANK/DANA)")
    parser.add_argument("--currency", type=str, default="USD", help="Currency (USD/IDR)")
    parser.add_argument("--client", type=str, help="Client name")
    parser.add_argument("--service", type=str, help="Service provided")
    parser.add_argument("--invoice", type=str, help="Invoice number")
    parser.add_argument("--summary", action="store_true", help="Show summary")
    parser.add_argument("--transactions", action="store_true", help="Show transactions")
    
    args = parser.parse_args()
    
    if args.summary:
        show_summary()
    elif args.transactions:
        show_transactions()
    elif args.amount and args.source:
        transaction = add_revenue(
            amount=args.amount,
            source=args.source,
            method=args.method,
            currency=args.currency,
            client=args.client or args.source,
            service=args.service or "Service",
            invoice=args.invoice or f"INV-{datetime.now().strftime('%Y%m%d')}"
        )
        log(f"💰 REVENUE ADDED: ${transaction['amount_usd']:.2f} from {transaction['source']}")
        print(f"\n✅ Revenue saved successfully!")
        print(f"   ID: {transaction['id']}")
        print(f"   Amount: ${transaction['amount_usd']:.2f}")
        print(f"   Source: {transaction['source']}")
        print(f"   Profit (80%): ${transaction['profit_80']:.2f}")
        show_summary()
    else:
        parser.print_help()
        print("\n💡 Examples:")
        print("   python3 revenue_save.py --amount 500 --source 'Four Seasons' --method USDT")
        print("   python3 revenue_save.py --summary")
        print("   python3 revenue_save.py --transactions")
