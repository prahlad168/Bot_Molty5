#!/usr/bin/env python3
"""
🚀 TOKOCRYPTO CEO FEE TRANSFER
Transfer fee ke rekening CEO via Tokocrypto

PAK PUR - Jalankan script ini dari komputer/laptop Anda
yang terhubung ke internet Indonesia (tanpa VPN luar negeri)
"""

import urllib.request
import json
import hashlib
import hmac
import time

# ============================================
# KONFIGURASI - ISI DATA DI BAWAH INI
# ============================================

# Tokocrypto API Keys (dari https://www.tokocrypto.com/usercenter/settings/api-management)
API_KEY = "d2050BeBEea0AbCB6bD44E4940b4776DDsWDYHAJ5FQK2exVsySNI0vTziRSfzKy"
SECRET_KEY = "96d395c894166AbAdec4cEBd938a868fhPTxJYbbEwR7yvUyWd2RdYasHOU4Hl0e"

# Alamat wallet tujuan (rekening Pak Pur)
RECIPIENT_EMAIL = "pakpur@email.com"  # GANTI DENGAN EMAIL TOKOCRYPTO PAK PUR
RECIPIENT_WALLET = "0x..."  # GANTI DENGAN ADDRESS WALLET PAK PUR (USDT/TRX)

# Jumlah transfer (dalam USDT atau crypto lain)
AMOUNT = 50  # USDT - SESUAIKAN DENGAN FEE YANG MAU DIKIRIM

# Crypto yang ditransfer
CRYPTO_SYMBOL = "USDT"  # Atau "TRX", "IDRT", dll

# ============================================
# KODE DI BAWAH INI JANGAN DIUBAH
# ============================================

def get_tokocrypto_signature(secret_key, timestamp, method, path):
    """Generate Tokocrypto API signature"""
    message = f"{method}|{path}|{timestamp}"
    signature = hmac.new(
        secret_key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()
    return signature

def get_balance():
    """Ambil saldo akun Tokocrypto"""
    timestamp = str(int(time.time() * 1000))
    method = "GET"
    path = "/api/v1/account/balances"
    
    signature = get_tokocrypto_signature(SECRET_KEY, timestamp, method, path)
    
    headers = {
        "X-API-KEY": API_KEY,
        "X-SIGNATURE": signature,
        "X-TIMESTAMP": timestamp,
        "Content-Type": "application/json"
    }
    
    url = f"https://www.tokocrypto.com{path}"
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.read().decode()}"}
    except Exception as e:
        return {"error": str(e)}

def withdraw_crypto(symbol, address, amount):
    """Withdraw crypto ke wallet address"""
    timestamp = str(int(time.time() * 1000))
    method = "POST"
    path = "/api/v1/withdraw/crypto"
    
    body = json.dumps({
        "symbol": symbol,
        "address": address,
        "amount": str(amount),
        "network": "TRC20" if symbol == "USDT" else "TRX"
    })
    
    signature = get_tokocrypto_signature(SECRET_KEY, timestamp, method, path)
    
    headers = {
        "X-API-KEY": API_KEY,
        "X-SIGNATURE": signature,
        "X-TIMESTAMP": timestamp,
        "Content-Type": "application/json"
    }
    
    url = f"https://www.tokocrypto.com{path}"
    
    try:
        req = urllib.request.Request(
            url,
            data=body.encode(),
            headers=headers,
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.read().decode()}"}
    except Exception as e:
        return {"error": str(e)}

def main():
    print("=" * 60)
    print("🚀 TOKOCRYPTO CEO FEE TRANSFER")
    print("=" * 60)
    print()
    
    # Step 1: Cek saldo
    print("📊 STEP 1: Mengecek saldo...")
    print("-" * 40)
    balance = get_balance()
    
    if "error" in balance:
        print(f"❌ Gagal mengambil saldo!")
        print(f"   Error: {balance['error']}")
        print()
        print("💡 Kemungkinan penyebab:")
        print("   - VPN aktif dengan server luar Indonesia")
        print("   - Koneksi internet terbatas")
        print("   - API keys tidak valid")
        return
    
    print("✅ Berhasil mengambil saldo!")
    print(json.dumps(balance, indent=2))
    print()
    
    # Step 2: Konfirmasi withdraw
    print("📋 STEP 2: Konfirmasi Transfer")
    print("-" * 40)
    print(f"   Crypto: {CRYPTO_SYMBOL}")
    print(f"   Jumlah: {AMOUNT}")
    print(f"   Tujuan: {RECIPIENT_WALLET[:10]}...{RECIPIENT_WALLET[-10:]}")
    print()
    
    confirm = input("Lanjutkan transfer? (ya/tidak): ").strip().lower()
    
    if confirm != 'ya':
        print("Transfer dibatalkan.")
        return
    
    # Step 3: Execute withdraw
    print()
    print("⏳ STEP 3: Mengeksekusi transfer...")
    print("-" * 40)
    
    result = withdraw_crypto(CRYPTO_SYMBOL, RECIPIENT_WALLET, AMOUNT)
    
    if "error" in result:
        print(f"❌ Gagal melakukan transfer!")
        print(f"   Error: {result['error']}")
    else:
        print("✅ Transfer berhasil!")
        print(json.dumps(result, indent=2))
    
    print()
    print("=" * 60)
    print("✅ PROSES SELESAI")
    print("=" * 60)

if __name__ == "__main__":
    main()
