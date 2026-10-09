# X Agent — @Siraaaaaaajatt ka auto-manager 🤖

Har 10 minute GitHub ke free servers pe chalta hai. Tumhara laptop on rakhne ki zarurat nahi.

## Ye kya karta hai

| Kaam | Time (IST) | Kaise |
|---|---|---|
| ☀️ Good Morning post | 7:30 AM | Roz naya, AI likhta hai (repeat nahi karta) |
| 📊 Crypto market post | 6:30 PM | CoinGecko + Fear & Greed ka live data, professional format, roz alag angle |
| 🌙 Good Night post | 10:30 PM | Roz naya |
| 💬 Comments ke reply | comment ke 5+ min baad | AI comment samajh ke reply likhta hai → Telegram pe aata hai → 1 tap mein post |
| 🤝 Following ki GM posts | 9:00 AM | Unki GM posts dhoond ke har ek ke liye personal GM reply → Telegram pe 1-tap buttons |

Spam/scam/"DM me" type comments ko AI khud skip kar deta hai. Kisi bhi post ya reply mein link nahi jaata (link wali post X pe $0.20 ki padti hai) aur financial advice / price prediction nahi deta.

---

## ⚠️ X ke 2026 rules — isliye kuch cheezein "1-tap" hain

1. **23 Feb 2026 se** X API se reply tabhi jaata hai jab samne wale ne tumhe @mention ya quote kiya ho. Jinko tum follow karte ho unki GM posts pe bot API se reply kar hi nahi sakta — isliye bot ready-made reply bhejta hai aur post tum ek tap mein karte ho.
2. X ke Automation Rules ke hisaab se **AI reply-bot chalane ke liye X ka written approval** chahiye. Isliye comments ke liye default `REPLY_MODE = "approve"` hai. Approval mil jaye (developer portal se request) to `config.py` mein `"auto"` kar do — bot khud 5 min baad reply post karega.
3. Browser automation (Selenium/website scripting) se X permanent suspend karta hai. Ye bot sirf official API use karta hai.

---

## 💰 Kharcha (andaza, per month)

| Cheez | Rate | Andaza |
|---|---|---|
| 3 posts/din | $0.015/post | ~$1.4 |
| Comments padhna (~20/din + context) | $0.005/read | ~$6 |
| GM drafts (60 posts/din scan) | $0.005/read | ~$9 |
| Auto replies (sirf "auto" mode mein) | $0.01/reply | ~$6 |
| Claude API (AI writing) | | ~$5–10 |
| GitHub Actions, Telegram, CoinGecko | | Free |

**Total ≈ $20–30/month.** Kam karna ho to `config.py` mein `GM_TIMELINE_READS` ghatao ya `REPLY_MODEL = "claude-haiku-5-5"` karo.
X console mein **spend limit zaroor set karo**.

---

## 🛠️ Setup (30–40 min, ek baar)

### Step 1 — X Developer app
1. **console.x.com** (ya developer.x.com) pe **@Siraaaaaaajatt** se login karo.
2. Naya **App** banao.
3. App → **User authentication settings** → App permissions: **Read and write** → Save.
   (Type: "Web App, Automated App or Bot", Callback URL: `https://example.com`, Website: koi bhi URL)
4. **Keys and tokens** → **API Key + API Secret** generate karo → copy.
5. Usi page pe **Access Token + Access Token Secret** generate karo → copy.
   ⚠️ Step 3 ke **baad** banana, warna token "Read only" banega aur post fail hogi.
6. **Billing / Credits** mein $10 daalo aur **spend limit** set karo.

### Step 2 — Claude API key
1. **platform.claude.com** → API Keys → **Create Key** → copy.
2. Billing mein $5–10 credit daalo.

### Step 3 — CoinGecko key (free)
1. **coingecko.com/en/api** → sign up → Developer Dashboard → **Create Demo API key** → copy.

### Step 4 — Telegram bot (drafts yahin aayenge)
1. Telegram mein **@BotFather** kholo → `/newbot` → naam do → jo **token** mile copy karo.
2. Apne naye bot ko kholo aur **"hi"** bhejo.
3. Browser mein ye kholo (TOKEN ki jagah apna token):
   ```
   https://api.telegram.org/botTOKEN/getUpdates
   ```
   Usme `"chat":{"id":123456789` dikhega — ye number tumhara **Chat ID** hai.

### Step 5 — GitHub secrets
Repo ready hai: **https://github.com/Smasher1614/x-agent** (Public — Actions unlimited free; tumhari keys Secrets mein rehti hain, public nahi hoti).

1. Repo kholo → **Settings → Secrets and variables → Actions → New repository secret** — ye 8 secrets add karo:

   | Name | Value |
   |---|---|
   | `X_API_KEY` | Step 1 ki API Key |
   | `X_API_SECRET` | Step 1 ki API Secret |
   | `X_ACCESS_TOKEN` | Step 1 ka Access Token |
   | `X_ACCESS_TOKEN_SECRET` | Step 1 ka Access Token Secret |
   | `ANTHROPIC_API_KEY` | Step 2 |
   | `COINGECKO_API_KEY` | Step 3 |
   | `TELEGRAM_BOT_TOKEN` | Step 4 ka token |
   | `TELEGRAM_CHAT_ID` | Step 4 ka number |

2. **Settings → Actions → General → Workflow permissions** → **Read and write permissions** → Save.

Jab tak secrets nahi daaloge, bot har run mein bas "Setup baaki hai" likh ke ruk jayega — kuch post nahi hoga.

> Workflow file (`.github/workflows/x-agent.yml`) repo mein nahi dikhe to: **Add file → Create new file** → naam `.github/workflows/x-agent.yml` → zip ki isi file ka content paste → Commit.

### Step 6 — Test (kuch post NAHI hoga)
**Actions** tab → **X Agent** → **Run workflow** → mode: **preview** → Run.
1–2 min mein Telegram pe sample GM, market post, GN aur ek reply-test aa jayega + X login check. Pasand na aaye to `config.py` mein `PERSONA` badlo aur dobara preview chalao.

### Step 7 — Live 🚀
Kuch nahi karna — schedule apne aap har 10 min chalega. Turant chalana ho to Run workflow → mode: **run**.
Note: GitHub ka schedule kabhi 5–15 min late chalta hai, isliye post time thoda aage-peeche ho sakta hai.

---

## ⚙️ Settings badalna — `config.py`
GitHub pe `config.py` kholo → ✏️ pencil icon → edit → Commit. Agla run naye settings use karega.

| Kya badalna hai | Setting |
|---|---|
| Post ke time | `POSTS` (24-hour format) |
| Tumhari awaaz / tone | `PERSONA` |
| Posts Hinglish mein | `POST_LANGUAGE = "Hinglish"` |
| Comments pe auto reply (approval ke baad) | `REPLY_MODE = "auto"` |
| Reply delay | `REPLY_DELAY_MINUTES` |
| GM drafts band | `GM_DRAFTS_ENABLED = False` |
| Sasta AI | `REPLY_MODEL = "claude-haiku-5-5"` |

**Auto mode mein:** jo user sirf "STOP" reply kare, use aage auto-reply nahi jaata (X rule). Bio mein likh sakte ho: *"Reply STOP to opt out of auto-replies."*

**Bot band karna:** Actions → X Agent → `...` → **Disable workflow**.

---

## 💻 Apne PC/server pe chalana (optional)
```bash
pip install -r requirements.txt
cp .env.example .env        # Windows: copy .env.example .env  — phir values bharo
python bot.py --preview     # test
python bot.py --loop        # har 5 min chalta rahega
```

---

## 🆘 Problem aaye to
| Dikkat | Fix |
|---|---|
| `401 Unauthorized` | Keys galat, ya Access Token permissions badalne se pehle bana tha → Step 1.5 dobara |
| `403 ... not allowed to reply` (auto mode) | X ka reply rule — bot us comment ko skip kar deta hai, normal hai |
| `402` / credits error | X console mein credits khatam |
| Market post nahi gaya | `COINGECKO_API_KEY` secret check karo |
| Telegram pe kuch nahi aaya | Bot ko "hi" bheja? Chat ID sahi? |
| Workflow ruk gaya | Actions tab → X Agent → **Enable workflow** |

Har run ka log: **Actions** tab → koi bhi run → **agent** → **Run bot**.
