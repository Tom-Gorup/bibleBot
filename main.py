import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os
from bible import Bible
from basicfunctions import BasicFunctions
import random

load_dotenv()

my_secret = os.environ['DISCORD_TOKEN']
test_discord_channel = int(os.environ['TEST_DISCORD_CHANNEL'])
# bible_study_channel = int(os.environ['BIBLE_STUDY_CHANNEL'])

description = '''The CryptoBot personal assistant. Start with `@CryptoBot help` to get started'''
bot = commands.Bot(command_prefix=commands.when_mentioned, description=description)


@tasks.loop(hours=22)  # task runs every 22 hour
async def my_background_task():
    channel = bot.get_channel(test_discord_channel)  # channel ID goes here
    # channel = bot.get_channel(cryptotalk_discord_channel)  # channel ID goes here
    basicfunction = BasicFunctions()


@bot.event
async def on_ready():
    my_background_task.start()
    print('Logged in as %s (%s)' % (bot.user.name, bot.user.id))


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


@bot.command(pass_context=True)
async def verse(ctx, *, verse: str):
    """I will tell you the price for the coin you ask for. Note, I'm currenlty only integrated into Coinbase. So it
    must be listed and being sold there for me to provide the value. Looking to add more exchanges soon!"""
    bible = Bible()
    passage = bible.get_esv_text(verse)

    await ctx.send(passage)

bot.run(my_secret)