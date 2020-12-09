import datetime
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')
token = "insert your token here"

async def is_owner(ctx): # Not really that well setup for easy use because most commands can be used by one person only. Maybe will make it more easy to setup in the future.
    return ctx.author.id == 424596008954232833 # You should probably put your owner id here

@bot.event
async def on_command_error(ctx, error):
    send_help = (commands.MissingRequiredArgument, commands.BadArgument, commands.TooManyArguments, commands.UserInputError)
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("what")
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This command is on cooldown. Please wait {error.retry_after:.2f}s')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have the permissions to use this command.')

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="anime"))
  print("Bot is online!")

@bot.command(aliases=['logout'])
@commands.check(is_owner)
async def shutdown(ctx):
    await ctx.send("Shutting down...")
    await bot.logout()

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def setup(ctx, key): # setup in server
    if ctx.channel.id == '':
        
    if ctx.author.has_role("Claimed"):
        await ctx.send("You can not claim another server (how are you able to type here...)")
    await ctx.author.send("")
    await ctx.send("Check your DMs for further info")

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def claim(ctx, key, serverid): # claim in dm
    if isinstance(ctx.channel, discord.channel.DMChannel):
        #
    elif:
        await ctx.send("This command can only be used in DMs")

bot.run(token)
