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
    #Put private log channel's id
    channel = Bot.get_channel(730145508106043413)
    #Send message to this channel
    await channel.send('<------------------------------->')
    #Put role's id
    role = ctx.message.guild.get_role(729285717628420106)
    await ctx.message.delete() 
    if role in ctx.message.author.roles:
        #Sending message and adding reaction
        ctx1 = await ctx.send("Присутствующие")
        await ctx1.add_reaction("☑️")
        await asyncio.sleep(5)
        #Fix message's reaction
        ctx1 = await ctx1.channel.fetch_message(ctx1.id)
        ctx2 = await ctx.send("`Расчет окончен`")
        for reaction in ctx1.reactions:
            if reaction.emoji == "☑️":
                positive = reaction
        #Take all users which added reaction
        users = await positive.users().flatten()
        sheet = client.open("test").worksheet("1703")
        try:
            users[1]
        except: 
            await ctx1.delete()
            return
        #Working with google table
        for i in users:
            if i.bot is False:
                name = i.display_name.split(' ')
                day = 0
                try: 
                    name[2]
                except:
                    await channel.send('Error user {}'.format(name))
                    continue
                await channel.send(name)
                g = 3
                sheet = client.open("test").worksheet(name[2])
                col1 = sheet.col_values(1)
                result = [int(item) for item in col1[2:]]
                hight = max(result)
                lenght = 2
                #For students which a here (on lesson)
                while g<hight+3:
                    cell = sheet.cell(g,2).value
                    name1 = cell.split(' ')
                    if name1[1] == name[0]:
                        if name1[0] == name[1]:
                            while True:
                                cell = sheet.cell(2,lenght).value
                                try:
                                    int(cell[0:2])
                                    break
                                except:
                                    lenght += 1
                            while True:
                                cell_day = sheet.cell(2,lenght).value
                                cell_lesson = sheet.cell(g,lenght).value      
                                if cell_lesson == '-':
                                    if day == 0:
                                        day = lenght
                                    sheet.update_cell(g,day, 1)
                                    await asyncio.sleep(2)
                                    break
                                else:
                                    lenght += 1
                            break
                    g = g + 1
        #For people who are not here
        numsheet = 0
        while True:
            try:
                sheet = client.open("test").get_worksheet(numsheet)
                sheet.get_all_records()
                result = [int(item) for item in col1[2:]]
                hight = max(result)
                g = 3
                while g<hight+3:
                    while True:
                        cell = sheet.cell(2,lenght).value
                        if cell == cell_day:
                            break
                        else:
                            lenght += 1
                    cell = sheet.cell(g,lenght).value
                    if cell == "-":
                        sheet.update_cell(g,lenght, 0)
                        await asyncio.sleep(2)
                    g = g + 1
                numsheet += 1
            except:
                break
        #Clear text channel
        await ctx1.delete() 
        await ctx2.delete()
        ctx1 = await ctx.send("`Выполнено`")
        await asyncio.sleep(10)         
    else:
        ctx1 = await ctx.send("`Нeдостаточно привилегий`")
        await asyncio.sleep(10)
    await ctx1.delete() 
       
#bot tocken
Bot.run("NzI5MjY2NTgyMzIwMTg1Mzc1.XwOm_g.FMp3Zb7HPfBPUmeIukyk-8WYM7c")  