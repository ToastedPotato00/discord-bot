import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
matrik = []
@bot.command()
async def add_trash(ctx, answer):
    matrik.append(answer)
    await ctx.send(f"{answer} trash added")

@bot.command()
async def remove_trash(ctx, answer):
    matrik.remove(answer)
    await ctx.send(f"{answer} removed")

@bot.command()
async def list_trash(message):
    await message.send(matrik)

@bot.command()
async def check(ctx, answer):
    def check_lagi(m):
        if m.author == ctx.author and m.channel == ctx.channel:
            return m.content
        
        return False

    if answer in matrik :
        await ctx.send("termasuk sampah")
        await ctx.send("mau di buang?(jawab dengan $reply)")
        res = await bot.wait_for("message", check=check_lagi)

        if res.lower() == "yes":
            await ctx.send("terbuang")
        else:
            await ctx.send("tidak dibuang")
    else:
        await ctx.send("bukan sampah")

# @bot.command()
# async def reply(ctx, answer):
#     if answer == "yes":
#         await ctx.send("terbuang")
#     elif answer == "no":
#         await ctx.send("tidak dibuang")
#     else:
#         await ctx.send("invalid error")

@bot.command()
async def time_check(ctx, answer):
    if answer == "apel":
        await ctx.send("1 jam akan terurai")
    elif answer == "pisang":
        await ctx.send("3 jam akan terurai")

bot.run("token")

