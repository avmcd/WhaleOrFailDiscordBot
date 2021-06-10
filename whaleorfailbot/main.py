import json
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='wof')

#todo: create json with ratio's

def add_score(member: discord.Member, amount: int):
    if os.path.isfile("file.json"):
        with open("file.json", "r") as fp:
            data = json.load(fp)
        try:
            data[f"{member.id}"]["score"] += amount
        except KeyError: # if the user isn't in the file, do the following
            data[f"{member.id}"] = {"score": amount} # add other things you want to store
    else:
        data = {f"{member.id}": {"score": amount}}
    # saving the file outside of the if statements saves us having to write it twice
    with open("file.json", "w+") as fp:
        json.dump(data, fp, sort_keys=True, indent=4) # kwargs for beautification
   # you can also return the new/updated score here if you want

def get_score(member: discord.Member):
    with open("file.json", "r") as fp:
        data = json.load(fp)
    return data[f"{member.id}"]["score"]

@bot.command()
async def cmd(ctx):
    # some code here
    add_score(ctx.author, 10)
    # 10 is just an example
    # you can use the random module if you want - random.randint(x, y)
    await ctx.send(f"You now have {get_score(ctx.author)} score!")

# TODO: Create command that lists out the ratio's i'm using


bot.run(TOKEN)
