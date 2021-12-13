#!python
import json
import os
import platform
import random
import sys

import nextcord
from nextcord import guild
from nextcord.ext import tasks, commands
from nextcord.ext.commands import Bot

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found!")
else:
    with open("config.json") as file:
        config = json.load(file)

intents = nextcord.Intents.all()

client = Bot(command_prefix=config["prefix"], intents=intents)

client.remove_command("help")

@client.event
async def on_ready():
    print(f"Logged in as: {client.user.name}")
    print(f"NextCord API Version: {nextcord.__version__}")
    print(f"Python Version: {platform.python_version()}")
    print(f"OS: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")

@tasks.loop(seconds=20)
async def check_activity():
    status = "<status>"
    await client.wait_until_ready()
    guild = client.get_guild(<guild id>)
    role = guild.get_role(<role id>) 
    for member in client.get_all_members():
        if member.activity != None:
            if member.activity.name == status:
                await member.add_roles(role)    



check_activity.start()
        
client.run(config["token"])
