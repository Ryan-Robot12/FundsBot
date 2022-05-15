
from discord.ext import commands
from replit import db
bot = commands.Bot(command_prefix='/')
cost = 0
try:
  cost = db["cost"]
except Exception as e:
  print(e)
  cost = 0
# db["cost"] = 0

@bot.command()
async def ping(ctx):
  await ctx.chanel.send("pong")
@bot.command()
async def add(ctx, arg):
  global cost
  try:
    cost_to_add = int(arg)
  except Exception:
    await ctx.channel.send("I'm sorry, there was an error. Please make sure your 'add' argument is a valid number")
  cost += cost_to_add
  db["cost"] = cost
  await ctx.channel.send("Current cost: $" + str(cost))

@bot.command()
async def subtract(ctx, arg):
  global cost
  # await ctx.channel.send(arg)
  try:
    cost_to_add = int(arg)
  except Exception:
    await ctx.channel.send("I'm sorry, there was an error. Please make sure your 'subtract' argument is a valid number")
  cost -= cost_to_add
  db["cost"] = cost
  await ctx.channel.send("Current cost: $" + str(cost))

@bot.command()
async def get_cost(ctx):
  await ctx.channel.send("Current cost: $" + str(cost))

# bot.add_command(ping)
bot.run('OTc1NDE5NTExMDczMzA0NjI3.GWoYBH.YsRPG3hRzRwUOp97H8P0IftQ9psZkkx90axuaw')
# client.run('OTc1NDE5NTExMDczMzA0NjI3.GWoYBH.YsRPG3hRzRwUOp97H8P0IftQ9psZkkx90axuaw')