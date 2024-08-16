import discord, random
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def guess(ctx, user_guess: int):
    answer = random.randint(1,10)
    if user_guess == answer:
        await ctx.send('benar')
    else:
        await ctx.send(f'salah, jawabannya adalah {answer}.')

@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)

@bot.event
async def on_message(message):
    if message.content.startswith('$deleteme'):
        await message.delete()
    await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    msg = f'{message.author} has deleted a message'
    await message.channel.send(msg)

bot.run("token")
