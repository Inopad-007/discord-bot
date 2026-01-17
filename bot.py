import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)

GUILD_ID = discord.Object(id=1426251354187370596)  # ID e serverit

@bot.event
async def on_ready():
    await bot.tree.sync(guild=GUILD_ID)
    print(f"Bot-i u lidh si {bot.user}")


    
# 🔹 SLASH COMMAND /about
@bot.tree.command(
    name="about",
    description="Tregon informacione rreth botit",
    guild=GUILD_ID
)
async def about(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🤖 **Un jam boti Inopad**\n"
        "Jam krijuar per t'ju ndihmuar ne server.\n"
        "Version: 1.0"
    )
    
    intents = discord.Intents.default()
intents.message_content = True

@bot.command()
async def hello(ctx):
    await ctx.send("Pershendetje! 🫡")

@bot.command()
async def ping(ctx):
    await ctx.send('pong🏓')

@bot.command()
async def inopad(ctx):
    await ctx.send('ca do re') 


bot.run("MTQ2MTYwMTk2MDQxODQ3NjA3Mg.Gb4Ofy.CwpWsVH-TP6OEMAqrrVYLHIQS-oNl5Hs1UpdX0")
