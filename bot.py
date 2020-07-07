import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

Bot = commands.Bot (command_prefix='!')
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)

client = gspread.authorize(creds)


#col = sheet.col_values(2)

@Bot.event
async def on_ready():
    print("Bot is online")

@Bot.command(pass_context=True)
async def start(ctx):
    role = ctx.message.guild.get_role(729285717628420106)
    await ctx.message.delete() 
    if role in ctx.message.author.roles:
        ctx1 = await ctx.send("Присутствующие")
        await ctx1.add_reaction("☑️")
        await asyncio.sleep(10)
        ctx1 = await ctx1.channel.fetch_message(ctx1.id)
        for reaction in ctx1.reactions:
            if reaction.emoji == "☑️":
                positive = reaction
        users = await positive.users().flatten()
        pprint(users)
        for i in users:
            if i.bot is False:
                name = i.display_name.split(' ')
                day = 0
                try: 
                    check = name[2]
                except:
                    pprint('Error user {}'.format(name))
                    continue
                if name[2] == '1703':
                    sheet = client.open("test").sheet1
                    g = 3
                    while g<7:
                        cell = sheet.cell(g,2).value
                        name1 = cell.split(' ')
                        if name1[1] == name[0]:
                            j = 11
                            while True:
                                cell_lesson = sheet.cell(g,j).value
                                if cell_lesson == '-':
                                    if day == 0:
                                        day = j
                                    sheet.update_cell(g,day, 1)
                                    await asyncio.sleep(2)
                                    break
                                else:
                                    j = j + 1
                            break
                        g = g + 1
        g = 3
        sheet = client.open("test").sheet1
        while g<7:
            cell = sheet.cell(g,day).value
            if cell == "-":
                sheet.update_cell(g,day, 0)
                await asyncio.sleep(2)
            g = g + 1   
        await ctx1.delete() 
        ctx1 = await ctx.send("`Выполнено`")
        await asyncio.sleep(10)         
    else:
        ctx1 = await ctx.send("`Нeдостаточно привилегий`")
        await asyncio.sleep(10)
    await ctx1.delete() 
       

Bot.run("NzI5MjY2NTgyMzIwMTg1Mzc1.XwOm_g.FMp3Zb7HPfBPUmeIukyk-8WYM7c")  