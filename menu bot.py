import discord
import random

client = discord.Client()

@client.event
async def on_message(message):
    list1 = ['한식','중식','양식','일식']
    list2 = ['치킨','피자','햄버거','냉면','돈가스','찜닭','초밥','회','삼겹살','떡볶이','마라탕',
    '짜장면','짬뽕','칼국수']
    list3 = ['피자','햄버거','파스타']
    list4 = ['맥도날드','버거킹','롯데리아','맘스터치','노브랜드버거']
    list5 = ['BBQ(황금올리브)','교촌치킨(허니콤보)','처가집(슈프림)','굽네치킨(갈비천왕)',
    '굽네치킨(고추바사삭)','지코바(양념숯불)','푸라닭(블랙알리오)','푸라닭(맛초킹)',
    'BHC(뿌링클)','BHC(맛초킹)','60계치킨(고추치킨)','호식이두마리(간장양념)',
    '또래오래(오곡후라이드)','자담치킨']

    food = random.choice(list1)
    menu = random.choice(list2)
    western_food = random.choice(list3)
    buger = random.choice(list4)
    chicken = random.choice(list5)

    if message.author == client.user:
        return
    
    if message.content.startswith("!메뉴"):
        await message.channel.send(menu)

    if message.content.startswith("!음식"):
        await message.channel.send(food)
    
    if message.content.startswith("!양식"):
        await message.channel.send(western_food)

    if message.content.startswith("!햄버거"):
        await message.channel.send(buger)

    if message.content.startswith("!치킨"):
        await message.channel.send(chicken)

client.run("ODc3MDM2MDQ0NTE4ODQ2NTM1.YRsxdw.mVrW3EVU7QNeKgcftDpdaRKLg1Q")