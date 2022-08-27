import discord
import os
import random
from discord.ext import commands
from discord import Embed, Colour
import asyncio
from quotes import quotes

from keep_alive import keep_alive

TOKEN = os.environ['TOKEN']

intents = discord.Intents.all()
intents.members = True  

client = commands.Bot(command_prefix='$', intents = intents)

@client.event
async def on_ready():
	print('We have logged in as: {0.user}'.format(client))

def cretae_options(series):
	names = list(quotes[series].keys())
	random.shuffle(names)
	num_people = len(names)
	id = random.choice(range(num_people))
	name = names[id]
	poss = list(range(num_people))
	poss.pop(id)
	for _ in range(num_people-4):
		random.shuffle(poss)
		poss.pop(0)
	random.shuffle(poss)
	options = [name]
	for i in range(3):
		options.append(names[poss[i]])
	random.shuffle(options)
	options = [option.capitalize() for option in options]
	return name, options

def generate_random_quote(series, name):
	quote_num = random.choice(range(len(quotes[series][name])))
	quote = quotes[series][name][quote_num]
	return quote


@client.command(name='guess')
async def _guess(ctx, series='friends'):
	name, options = cretae_options(series)
	quote = generate_random_quote(series, name)
	embed = Embed(title='Guess who said this!', color=Colour.blue())
	embed.add_field(name='Question:', value=quote, inline=False)
	opt = "1. "+options[0]+"\n2. "+options[1]+"\n3. "+ options[2]+"\n4. "+options[3]
	embed.add_field(name='Options:', value=opt, inline=True)
	embed.set_footer(icon_url=ctx.author.avatar_url, text=f"To be answered by {ctx.author}")	
	reply = await ctx.send(embed=embed)
	emojis = ["1️⃣","2️⃣","3️⃣","4️⃣"]
	for emoji in emojis:
		await reply.add_reaction(emoji)		
	def check_answer(reaction, user):
		return user == ctx.author	
	reaction, user = None, None
	try:
		reaction, user = await client.wait_for("reaction_add", timeout=30, check=check_answer)
	except asyncio.TimeoutError:
		embed = Embed(title='Answer the next question faster!!', color=Colour.red())
		await ctx.send(embed=embed)
	if reaction and user and reaction.emoji in emojis:
			if options[emojis.index(reaction.emoji)]==name.capitalize():
				embed = Embed(title='Correct Answer!! You guessed right! ' + name.capitalize() + ' said it!', color=Colour.purple())
				await ctx.send(embed=embed)
				await ctx.send(file=discord.File("gifs/" + series + "/" + name + ".gif"))
			else:
				embed = Embed(title='Wrong answer, :(. Actually said by ' + name.capitalize(), color=Colour.red())
				await ctx.send(embed=embed)
				await ctx.send(file=discord.File("gifs/" + series + "/" + name + ".gif"))
	else:
		pass



keep_alive()
client.run(TOKEN)

