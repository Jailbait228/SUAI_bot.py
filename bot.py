import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random

Bot = commands.Bot (command_prefix='!')

@Bot.event
async def on_ready():
    print("Bot is online")

@Bot.command(pass_context=True)
async def start(ctx):
    role = ctx.message.guild.get_role(387190022232735747)
    await ctx.message.delete() 
    if role in ctx.message.author.roles:
        ctx1 = await ctx.send("Присутствующие")
        await ctx1.add_reaction("☑️")
        await asyncio.sleep(5)
        ctx1 = await ctx1.channel.fetch_message(ctx1.id)
        for reaction in ctx1.reactions:
            if reaction.emoji == "☑️":
                positive = reaction
       # async for user in positive.users().display_name:
        #    await ctx.send('{0} has reacted with {1.emoji}!'.format(user, positive))
        users = await positive.users().flatten()
        #winner = random.choice(users)
        for i in users:
            if i.bot is False:
                await ctx.send('{} has won the raffle.'.format(i.display_name))
    else:
        await ctx.send("`Нeдостаточно привилегий`")
        await asyncio.sleep(10)
    await ctx1.delete()    

Bot.run("NzI4MjQzODQyNjE2MTMxNTk1.XwLx7w.7ul3bePpS3S827Oe5zyZMERe7zo")  