# This a discord bot written in Python 3.12.0 that 
# retrieves the player count of the Isle Legacy server 
# Age of Dino Sandbox, once you invite the bot to your discord server, 
# simply type !aod and you will get the 
# number of active players on the server.


import settings
import discord
import requests
from discord.ext import commands
import json 

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)

def get_player_info():
    try:
        response = requests.get("https://api.gamemonitoring.net/servers/1983891")
        data = response.json()

        num_players = data['response']['numplayers']
        max_players = data['response']['maxplayers']

        return num_players, max_players

    except Exception as e:
        print(f"Error fetching player info: {e}")
        return None, None

@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready and connected to Discord!")

@bot.command(name="aod")
async def player_info(ctx):
    num_players, max_players = get_player_info()

    if num_players is not None and max_players is not None:
        await ctx.send(f"Current players: {num_players}/{max_players}")
    else:
        await ctx.send("Couldn't fetch the player count at the moment.")

if __name__ == "__main__":
    bot.run(settings.DISCORD_API_SECRET)