import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import datetime

client = commands.Bot(command_prefix = 'h-')
client.remove_command("help")
players = {}

@client.event
async def on_ready():
    print("■■■■■■■■■■■■■■■[ I  N  F  O ]■■■■■■■■■■■■■■■")
    print("")
    print(">> TEAM. Empty | Discord Bot PROJECT")
    print("")
    print("■■■■■■■■■■■■■■■[ I  N  F  O ]■■■■■■■■■■■■■■■")
    print("")
    print("[INFO] Bot Commands Loading..")
    print("")
    print("■■■■■■■■■■■■■■■[ I  N  F  O ]■■■■■■■■■■■■■■■")
    game = discord.Game("h-help를 입력해보세요!")
    await client.change_presence(status=discord.Status.online, activity=game)

# Commands : Normal
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
            title="HI-FI QuadDAC HELP",
            description="★ 기본 접두사 : **h-**\n★ 현재 버전 : **1.0**\n\n==============================\n\n모든 명령어를 볼려면 **[여기](http://teamempty.dothome.co.kr)**를 클릭해주세요!",
            color=0xffff00
        )
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def 생활정보(ctx):
    embed = discord.Embed(
            title="생 활 정 보",
            description="**[전국날씨](https://search.naver.com/search.naver?ie=UTF-8&query=%EC%A0%84%EA%B5%AD%EB%82%A0%EC%94%A8&sm=chr_hty)**,**[준비중입니다]**",
            color=0x00ffff
        )
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def info(ctx):
    embed = discord.Embed(
            title="Bot Running Information",
            description="현재 돌아가고 있는곳 :\nㄴ Lenovo K3 Note(with MIUI)에서 구동 중\n\n프로그래밍 언어 :\nㄴ Python 3.6.2",
            color=0xffff00
        )
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def botinfo(ctx):
    bid = client.user.id
    embed = discord.Embed(
            title="Bot Information",
            description="**봇 ID** : " + str(bid) + "\n**봇 업타임** : 알수 없음\n**봇 소유자** : ClickToREturns(깃허브 참고)\n**업데이트 간격** : 그런거 몰라요, 깃허브 보세요",
            color=0xffff00
        )
    await ctx.send(embed=embed)

# Commands : Game
@client.command(pass_context=True)
async def 가위(ctx):
    str = ['가위','바위','보']
    r = random.choice(str)
    if r == '가위':
        await ctx.send("음 저는요.. : " + r + "\n> **저랑 비긴거 같아요**")
    elif r == '바위':
        await ctx.send("음 저는요.. : " + r + "\n> **제가 졌네요..!**")
    elif r == '보':
        await ctx.send("음 저는요.. : " + r + "\n> **제가 이겼네요!**")

@client.command(pass_context=True)
async def 바위(ctx):
    str = ['가위','바위','보']
    r = random.choice(str)
    if r == '가위':
        await ctx.send("음 저는요.. : " + r + "\n> **제가 졌네요..!**")
    elif r == '바위':
        await ctx.send("음 저는요.. : " + r + "\n> **저랑 비긴거 같아요**")
    elif r == '보':
        await ctx.send("음 저는요.. : " + r + "\n> **제가 이겼네요!**")

@client.command(pass_context=True)
async def 보(ctx):
    str = ['가위','바위','보']
    r = random.choice(str)
    if r == '가위':
        await ctx.send("음 저는요.. : " + r + "\n> **제가 이겼네요!**")
    elif r == '바위':
        await ctx.send("음 저는요.. : " + r + "\n> **제가 졌네요..!**")
    elif r == '보':
        await ctx.send("음 저는요.. : " + r + "\n> **저랑 비긴거 같아요**")

client.run('NjExMzg1ODUzOTMwODk3NDE5.XVfSJw.DyHTndlWPrJ5HYz1bTqShfH_KyI')
