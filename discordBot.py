import discord
from discord.ext import commands
import json
from tokenConfig import getToken

client = discord.Client(command_prefix='')


@client.event
async def on_ready():
    await client.login(getToken())
    await client.wait_until_ready()
    user: discord.User = await client.fetch_user(205434999888019456)
    if not user.dm_channel:
        await user.create_dm()
    channel: discord.DMChannel = user.dm_channel
    with open("logs.json", "r", encoding="utf-8") as read_file:
        logs = json.load(read_file)
    msg = list(logs.keys())[-1]
    await channel.send(f'[{msg}]: {logs[msg]["tweet"]} | {logs[msg]["postingHour"]} | {logs[msg]["waitingTime"]}')
    await client.logout()

client.run(getToken())
print("end")
