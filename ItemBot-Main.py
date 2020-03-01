import requests
import discord
from discord.ext import commands
import pymysql

itembot = commands.Bot(command_prefix='.')
TOKEN = open(local file with token).read()
db_info = pymysql.connect(connection stuff)
cursor = db_info.cursor()
sql_query = 'SELECT * FROM ror2_items'


# Playing Message
@itembot.event
async def on_ready():
    print('Ready!')
    await itembot.change_presence(status=discord.Status.online, activity=discord.Game('Risk of Rain 2'))


#find command, looks up items for ror2 on a database server
@itembot.command()
async def find(ctx, *, question):
    sql_query = 'SELECT * FROM item_list'
    cursor.execute(sql_query)
    results = cursor.fetchall()
    for row in results:
        if question in row:
            row[0]
            row[1]
            row[2]
            row[3]
            if row[2] == 'white':
                embedw = discord.Embed(
                 title=row[0],
                    description=row[1],
                    color=discord.Color.lighter_grey()
                )
                embedw.set_thumbnail(url=row[3])
                await ctx.send(embed=embedw)
            elif row[2] == 'uncommon':
                embed_un = discord.Embed(
                    title=row[0],
                    description=row[1],
                    color=discord.Color.green()
                )
                embed_un.set_thumbnail(url=row[3])
                await ctx.send(embed=embed_un)
            elif row[2] == 'Legendary':
                embed_leg = discord.Embed(
                    title=row[0],
                    description=row[1],
                    color=discord.Color.red()
                )
                embed_leg.set_thumbnail(url=row[3])
                await ctx.send(embed=embed_leg)
            elif row[2] == 'Boss':
                embed_boss = discord.Embed(
                    title=row[0],
                    description=row[1],
                    color=discord.Color.lighter_yellow()
                )
                embed_boss.set_thumbnail(url=row[3])
                await ctx.send(embed=embed_boss)
            elif row[2] == 'Lunar':
                embed_lun = discord.Embed(
                    title=row[0],
                    description=row[1],
                    color=discord.Color.blue()
                )
                embed_lun.set_thumbnail(url=row[3])
                await ctx.send(embed=embed_lun)
            elif row[2] == 'Equipment':
                embed_eq = discord.Embed(
                    title=row[0],
                    description=row[1],
                    color=discord.Color.blue()
                )
                embed_eq.set_thumbnail(url=row[3])
                await ctx.send(embed=embed_eq)
            else:
                await ctx.semd('Error')


@itembot.command()
async def ping(ctx):
    embed = discord.Embed(
        title='Latency',
        description= f'Latency: {round(itembot.latency * 1000)}ms',
        color=discord.Color.green()
    )
    image=open('connectivity.jpg', 'rb').read()
    embed.set_author(name='', icon_url='https://datacenternews.asia/uploads/story/2016/08/18/ThinkstockPhotos-579142910.jpg')
    await ctx.send(embed=embed)

itembot.run(TOKEN)
