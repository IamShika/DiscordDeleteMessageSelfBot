import json
import asyncio
import discord
from discord.ext import commands

# Load config initially
with open("config.json", "r") as f:
    config = json.load(f)

# Assign config values
TOKEN = config["token"]
TARGET_GUILD_ID = config["guild_id"]
SCAM_KEYWORDS = config["scam_keywords"]
BLOCKED_USER_IDS = set(config["blocked_user_ids"])
BLOCKED_CHANNEL_IDS = set(config["blocked_channel_ids"])
ACTIVE = config["active"]
IGNORE_SELF = config.get("ignore_self", True)
SCAN_ON_STARTUP = config.get("scan_on_startup", False)

# Function to reload config file
def reload_config():
    global config, TOKEN, TARGET_GUILD_ID, SCAM_KEYWORDS, BLOCKED_USER_IDS, BLOCKED_CHANNEL_IDS, ACTIVE, IGNORE_SELF, SCAN_ON_STARTUP

    with open("config.json", "r") as f:
        config = json.load(f)

    TOKEN = config["token"]
    TARGET_GUILD_ID = config["guild_id"]
    SCAM_KEYWORDS = config["scam_keywords"]
    BLOCKED_USER_IDS = set(config["blocked_user_ids"])
    BLOCKED_CHANNEL_IDS = set(config["blocked_channel_ids"])
    ACTIVE = config["active"]
    IGNORE_SELF = config.get("ignore_self", True)
    SCAN_ON_STARTUP = config.get("scan_on_startup", False)

    print("[🔁] Config reloaded.")

# Bot setup
bot = commands.Bot(command_prefix="!", self_bot=True)

# Function to scan past messages
async def scan_past_messages():
    print("[🔍] Scanning recent messages for scams...")
    guild = bot.get_guild(TARGET_GUILD_ID)
    if not guild:
        print("[!] Couldn't find the target guild.")
        return

    for channel in guild.text_channels:
        try:
            async for message in channel.history(limit=100):  # Adjust limit as needed
                if IGNORE_SELF and message.author.id == bot.user.id:
                    continue
                if message.author.id in BLOCKED_USER_IDS or message.channel.id in BLOCKED_CHANNEL_IDS:
                    continue
                if any(keyword.lower() in message.content.lower() for keyword in SCAM_KEYWORDS):
                    await message.delete()
                    print(f"[🗑️] Deleted (past) in #{channel.name} - {message.author}: {message.content}")
        except Exception as e:
            print(f"[!] Could not read #{channel.name}: {e}")

@bot.event
async def on_ready():
    print(f"[✓] Logged in as: {bot.user}")
    print(f"[✓] Monitoring server ID: {TARGET_GUILD_ID}")
    print(f"[✓] Ignore self: {IGNORE_SELF}")
    print(f"[✓] Active: {ACTIVE}")
    print(f"[✓] Scan on startup: {SCAN_ON_STARTUP}")
    
    if SCAN_ON_STARTUP:
        await scan_past_messages()

@bot.event
async def on_message(message):
    global ACTIVE

    if IGNORE_SELF and message.author.id == bot.user.id:
        return

    if message.content.lower() == "!botpause" and message.author.id == bot.user.id:
        ACTIVE = False
        print("[⏸️] Bot is paused.")
        return

    if message.content.lower() == "!botresume" and message.author.id == bot.user.id:
        ACTIVE = True
        print("[▶️] Bot resumed.")
        return

    if message.content.lower() == "!reloadconfig" or message.content.lower() == "!botrefresh" or message.content.lower() == "!botreload" and message.author.id == bot.user.id:
        reload_config()
        await message.channel.send("🔁 Config reloaded.")
        return

    if message.content.lower() == "!scanpast" or message.content.lower() == "!botscan" and message.author.id == bot.user.id:
        await scan_past_messages()
        await message.channel.send("🔍 Past messages scanned.")
        return

    if not ACTIVE:
        return

    if not message.guild or message.guild.id != TARGET_GUILD_ID:
        return

    if message.author.id in BLOCKED_USER_IDS or message.channel.id in BLOCKED_CHANNEL_IDS:
        return

    if any(keyword.lower() in message.content.lower() for keyword in SCAM_KEYWORDS):
        try:
            await message.delete()
            print(f"[🗑️] Deleted in '{message.guild.name}' - {message.author}: {message.content}")
        except Exception as e:
            print(f"[!] Failed to delete message: {e}")

# Run bot
bot.run(TOKEN)
