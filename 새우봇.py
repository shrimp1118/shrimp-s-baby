from functools import total_ordering
from time import sleep
import discord
import random
import time
import threading
import pymysql

client = discord.Client()

@client.event
async def on_ready(): 
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드봇 이름:" + client.user.name)
    print("디스코드봇 ID:" + str(client.user.id))
    print("디스코드봇 버전:" + str(discord.__version__))
    print('------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("리뉴얼 되어 돌아온 새우새우 도박봇"))
