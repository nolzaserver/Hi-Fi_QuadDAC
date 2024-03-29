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
    bid = client.user.id
    embed = discord.Embed(
            title="[ 도움말 ] :: [ ** 봇 ID : " + str(bid) + "** ]",
            description="★ 기본 접두사 : **h-**\n★ 현재 버전 : **BETA Service Mode**\n\n==============================\n\n모든 명령어를 볼려면 **[여기](http://teamempty.dothome.co.kr)**를 클릭해주세요!",
            color=0x99ccff
        )
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def 생활정보(ctx):
    embed = discord.Embed(
            title="생 활 정 보",
            description="**[전국날씨](https://search.naver.com/search.naver?ie=UTF-8&query=%EC%A0%84%EA%B5%AD%EB%82%A0%EC%94%A8&sm=chr_hty)**,**[준비중입니다]**",
            color=0x99ffff
        )
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def info(ctx):
    embed = discord.Embed(
            title="Bot Running Information",
            description="현재 돌아가고 있는곳 :\nㄴ 개발자 노트북에서 구동 중..\n\n프로그래밍 언어 :\nㄴ Python 3.7.0",
            color=0xffff00
        )
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def partner(ctx):
    embed = discord.Embed(
            title="**TEAM. EMPTY** Parner Server",
            description="★ 파란색 글씨를 클릭시 접속됩니다.\n\n[대서 홍보방](https://discord.gg/yjq4mTv) - 자유 홍보서버(개발자 추천)\n**[ 새로운 파트너 모집중입니다 ]**",
            color=0x99ff99
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

client.run('token')
