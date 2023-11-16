import discord
from discord.ext import commands

intents = discord.Intents.default() 
intents.message_content = True


bot = commands.Bot(command_prefix='#',intents=discord.Intents.all())
 
@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
 
@bot.command("마")
async def hello(message):
    await message.channel.send('어어 왔나')

@bot.command("입장")
async def join(ctx):
		if ctx.author.voice and ctx.author.voice.channel:
			channel = ctx.author.voice.channel
			await channel.connect()
		else:
			await ctx.send("음성 채널이 존재하지 않습니다.")

bot.run('MTE2ODQ1OTEwNTk1NDk2NzYwNQ.GHDBjp.xoXzbgGCCFf0oWtD8nQH1vuwB_Ua2-FSGoigZg')