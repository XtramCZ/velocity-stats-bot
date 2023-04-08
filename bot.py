import discord, os, requests
from discord.ext.commands import Bot
from colorama import Fore, init
init()


### CONFIG ###
token = ""
prefix = "$"
api_keys = [
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
]
##############


bot = Bot(status=discord.Status.dnd, command_prefix=prefix, intents=discord.Intents.all())

command = 'clear'
if os.name in ('nt', 'dos'):
    command = 'cls'
os.system(command)

@bot.event
async def on_ready():
    try:
        await bot.wait_until_ready()
        print(f"{Fore.GREEN}BOT ONLINE{Fore.RESET}")
    except Exception as e:
        print(e)

@bot.command()
async def stats(ctx):
    embed = discord.Embed(title="Velocity Stats", color=0x00f2ff)
    total_alts = 0
    total_servers = 0
    for key in api_keys:
        res = requests.get(f'https://genefit.to/velocity/api/stats.php?key={key}').json()
        total_alts = total_alts + res['alts']
        total_servers = total_servers + res['total_servers']
        embed.add_field(name=f"VPS {api_keys.index(key)+1}", value=f"Alts: {res['alts']}\nServers: {res['total_servers']}\nTime running: {res['time_running']}")
    embed.add_field(name=f"TOTAL", value=f"Tokens: {total_alts}\nServers: {total_servers}")
    await ctx.reply(embed=embed)

bot.run(token)
