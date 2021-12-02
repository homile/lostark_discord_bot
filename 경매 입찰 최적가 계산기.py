# a_gold = 경매가(입력값) x 0.95 x (파티원수-1)(입력값) / (파티원수)(입력값)
# 명령어 : !분배금 8인 거래소최소가격

import discord
from discord.ext import commands
import random
# import requests
# from bs4 import BeautifulSoup

client = discord.Client()
client = commands.Bot(command_prefix='!!')

# 인사말
@client.command(aliases=['안녕', '안녕하세요', 'ㅎㅇ'])
async def hello(ctx):
    await ctx.send('안녕하세요')


# 도움말
@client.command(aliases=['명령어', '도움'])
async def 도움말(ctx) :
    embed = discord.Embed(title = "도움말",
    description = "호밀이의 봇 제작 21.10.16.", color = 0x62c1cc)
    embed.add_field(name = "!!도움", value = "뭘봐 봇의 도움말을 알려줍니다.")
    embed.add_field(name = "!!분배금"
    , value = "보스 클리어 경매시 입찰 최적가를 알 수 있습니다.\n`!!분배금 파티원수 경매장최소가` "
    , inline=False)
    embed.add_field(name = "!!메뉴"
    , value = "메뉴를 추천해줍니다.\n`!!메뉴`, `!!음식`, `!!양식`, `!!햄버거`, `!!치킨` "
    , inline=False)
    embed.add_field(name = "추가 예정"
    , value = "현재 작업중이며 추가 예정 기능\n`캐릭터 검색`, `원정대 주간 수익`"
    , inline=False)
    # embed.set_footer(text = "푸터에 넣을 내용")
    await ctx.send(embed = embed)


# 경매 최적골드 계산기
@client.command()
async def 분배금(ctx, *price_party:int):
    # 입력받는 리스트
    party = price_party[0]          # 파티원수
    auction_price = price_party[1]  # 거래소 최저가

    Commission = int(auction_price * 0.95)          # 5% 수수료 제외 지급골드
    a_gold = int(Commission * (party-1) / party)    # 이득 입찰가
    Distribution = int(a_gold / (party - 1))        # 개인 분배금
    Net_Income = Commission - a_gold                # 순이익
    
    total = '입찰최적가 : ' + str(a_gold) + ' | 분배금 : ' + str(Distribution) + ' | 순이익 : ' + str(Net_Income)
    await ctx.send(total)


client.run("ODc3MDM2MDQ0NTE4ODQ2NTM1.YRsxdw.mVrW3EVU7QNeKgcftDpdaRKLg1Q")