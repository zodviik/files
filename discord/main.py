from config import token
import discord, os, asyncio
from discord.ext import commands


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

ban_words = {"hello", "ban","word"}

@bot.event
async def on_ready():
    print("!")



@bot.command()
async def start(ctx:commands.context.Context):
    author = ctx.message.author
    await ctx.send(author.mention)



@bot.command()
async def timer(ctx:commands.context.Context, arg="60"):
    try:
        arg = int(arg)
        await ctx.send(f"Таймер на {arg} секунд установлен")
        await asyncio.sleep(arg)
        await ctx.send("Время вышло")
    except ValueError:
        await ctx.send("Неправильное число")
        await ctx.send_help()



@bot.command()
async def clear(ctx:commands.context.Context, arg=100):
    if ctx.message.author.guild_permissions.administrator:
        await ctx.channel.purge(limit=arg)
    else:
        await ctx.send("Недостаточно прав)")

@bot.command()
async def mute(ctx:commands.context.Context, member:discord.member.Member, arg=300):
    mute = discord.utils.get(ctx.guild.roles, name="mute")
    unmute = discord.utils.get(ctx.guild.roles, name="unmute")
    if ctx.message.author.guild_permissions.administrator:
        await member.add_roles(mute)
        await member.remove_roles(unmute)
        await ctx.send(f"{member.mention} был замьючен на {arg} секунд")
        await asyncio.sleep(arg)
        await member.add_roles(unmute)
        await member.remove_roles(mute)
        await ctx.send(f"{member.mention} был размьючен")
    else:
        await ctx.send("Недостаточно прав)")
    

@bot.command()
async def unmute(ctx:commands.context.Context, member:discord.member.Member):
    mute = discord.utils.get(ctx.guild.roles, name="mute")
    unmute = discord.utils.get(ctx.guild.roles, name="unmute")
    if ctx.message.author.guild_permissions.administrator:
        await member.add_roles(unmute)
        await member.remove_roles(mute)
        await ctx.send(f"{member.mention} был размьючен")



@bot.command()
async def message(ctx:commands.context.Context, member:discord.Member,*, arg):
    await member.send(arg)
    

@bot.event
async def on_message(ctx:discord.message.Message):
    
    if ban_words & set(ctx.content.lower().split()):
        await ctx.channel.send("Это писать нельзя!")
        await ctx.delete()
    await bot.process_commands(ctx)



@bot.event
async def on_member_join(ctx:discord.member.Member):
    for channel in bot.get_guild(ctx.guild.id).channels:
        if channel.name == "bots":
            unmute = discord.utils.get(ctx.guild.roles, name="unmute")
            await ctx.add_roles(unmute)
            await bot.get_channel(channel.id).send(f"Приветствуем на сервере {ctx.mention}")
            



@bot.event
async def on_member_remove(ctx:discord.member.Member):
    for channel in bot.get_guild(ctx.guild.id).channels:
        if channel.name == "bots":
            await bot.get_channel(channel.id).send(f"Пока! {ctx.mention}")



bot.run(token)