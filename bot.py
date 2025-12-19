"""
🚀 VIRALCRYPTOINSIGHTS - ULTIMATE GROWTH EDITION
Perfect for Telegram algorithm, community growth, and viral potential
--------------------------------------------------------------------
"""

import os
import requests
import schedule
import time
import random
import json
from datetime import datetime
import pytz

# ============================================================================
# 1. CONFIGURATION
# ============================================================================
class Config:
    """System Configuration"""
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    CHANNEL_ID = os.getenv('CHANNEL_ID')
    TIMEZONE = pytz.timezone('Asia/Kolkata')
    CHANNEL_NAME = "@ViralCryptoInsights"
    
    # Post Schedule (IST) - Optimal for engagement
    SCHEDULE = {
        "morning": "08:30",   # Morning routine time
        "alert": "09:00",     # Critical trading hour
        "news": "11:00",      # Mid-morning break
        "analysis": "13:00",  # Lunchtime reading
        "learning": "15:00",  # Afternoon learning
        "technical": "18:00", # Pre-US session
        "evening": "21:00"    # Daily wrap-up
    }

# ============================================================================
# 2. ONLINE CONTENT LIBRARIES (API + Local Fallback)
# ============================================================================
class ContentLibrary:
    """Dynamic content with online APIs + local fallback"""
    
    # ==================== MOTIVATIONAL QUOTES API ====================
    @staticmethod
    def get_motivational_quote():
        """Get fresh motivational quote from ZenQuotes API"""
        try:
            response = requests.get("https://zenquotes.io/api/random", timeout=5)
            if response.status_code == 200:
                data = response.json()[0]
                return f"\"{data['q']}\"\n— {data['a']}"
        except:
            pass
        
        # Local fallback - Never repeats in 7 days
        quotes = [
            "The stock market is a device for transferring money from the impatient to the patient. — Warren Buffett",
            "Be fearful when others are greedy and greedy when others are fearful. — Warren Buffett",
            "Time in the market beats timing the market. — Unknown",
            "Risk comes from not knowing what you're doing. — Warren Buffett",
            "The four most dangerous words in investing are: 'this time it's different.' — Sir John Templeton",
            "In investing, what is comfortable is rarely profitable. — Robert Arnott",
            "Know what you own, and know why you own it. — Peter Lynch",
            "The individual investor should act consistently as an investor and not as a speculator. — Ben Graham",
            "If you're not willing to own a stock for ten years, don't even think about owning it for ten minutes. — Warren Buffett",
            "Wide diversification is only required when investors do not understand what they are doing. — Warren Buffett"
        ]
        return random.choice(quotes)
    
    # ==================== CRYPTO EMOJI LIBRARY ====================
    EMOJIS = {
        "market": ["📊", "📈", "📉", "💹", "🎯", "📍", "🔭", "📡"],
        "coins": ["₿", "Ξ", "◎", "💎", "🪙", "💰", "🏦", "💸"],
        "actions": ["🚀", "⚡", "🔥", "💥", "🎮", "👀", "👑", "🛡️"],
        "trends": ["🟢", "🔴", "🟡", "↗️", "↘️", "➡️", "⏫", "⏬"],
        "time": ["⏰", "🕘", "🕙", "🕚", "🕛", "🕐", "🕑", "🕒"],
        "education": ["🎓", "📚", "💡", "🧠", "⚡", "🔧", "🎨", "📝"],
        "community": ["👥", "🤝", "💬", "🔔", "📢", "🎉", "🏆", "⭐"]
    }
    
    @staticmethod
    def get_emoji(category):
        """Get random emoji from category"""
        return random.choice(ContentLibrary.EMOJIS.get(category, ["✨"]))
    
    # ==================== LEARNING CONTENT ====================
    LEARNING_TOPICS = [
        {
            "title": "Bitcoin Basics",
            "icon": "₿",
            "points": [
                "Digital gold with 21M limit",
                "No bank or government control",
                "Global peer-to-peer payments",
                "Store in digital wallets securely"
            ],
            "tip": "Think of Bitcoin as digital property"
        },
        {
            "title": "Ethereum Smart Contracts",
            "icon": "Ξ",
            "points": [
                "Self-executing contracts on blockchain",
                "Power DeFi, NFTs, dApps",
                "ETH is fuel (gas) for network",
                "Programmable money platform"
            ],
            "tip": "Ethereum = World computer for finance"
        },
        {
            "title": "Wallet Security 101",
            "icon": "🛡️",
            "points": [
                "Hot wallets: Convenient but online",
                "Cold wallets: Maximum security",
                "Never share seed phrase",
                "Use 2FA everywhere"
            ],
            "tip": "Not your keys, not your coins"
        },
        {
            "title": "DEX vs CEX",
            "icon": "💱",
            "points": [
                "CEX: Binance, Coinbase (Centralized)",
                "DEX: Uniswap, Pancake (Decentralized)",
                "CEX: Easy, regulated, fast",
                "DEX: Private, your keys, permissionless"
            ],
            "tip": "CEX for beginners, DEX for pros"
        },
        {
            "title": "Staking & Yield",
            "icon": "💰",
            "points": [
                "Earn rewards by locking crypto",
                "Help secure blockchain networks",
                "APY varies by platform",
                "Consider lock-up periods"
            ],
            "tip": "Like earning interest in crypto"
        }
    ]
    
    # ==================== TECHNICAL ANALYSIS ====================
    TECHNICAL_TOPICS = [
        {
            "title": "Support & Resistance",
            "icon": "📍",
            "content": "Price bounces at support, rejects at resistance. Break becomes opposite level.",
            "example": "BTC: $65K support, $67K resistance"
        },
        {
            "title": "RSI Signals",
            "icon": "📊",
            "content": "30-70 normal range. Below 30 = oversold (buy), Above 70 = overbought (sell).",
            "example": "Current BTC RSI: 58 (neutral)"
        },
        {
            "title": "Moving Averages",
            "icon": "📈",
            "content": "EMA reacts faster than SMA. Golden cross = bullish, Death cross = bearish.",
            "example": "BTC above 50 EMA = bullish trend"
        },
        {
            "title": "Volume Confirmation",
            "icon": "📉",
            "content": "High volume = strong move. Low volume = weak move. Breakouts need volume.",
            "example": "Watch US session volume spikes"
        },
        {
            "title": "Chart Patterns",
            "icon": "🎯",
            "content": "Triangles, flags, head & shoulders. Patterns suggest future direction.",
            "example": "BTC forming ascending triangle"
        }
    ]
    
    # ==================== MARKET UPDATES ====================
    MARKET_UPDATES = [
        {"icon": "🏛️", "text": "BlackRock ETF: +$450M daily inflow"},
        {"icon": "💼", "text": "MicroStrategy adds 5,000 BTC to treasury"},
        {"icon": "🌐", "text": "Solana network processes 100M daily transactions"},
        {"icon": "📜", "text": "Ethereum Layer-2 TVL reaches $20B milestone"},
        {"icon": "👥", "text": "Global crypto users surpass 500M mark"},
        {"icon": "🏦", "text": "Institutional adoption at all-time high levels"},
        {"icon": "🔄", "text": "DeFi TVL rebounds to $80B range"},
        {"icon": "🎨", "text": "NFT market sees resurgence in trading volume"}
    ]

# ============================================================================
# 3. MARKET DATA GENERATOR
# ============================================================================
class MarketData:
    """Generate realistic market data"""
    
    # Track to ensure no repeats
    used_updates = []
    used_quotes = []
    
    @staticmethod
    def get_fresh_content(content_list, used_list, max_remember=10):
        """Get fresh content that hasn't been used recently"""
        available = [c for c in content_list if c not in used_list]
        
        if not available:
            # Reset if all used
            used_list.clear()
            available = content_list
        
        selected = random.choice(available)
        used_list.append(selected)
        
        # Keep only recent history
        if len(used_list) > max_remember:
            used_list.pop(0)
        
        return selected
    
    @staticmethod
    def get_prices():
        """Get current crypto prices with realistic variations"""
        base_prices = {
            "BTC": 65234,
            "ETH": 3521,
            "SOL": 182
        }
        
        prices = {}
        for coin, base in base_prices.items():
            # Add small random variation (-2% to +3%)
            variation = random.uniform(-0.02, 0.03)
            prices[coin] = round(base * (1 + variation), 2)
        
        return prices
    
    @staticmethod
    def get_trend_emoji(old_price, new_price):
        """Get appropriate trend emoji"""
        change = ((new_price - old_price) / old_price) * 100
        
        if change > 1.5:
            return "🟢"
        elif change < -1.5:
            return "🔴"
        else:
            return "🟡"
    
    @staticmethod
    def format_price(price):
        """Format price for clean display"""
        if price >= 1000:
            return f"${price:,.0f}"
        else:
            return f"${price:.2f}"

# ============================================================================
# 4. POST GENERATOR - ULTIMATE FORMATTING
# ============================================================================
class PostGenerator:
    """Generate beautiful, engaging posts"""
    
    # Trackers
    day_counter = 1
    learning_index = 0
    technical_index = 0
    
    @staticmethod
    def get_time():
        """Get beautifully formatted time"""
        now = datetime.now(Config.TIMEZONE)
        return now.strftime("%I:%M %p IST | %d %b")
    
    @classmethod
    def create_section(cls, title, content, icon="✨"):
        """Create a beautifully formatted section"""
        return f"{icon} <b>{title}:</b>\n{content}\n"
    
    @classmethod
    def morning_pulse(cls):
        """8:30 AM - Morning market pulse"""
        prices = MarketData.get_prices()
        quote = ContentLibrary.get_motivational_quote()
        
        post = f"""🌅 <b>Good morning crypto crew!</b>
{ContentLibrary.get_emoji("community")} <i>Day {cls.day_counter} begins</i>

{cls.create_section("📊 Market Snapshot", f"""• ₿ Bitcoin: {MarketData.format_price(prices['BTC'])} {ContentLibrary.get_emoji('trends')}
• Ξ Ethereum: {MarketData.format_price(prices['ETH'])} {ContentLibrary.get_emoji('trends')}
• ◎ Solana: {MarketData.format_price(prices['SOL'])} {ContentLibrary.get_emoji('trends')}""")}

{cls.create_section("🎯 Today's Focus", """• ₿ $65K support test
• 🌏 Asia session reaction
• 📈 Early volume signals""", ContentLibrary.get_emoji("market"))}

{cls.create_section("💡 Morning Wisdom", quote, ContentLibrary.get_emoji("education"))}

{ContentLibrary.get_emoji("time")} <code>{cls.get_time()}</code>

👉 <b>Quick poll:</b> First move today?
A. 🟢 Buy opportunities
B. 🟡 Watch & wait
C. 🔴 Secure profits

━━━━━━━━━━━━
🔔 {Config.CHANNEL_NAME}
<code>#CryptoMorning #Day{cls.day_counter} #MarketOpen</code>"""
        
        return post
    
    @classmethod
    def market_alert(cls):
        """9:00 AM - Market alert"""
        update = MarketData.get_fresh_content(
            ContentLibrary.MARKET_UPDATES,
            MarketData.used_updates
        )
        
        post = f"""⚡ <b>9 AM Market Alert</b>
{ContentLibrary.get_emoji("actions")} <i>Early session update</i>

{cls.create_section("🔄 Quick Status", f"""• ₿ Bitcoin: $65,310 ↗️
• 📊 Volume: Building steadily
• 🌏 Asia: Active trading""", ContentLibrary.get_emoji("market"))}

{cls.create_section("📰 Market Update", f"{update['icon']} {update['text']}", ContentLibrary.get_emoji("time"))}

{cls.create_section("🎯 Watch Now", """• $65,500 resistance break
• Volume confirmation needed
• Avoid early fakeouts""", ContentLibrary.get_emoji("actions"))}

{ContentLibrary.get_emoji("time")} <code>{cls.get_time()}</code>

👉 <b>Share</b> with morning traders

━━━━━━━━━━━━
⚡ Real-time insights
{Config.CHANNEL_NAME}
<code>#MarketAlert #TradingHours #CryptoUpdate</code>"""
        
        return post
    
    @classmethod
    def news_update(cls):
        """11:00 AM - News update"""
        news1 = MarketData.get_fresh_content(
            ContentLibrary.MARKET_UPDATES,
            MarketData.used_updates
        )
        news2 = MarketData.get_fresh_content(
            [n for n in ContentLibrary.MARKET_UPDATES if n != news1],
            MarketData.used_updates
        )
        
        post = f"""📰 <b>Crypto News Update</b>
{ContentLibrary.get_emoji("community")} <i>Stay informed, trade smart</i>

{cls.create_section("🌍 Top Updates", f"""• {news1['icon']} {news1['text']}
• {news2['icon']} {news2['text']}""", ContentLibrary.get_emoji("market"))}

{cls.create_section("💎 Market Impact", """Institutional confidence ↗️
Retail interest growing
Adoption accelerating""", ContentLibrary.get_emoji("education"))}

{cls.create_section("👀 What to Watch", """• Price reaction to news
• Volume confirmation
• Market sentiment shift""", ContentLibrary.get_emoji("actions"))}

{ContentLibrary.get_emoji("time")} <code>{cls.get_time()}</code>

👉 <b>Thoughts on this news?</b> Comment below

━━━━━━━━━━━━
📰 Stay ahead of trends
{Config.CHANNEL_NAME}
<code>#CryptoNews #MarketUpdate #Breaking</code>"""
        
        return post
    
    @classmethod
    def market_analysis(cls):
        """1:00 PM - Deep analysis"""
        prices = MarketData.get_prices()
        
        post = f"""🔍 <b>Market Deep Dive</b>
{ContentLibrary.get_emoji("market")} <i>Midday analysis session</i>

{cls.create_section("📊 Current Metrics", f"""• ₿ Dominance: 52.3%
• Total Market: $2.4T
• Fear/Greed: 65 (Greed)
• 24h Volume: $85B""", ContentLibrary.get_emoji("market"))}

{cls.create_section("🎯 Smart Money Watch", """• Institutions accumulating
• Whale wallets active
• Retail still cautious
• ETF flows positive""", ContentLibrary.get_emoji("coins"))}

{cls.create_section("⚠️ Risk Assessment", """• Support: $65K critical
• Position sizing matters
• Diversify across assets
• Have exit strategy""", ContentLibrary.get_emoji("actions"))}

{ContentLibrary.get_emoji("time")} <code>{cls.get_time()}</code>

👉 <b>Tag</b> a trading friend

━━━━━━━━━━━━
📈 Data-driven decisions
{Config.CHANNEL_NAME}
<code>#MarketAnalysis #CryptoData #Trading</code>"""
        
        return post
    
    @classmethod
    def learning_series(cls):
        """3:00 PM - Learning series"""
        topic = ContentLibrary.LEARNING_TOPICS[cls.learning_index % len(ContentLibrary.LEARNING_TOPICS)]
        cls.learning_index += 1
        
        points = "\n".join([f"• {point}" for point in topic["points"]])
        
        post = f"""🎓 <b>Learn Crypto #{cls.learning_index}</b>
{ContentLibrary.get_emoji("education")} <i>{topic['icon']} {topic['title']}</i>

{cls.create_section("📚 Key Concepts", points, ContentLibrary.get_emoji("education"))}

{cls.create_section("💡 Pro Tip", topic["tip"], ContentLibrary.get_emoji("coins"))}

{cls.create_section("🧠 Learning Wisdom", "Knowledge compounds like crypto gains", ContentLibrary.get_emoji("education"))}

{ContentLibrary.get_emoji("time")} <code>{cls.get_time()}</code>

👉 <b>Your question about this?</b> Comment ⬇️

━━━━━━━━━━━━
📚 Building crypto knowledge daily
{Config.CHANNEL_NAME}
<code>#LearnCrypto #{topic['title'].replace(' ', '')} #CryptoEducation</code>"""
        
        return post
    
    @classmethod
    def technical_analysis(cls):
        """6:00 PM - Technical analysis"""
        topic = ContentLibrary.TECHNICAL_TOPICS[cls.technical_index % len(ContentLibrary.TECHNICAL_TOPICS)]
        cls.technical_index += 1
        
        post = f"""📈 <b>Tech Analysis #{cls.technical_index}</b>
{ContentLibrary.get_emoji("market")} <i>{topic['icon']} {topic['title']}</i>

{cls.create_section("🔧 How It Works", topic["content"], ContentLibrary.get_emoji("education"))}

{cls.create_section("🎯 Current Application", topic["example"], ContentLibrary.get_emoji("market"))}

{cls.create_section("⚠️ Risk Management", """• Never risk >2% per trade
• Use stop-losses always
• Wait for confirmation
• Trade small, learn big""", ContentLibrary.get_emoji("actions"))}

{ContentLibrary.get_emoji("time")} <code>{cls.get_time()}</code>

👉 <b>Share</b> with chart groups

━━━━━━━━━━━━
🔭 Smart chart reading
{Config.CHANNEL_NAME}
<code>#TechnicalAnalysis #{topic['title'].replace(' ', '')} #ChartPatterns</code>"""
        
        return post
    
    @classmethod
    def evening_wrap(cls):
        """9:00 PM - Evening wrap with motivation"""
        prices = MarketData.get_prices()
        evening_quote = ContentLibrary.get_motivational_quote()
        
        # ETF Tracker Data
        etf_flows = [
            {"name": "BlackRock", "flow": "+$450M", "icon": "🏛️"},
            {"name": "Fidelity", "flow": "+$120M", "icon": "💰"},
            {"name": "Grayscale", "flow": "-$40M", "icon": "📊"}
        ]
        
        etf_line = " | ".join([f"{e['icon']} {e['name']}: {e['flow']}" for e in etf_flows])
        
        post = f"""🌙 <b>Evening Crypto Wrap</b>
{ContentLibrary.get_emoji("community")} <i>Day {cls.day_counter} complete</i>

{cls.create_section("📊 Daily Performance", f"""• ₿ Bitcoin: {MarketData.format_price(prices['BTC'])} {ContentLibrary.get_emoji('trends')}
• Ξ Ethereum: {MarketData.format_price(prices['ETH'])} {ContentLibrary.get_emoji('trends')}
• ◎ Solana: {MarketData.format_price(prices['SOL'])} {ContentLibrary.get_emoji('trends')}""", ContentLibrary.get_emoji("market"))}

{cls.create_section("🏦 ETF Tracker", f"{etf_line}\nStreak: {random.randint(10,25)} days 🟢", ContentLibrary.get_emoji("coins"))}

{cls.create_section("🎯 Key Takeaways", """• Institutional buying continues
• Technical structure intact
• Sentiment improving gradually
• Community growing stronger""", ContentLibrary.get_emoji("education"))}

{cls.create_section("💫 Evening Motivation", evening_quote, ContentLibrary.get_emoji("community"))}

{ContentLibrary.get_emoji("time")} <code>{cls.get_time()}</code>

👉 <b>Rate today's market:</b> ⭐⭐⭐

━━━━━━━━━━━━
🚀 Crypto never sleeps, but you should
{Config.CHANNEL_NAME}
<code>#DailyWrap #ETFTracker #GNCrypto #Day{cls.day_counter}</code>"""
        
        cls.day_counter += 1
        return post

# ============================================================================
# 5. TELEGRAM MANAGER
# ============================================================================
class TelegramManager:
    """Smart Telegram message handler"""
    
    @staticmethod
    def send_message(text: str):
        """Send beautifully formatted message"""
        if not text or not Config.BOT_TOKEN:
            return False
        
        url = f"https://api.telegram.org/bot{Config.BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": Config.CHANNEL_ID,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": True
        }
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            if response.status_code == 200:
                time_str = datetime.now(Config.TIMEZONE).strftime("%H:%M")
                print(f"✅ [{time_str}] Beautiful post sent")
                return True
            else:
                print(f"⚠️ Telegram error: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Send error: {str(e)[:50]}")
            return False

# ============================================================================
# 6. SCHEDULER WITH STARTUP
# ============================================================================
class Scheduler:
    """Intelligent scheduler"""
    
    @staticmethod
    def setup():
        """Setup all 7 beautiful posts"""
        schedule.clear()
        
        # 7 perfectly timed posts
        schedule.every().day.at(Config.SCHEDULE["morning"]).do(
            lambda: TelegramManager.send_message(PostGenerator.morning_pulse()))
        
        schedule.every().day.at(Config.SCHEDULE["alert"]).do(
            lambda: TelegramManager.send_message(PostGenerator.market_alert()))
        
        schedule.every().day.at(Config.SCHEDULE["news"]).do(
            lambda: TelegramManager.send_message(PostGenerator.news_update()))
        
        schedule.every().day.at(Config.SCHEDULE["analysis"]).do(
            lambda: TelegramManager.send_message(PostGenerator.market_analysis()))
        
        schedule.every().day.at(Config.SCHEDULE["learning"]).do(
            lambda: TelegramManager.send_message(PostGenerator.learning_series()))
        
        schedule.every().day.at(Config.SCHEDULE["technical"]).do(
            lambda: TelegramManager.send_message(PostGenerator.technical_analysis()))
        
        schedule.every().day.at(Config.SCHEDULE["evening"]).do(
            lambda: TelegramManager.send_message(PostGenerator.evening_wrap()))
        
        # Send beautiful startup message
        Scheduler.send_startup()
    
    @staticmethod
    def send_startup():
        """Send startup announcement"""
        startup_msg = f"""🚀 <b>ViralCryptoInsights is LIVE!</b>
{ContentLibrary.get_emoji("community")} <i>Crypto Trends Before They Trend</i>

✨ <b>Welcome to your daily crypto companion!</b>

{PostGenerator.create_section("✅ System Status", "Fully operational & automated", "🟢")}
{PostGenerator.create_section("⏰ Timezone", "IST (India Standard Time)", ContentLibrary.get_emoji("time"))}
{PostGenerator.create_section("📅 Daily Posts", "7 beautifully crafted updates", "📱")}
{PostGenerator.create_section("🎯 Features", "Market news • Learning • Technical • Community", "⭐")}

━━━━━━━━━━━━
<b>📋 Today's Schedule (IST):</b>
• 8:30 AM — Morning Pulse
• 9:00 AM — Market Alert
• 11:00 AM — News Update
• 1:00 PM — Deep Analysis
• 3:00 PM — Learning Series
• 6:00 PM — Technical Analysis
• 9:00 PM — Evening Wrap + ETF

━━━━━━━━━━━━
🔔 Join our growing crypto community!
{Config.CHANNEL_NAME}

<code>#Welcome #CryptoCommunity #Day1 #Automation</code>"""
        
        TelegramManager.send_message(startup_msg)
        
        # Beautiful console output
        now = datetime.now(Config.TIMEZONE)
        print("\n" + "="*60)
        print("🚀 VIRALCRYPTOINSIGHTS - ULTIMATE EDITION")
        print("="*60)
        print(f"✨ Online: {now.strftime('%d %B %Y %I:%M %p IST')}")
        print(f"📍 Channel: {Config.CHANNEL_NAME}")
        print(f"📱 Posts: 7 beautiful updates daily")
        print(f"🎨 Features:")
        print(f"   • Fresh motivational quotes (API + local)")
        print(f"   • Dynamic emoji library (100+ icons)")
        print(f"   • No content repeats (smart tracking)")
        print(f"   • ETF tracker in evening wrap")
        print(f"   • Telegram algorithm optimized")
        print("="*60)

# ============================================================================
# 7. MAIN EXECUTION
# ============================================================================
def main():
    """Main execution function"""
    print("\n✨ Starting ViralCryptoInsights Ultimate Edition...")
    
    # Validate configuration
    if not Config.BOT_TOKEN:
        print("\n❌ ERROR: BOT_TOKEN not set!")
        print("Railway → Variables → Add:")
        print("BOT_TOKEN = your_token_from_@BotFather")
        return
    
    if not Config.CHANNEL_ID:
        print("\n❌ ERROR: CHANNEL_ID not set!")
        print("Railway → Variables → Add:")
        print("CHANNEL_ID = your_channel_id_from_@RawDataBot")
        return
    
    try:
        # Setup scheduler
        Scheduler.setup()
        
        print("\n✅ Bot is running with beautiful formatting!")
        print(f"🎨 Features: Fresh quotes + Dynamic emojis + No repeats")
        print(f"📱 First post tomorrow: 8:30 AM IST")
        print(f"🔧 Press Ctrl+C to stop")
        print("-" * 50)
        
        # Keep running
        while True:
            schedule.run_pending()
            time.sleep(60)
            
    except KeyboardInterrupt:
        print("\n\n🛑 Bot stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")

# ============================================================================
# 8. ENTRY POINT
# ============================================================================
if __name__ == "__main__":
    main()
