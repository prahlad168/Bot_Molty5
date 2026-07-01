# Molty Royale Bot Agent - Project Memory

## Project Overview
Bot AI untuk Molty Royale game - blockchain-based battle royale game on CROSS Chain.

## Repository
- **Path**: `/workspace/project/Bot_Molty5`
- **Version**: 2.0.0
- **Skill Version**: 1.5.2

## Current Status
⚠️ Bot perlu credentials untuk bisa dijalankan.

## Changes Made (2026-07-01)

### 1. Airdrop Configuration Added
Fitur airdrop sudah ditambahkan ke bot:

**Files Modified:**
- `bot/config.py` - Added airdrop environment variables
- `bot/state_router.py` - Added AIRDROP_PENDING state
- `bot/heartbeat.py` - Added `_handle_airdrop_pending()` method
- `bot/__init__.py` - Updated exports
- `.env.example` - Added airdrop configuration template

**Files Created:**
- `bot/airdrop.py` - Airdrop management module

### 2. Airdrop Environment Variables
```env
ENABLE_AIRDROP=true
AIRDROP_WHITELIST_ONLY=false
AIRDROP_MIN_BALANCE=0
AIRDROP_GAS_PRIORITY_FEE=
AIRDROP_MAX_GAS_PRICE=100
AIRDROP_CLAIM_BATCH_SIZE=10
AIRDROP_RETRY_ATTEMPTS=3
AIRDROP_RETRY_DELAY=60
AIRDROP_NOTIFY_WEBHOOK=
AIRDROP_AUTO_CLAIM=true
AIRDROP_CLAIM_DEADLINE=
```

## New Project: Speech-to-Text App
Lokasi: `/workspace/project/speech-to-text/`

Aplikasi voice control untuk bot Molty Royale.

### Setup:
```bash
cd /workspace/project/speech-to-text
pip install -r requirements.txt
```

### Run:
```bash
python app.py
```

### Commands:
- "bot status" - Periksa status bot
- "bot mulai" - Jalankan bot
- "bot berhenti" - Hentikan bot
- "waktu" - Tampilkan waktu
- "bantuan" - Tampilkan bantuan
- "keluar" - Keluar aplikasi

## Next Steps (To Continue at Home)

### 1. Setup Credentials
Bot memerlukan file `.env` dengan credentials berikut:

```env
AGENT_NAME=YourBotName
API_KEY=<your_api_key>
AGENT_PRIVATE_KEY=<your_private_key>
AGENT_WALLET_ADDRESS=<your_wallet_address>
OWNER_EOA=<owner_wallet_address>
OWNER_PRIVATE_KEY=<owner_private_key>
```

### 2. Setup Instructions
1. Clone repository ke laptop
2. Buat file `.env` dari `.env.example`
3. Isi credentials yang diperlukan
4. Install dependencies: `pip install -r requirements.txt`
5. Jalankan bot: `python -m bot.main`

### 3. Credentials Sources
- **API_KEY**: Didapat dari Molty Royale API setelah first-run
- **AGENT_PRIVATE_KEY**: Dari wallet Anda (MetaMask, etc.)
- **AGENT_WALLET_ADDRESS**: Bisa di-generate dari private key
- **OWNER_EOA & OWNER_PRIVATE_KEY**: Wallet owner untuk gas fees

## Key Files Reference
- `bot/main.py` - Entry point
- `bot/heartbeat.py` - Main loop
- `bot/airdrop.py` - Airdrop module (NEW)
- `bot/config.py` - Configuration
- `bot/state_router.py` - State machine
- `.env.example` - Environment template

## Dashboard
- Default port: 8080
- WebSocket: wss://cdn.moltyroyale.com/ws/agent
- API Base: https://cdn.moltyroyale.com/api

## Notes
- State airdrop disimpan di: `~/.molty-royale/airdrop-state.json`
- Memory bot disimpan di: `~/.molty-royale/molty-royale-context.json`
- Credentials aman di: `dev-agent/` dengan chmod 600