# =====================================================================
#  X AGENT — SETTINGS
#  Bot ka behaviour badalna ho to SIRF yeh file edit karo.
#  (Keys / passwords yahan mat daalna — woh GitHub Secrets mein jaate hain)
# =====================================================================

X_HANDLE = "Siraaaaaaajatt"        # bina @ ke (sirf info ke liye)
TIMEZONE = "Asia/Kolkata"          # saare times IST mein

# Tumhari "awaaz" — AI isi style mein likhega. Apne hisaab se badal sakte ho.
PERSONA = """You write as Smasher (@Siraaaaaaajatt) — a Web3 builder and crypto content creator from India.
Voice: confident, clear, friendly and professional. Calm, data-first, no hype, no shilling, no cringe slang."""

# ---------------------------------------------------------------------
# 1) DAILY POSTS  (24-hour format, IST)
# ---------------------------------------------------------------------
POSTS = [
    {"name": "gm",     "time": "07:30", "enabled": True},   # Good morning post
    {"name": "market", "time": "18:30", "enabled": True},   # Crypto market info post
    {"name": "gn",     "time": "22:30", "enabled": True},   # Good night post
]
POST_WINDOW_MINUTES = 120   # bot late chala to time ke 2 ghante andar hi post karega, warna us din skip
POST_LANGUAGE = "English"   # "English" ya "Hinglish"
MAX_POST_CHARS = 270        # X limit 280 hai; thoda margin rakha hai

# Market post mein kaunse coins dikhaane hain (CoinGecko IDs)
MARKET_COINS = ["bitcoin", "ethereum", "solana", "binancecoin", "ripple"]

# ---------------------------------------------------------------------
# 2) COMMENT REPLIES  (jo log tumhari post pe comment karte hain)
# ---------------------------------------------------------------------
#  "approve" = AI reply likhega, Telegram pe bhejega, tum 1 tap mein post karoge   ← SAFE (default)
#  "auto"    = bot khud reply post karega. X ke rules ke hisaab se AI reply-bot ke
#              liye X ka written approval chahiye — approval milne ke baad hi on karna.
#  "off"     = replies band
REPLY_MODE = "approve"
REPLY_DELAY_MINUTES = 5      # comment aane ke kam se kam itne minute baad reply
MAX_REPLIES_PER_DAY = 40
MAX_REPLIES_PER_RUN = 8
MAX_MENTION_AGE_HOURS = 6    # isse purane comments ignore
MAX_REPLY_CHARS = 220
MENTIONS_MAX_RESULTS = 50    # ek baar mein max kitne naye comments padhe (har read ≈ $0.005)

# ---------------------------------------------------------------------
# 3) GM DRAFTS  (jinko follow karte ho unki GM posts ke liye reply drafts)
#    X API ab un posts pe bot-reply allow nahi karta, isliye bot Telegram pe
#    ready-made reply + 1-tap button bhejta hai — post tum khud karte ho.
# ---------------------------------------------------------------------
GM_DRAFTS_ENABLED = True
GM_DRAFTS_TIME = "09:00"           # roz is time ke baad ek baar
GM_DRAFTS_WINDOW_MINUTES = 120
GM_TIMELINE_READS = 60             # kitni timeline posts scan kare (60 × $0.005 ≈ $0.30/din)
MAX_GM_DRAFTS = 12

# ---------------------------------------------------------------------
# 4) AI MODEL (Claude API)
# ---------------------------------------------------------------------
LLM_MODEL = "claude-sonnet-5-5"          # posts ke liye (best quality)
REPLY_MODEL = "claude-sonnet-5-5"        # replies ke liye — sasta chahiye to "claude-haiku-5-5"

# ---------------------------------------------------------------------
# Advanced (chhedne ki zarurat nahi)
# ---------------------------------------------------------------------
LOOP_SECONDS = 300                       # --loop mode mein har kitne second chale
INTENT_URL = "https://x.com/intent/post" # 1-tap reply links
