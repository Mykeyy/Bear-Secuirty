import discord
from discord.ext import commands
from discord import app_commands  # Import app_commands for slash commands
import os
from dotenv import load_dotenv  # Import load_dotenv to read .env file
import time  # Import time module to track uptime

# Load environment variables from .env file
load_dotenv()

# Get the token from the .env file
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up the bot with intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Track the bot's start time
start_time = time.time()

@bot.event
async def on_ready():
    # Set the bot's status to "idle" while "watching" "Yua's Cove"
    await bot.change_presence(
        status=discord.Status.idle,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="Yua's Cove"
        )
    )
    print(f'{bot.user.name} has connected to Discord!')
    try:
        synced = await bot.tree.sync()  # Sync slash commands
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# Modify the /ping command to include latency and uptime
@bot.tree.command(name="ping", description="Ping the bot API and check latency and uptime.")
async def ping(interaction: discord.Interaction):
    # Calculate latency in milliseconds
    latency = round(bot.latency * 1000)  # bot.latency is in seconds

    # Calculate uptime
    current_time = time.time()
    uptime_seconds = int(current_time - start_time)
    uptime_hours, remainder = divmod(uptime_seconds, 3600)
    uptime_minutes, uptime_seconds = divmod(remainder, 60)

    # Create an embed with latency and uptime
    embed = discord.Embed(
        title="🏓 Pong!",
        description="The bot API is responsive!",
        color=discord.Color.from_str("#3e5fc0")  # Blue color
    )
    embed.add_field(name="Latency", value=f"{latency} ms", inline=False)
    embed.add_field(name="Uptime", value=f"{uptime_hours}h {uptime_minutes}m {uptime_seconds}s", inline=False)
    embed.set_footer(text="Bear Sec Bot | Powered by Yua's Cove")
    await interaction.response.send_message(embed=embed)

# Add a slash command for /bear
@bot.tree.command(name="bear", description="Check if the bot is working.")
async def bear(interaction: discord.Interaction):
    await interaction.response.send_message("Hi, I am working! 🐻‍❄️")

# Run the bot with your token
if TOKEN:
    bot.run(TOKEN)
else:
    print("Error: DISCORD_TOKEN is not set in the .env file.")