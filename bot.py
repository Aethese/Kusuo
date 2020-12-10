import datetime
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')
token = "insert your token here"

async def is_owner(ctx): # Not really that well setup for easy use because most commands can be used by one person only. Maybe will make it more easy to setup in the future.
    return ctx.author.id == 424596008954232833 # You should probably put your owner id here

@bot.event
async def on_command_error(ctx, error):
    send_help = (commands.MissingRequiredArgument, commands.BadArgument, commands.TooManyArguments, commands.UserInputError)
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("I don't understand...")
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

@bot.command(description="Get your premium key", aliases=["getkey", "get-key"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def setup(ctx): # setup in server
    if ctx.channel.id == '786305794874408960': # i have this setup so you can only use the command in a certain channel and without a certain role
        if ctx.author.has_role("Claimed"): # the channel doesn't allow people with this role to send messages in the channel, but just in case :)
            await ctx.send("You can not claim another server (how are you able to type here...)")
        else:
            file = open("keys.txt", "r+")
            k = file.readline() # the key
            await ctx.author.send("{} is your premium key! Please respond to this message with $claim your_key your_server_id to setup your premium server".format(k)) # send the instructions + key to the author
            f.seek(0) # reset the file to read the first line again
            d = file.readlines() # gets all of the keys
            for i in d:
                if i != k: # finds the key
                    f.write(i) # writes the key out
            file.close() # we want to close it to free up system resources
            
            await ctx.send("Check your DMs {} for further info".format(ctx.author.name))
            member = ctx.message.author
            role = get(member.server.roles, name="Claimed")
            await bot.add_roles(member, role) # this gives the command, but will remove it after a month (once i add that feature)
    else: # if the channel id isn't the one above, the command gets ignored
        pass

@bot.command(description="Claim your premium server through DMs with a key given to you with the 'setup' command")
@commands.cooldown(1, 5, commands.BucketType.user)
async def claim(ctx, key, serverid): # claim in dm
    if isinstance(ctx.channel, discord.channel.DMChannel):
        #
    else:
        await ctx.send("This command can only be used in DMs") # You can also just pass this command too

@bot.command()
@commands.check(is_owner)
async def addkey(ctx): # the owner can add keys with this simple command
    #

@bot.command(aliases=['patreon', 'premium', 'patron']) # just got to plug the patreon page
@commands.cooldown(1, 5, commands.BucketType.user)
async def donate(ctx):
    embed=discord.Embed(title="Patreon", url="https://www.patreon.com/aethese", color=0x00ffb7)
    embed.set_author(name="Donations", icon_url="https://i.imgur.com/f4L5PvD.png")
    embed.set_footer(text="I take donations through Patreon with the link above! All donations/purchases are greatly appreciated!")
    await ctx.send(embed=embed)

bot.run(token)
