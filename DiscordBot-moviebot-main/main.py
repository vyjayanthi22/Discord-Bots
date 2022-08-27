import discord
import os
import re
from discord.ext import commands
from discord import Embed, Colour


from movie import get_movie_id, get_movie_description, get_movie_poster, get_movie_genres, get_movie_rating, get_movie_production_companies, get_movie_tagline
from tv import get_tv_id, get_tv_description, get_tv_poster, get_tv_genres, get_tv_rating, get_tv_summary, get_tv_production_companies, get_tv_tagline
from collection import get_collection_id, get_collection_description, get_collection_summary, get_collection_poster
from actor import get_person_id, get_person_poster, get_person_summary

from keep_alive import keep_alive

api_key = os.environ['api_key']
TOKEN = os.environ['TOKEN']

intents = discord.Intents.all()

client = commands.Bot(command_prefix='$', intents = intents)

@client.event
async def on_ready():
	print('We have logged in as: {0.user}'.format(client))

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency*1000)} ms')

@client.command()
async def on_member_join(member):
    await member.send('''Welcome to the channel!\nI am a movie bot\n.Please type {$help} for high-level description.\nYou can use $info for deatiled descriptions of all commands.''')
	

value_description = '''Returns the description for either a movie or TV show or a collection'''
value_dp1 = '''Any of ['m', 'mov', 'movie', 'movies'] for a movie.\nAny of ['tv', 'show', 'tv_show', 'tv_series', 'series'] for TV show.\nAny of ['c', 'collections', 'collection'] for a collection.'''
value_dp2 = '''The title of the movie or TV show or collection, the closer the better.'''

value_poster = '''Returns the poster for either a movie or TV show or a collection or a person'''
value_pp1 = '''Any of ['m', 'mov', 'movie', 'movies'] for a movie.\nAny of ['tv', 'show', 'tv_show', 'tv_series', 'series'] for TV show.\nAny of ['c', 'collections', 'collection'] for a collection.\nAny of ['person', 'actor', 'p', 'actress', 'director', 'actors'] for a person.'''
value_pp2 = '''The title of the movie or TV show or collection or the name of the person, the closer the better.'''
value_pp3 = '''In case of TV show, we can provide an optional season number as {s<num>}. If season number is absent or invalid, the poster for the whole series is returned.'''

value_genres = '''Returns the list of genres for either a movie or TV show or a collection'''
value_gp1 = '''Any of ['m', 'mov', 'movie', 'movies'] for a movie.\nAny of ['tv', 'show', 'tv_show', 'tv_series', 'series'] for TV show.'''
value_gp2 = '''The title of the movie or TV show, the closer the better.'''

value_rating = '''Returns the rating and popularity for either a movie or TV show or a collection'''
value_rp1 = '''Any of ['m', 'mov', 'movie', 'movies'] for a movie.\nAny of ['tv', 'show', 'tv_show', 'tv_series', 'series'] for TV show.'''
value_rp2 = '''The title of the movie or TV show, the closer the better.'''

value_pdcmps = '''Returns the list of production for either a movie or TV show or a collection'''
value_pcp1 = '''Any of ['m', 'mov', 'movie', 'movies'] for a movie.\nAny of ['tv', 'show', 'tv_show', 'tv_series', 'series'] for TV show.'''
value_pcp2 = '''The title of the movie or TV show, the closer the better.'''

value_tagline = '''Returns the tagline for either a movie or TV show or a collection'''
value_tp1 = '''Any of ['m', 'mov', 'movie', 'movies'] for a movie.\nAny of ['tv', 'show', 'tv_show', 'tv_series', 'series'] for TV show.'''
value_tp2 = '''The title of the movie or TV show, the closer the better.'''

value_summary = '''Returns the summary for either a TV show or a collection or a person'''
value_sp1 = '''Any of ['tv', 'show', 'tv_show', 'tv_series', 'series'] for TV show.\nAny of ['c', 'collections', 'collection'] for a collection.\nAny of ['person', 'actor', 'p', 'actress', 'director', 'actors'] for a person.'''
value_sp2 = '''The title of the TV show or collection or the name of the person, the closer the better.'''



@client.command()
async def info(ctx):
	await ctx.send(f'DOCUMENTATION')
	embed_description = Embed(title='$description', color=Colour.red())
	embed_description.add_field(name='Description', value=value_description, inline=False)
	embed_description.add_field(name='parameter_1 - identifier for movie or tv show or collection', value=value_dp1, inline=False)
	embed_description.add_field(name='parameter_2 - the title', value=value_dp2, inline=False)
	await ctx.send(embed=embed_description)
	embed_poster = Embed(title='$poster', color=Colour.blue())
	embed_poster.add_field(name='Description', value=value_poster, inline=False)
	embed_poster.add_field(name='parameter_1 - identifier for movie or tv show or collection or person', value=value_pp1, inline=False)
	embed_poster.add_field(name='parameter_2 - the title or name', value=value_pp2, inline=False)
	embed_poster.add_field(name='parameter_3 - (optional) season number', value=value_pp3, inline=False)
	await ctx.send(embed=embed_poster)
	embed_genres = Embed(title='$genres', color=Colour.green())
	embed_genres.add_field(name='Description', value=value_genres, inline=False)
	embed_genres.add_field(name='parameter_1 - identifier for movie or tv show', value=value_gp1, inline=False)
	embed_genres.add_field(name='parameter_2 - the title', value=value_gp2, inline=False)
	await ctx.send(embed=embed_genres)
	embed_rating = Embed(title='$rating', color=Colour.blurple())
	embed_rating.add_field(name='Description', value=value_rating, inline=False)
	embed_rating.add_field(name='parameter_1 - identifier for movie or tv show', value=value_rp1, inline=False)
	embed_rating.add_field(name='parameter_2 - the title', value=value_rp2, inline=False)
	await ctx.send(embed=embed_rating)
	embed_pdcmps = Embed(title='$production_companies', color=Colour.gold())
	embed_pdcmps.add_field(name='Description', value=value_pdcmps, inline=False)
	embed_pdcmps.add_field(name='parameter_1 - identifier for movie or tv show', value=value_pcp1, inline=False)
	embed_pdcmps.add_field(name='parameter_2 - the title', value=value_pcp2, inline=False)
	await ctx.send(embed=embed_pdcmps)
	embed_tagline = Embed(title='$tagline', color=Colour.dark_purple())
	embed_tagline.add_field(name='Description', value=value_tagline, inline=False)
	embed_tagline.add_field(name='parameter_1 - identifier for movie or tv show', value=value_tp1, inline=False)
	embed_tagline.add_field(name='parameter_2 - the title', value=value_tp2, inline=False)
	await ctx.send(embed=embed_tagline)
	embed_summary = Embed(title='$summary', color=Colour.dark_teal())
	embed_summary.add_field(name='Description', value=value_summary, inline=False)
	embed_summary.add_field(name='parameter_1 - identifier for TV show or a collection or a person', value=value_sp1, inline=False)
	embed_summary.add_field(name='parameter_2 - the title or name', value=value_sp2, inline=False)
	await ctx.send(embed=embed_summary)

@client.command(name='description', help='Description of movie or TV show or collection')
async def _description(ctx, *, msg):
	rest = msg.split(' ', 1)
	m_tv_c = rest[0]
	name = rest[1]
	if m_tv_c in ['m', 'mov', 'movie', 'movies']:
		mid = get_movie_id(name)
		if mid == 'DNE':
			await ctx.send('Movie title not found, check the spellings!')
		else:
			org_title, description = get_movie_description(mid)
			embed = Embed(title=org_title, color=Colour.blue())
			embed.add_field(name='Description', value=description, inline=True)
			embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
			await ctx.send(embed=embed)
	elif m_tv_c in ['tv', 'show', 'tv_show', 'tv_series', 'series']:
		tvid = get_tv_id(name)
		if tvid == 'DNE':
			await ctx.send('TV Series title not found, check the spellings!')
		else:
			org_title, description = get_tv_description(tvid)
			embed = Embed(title=org_title, color=Colour.green())
			embed.add_field(name='Description', value=description, inline=True)
			embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
			await ctx.send(embed=embed)
	elif m_tv_c in ['c', 'collections', 'collection']:
		cid = get_collection_id(name)
		if cid=='DNE':
			await ctx.send('Collection title not found, check the spellings!')
		else:
			org_title, description = get_collection_description(cid)
			embed = Embed(title=org_title, color=Colour.red())
			embed.add_field(name='Description', value=description, inline=True)
			embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
			await ctx.send(embed=embed)	


@client.command(name='poster', help = 'Poster of a movie or TV show or collection or person')
async def _poster(ctx, *, msg):
	rest = msg.split(' ', 1)
	m_tv_c_p = rest[0]
	name = rest[1]
	if m_tv_c_p in ['m', 'mov', 'movie', 'movies']:
		mid = get_movie_id(name)
		if mid == 'DNE':
			await ctx.send('Movie title not found, check the spellings!')
		else:
			org_title, poster_url = get_movie_poster(mid)
			embed = Embed(title=org_title, color=Colour.blue())
			embed.set_image(url=poster_url)
			embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
			await ctx.send(embed=embed)
	elif m_tv_c_p in ['tv', 'show', 'tv_show', 'tv_series', 'series']:
		pattern = r's(\d{0,2})$'
		match = re.findall(pattern, name)
		if len(match)==0:
			snum = 'total'
		elif len(match[0])==0:
			snum = 'total'
			name = name[:-1].rstrip()
		else:
			snum = match[0]
			name = name[:-1*(1 + len(snum))].rstrip()
		tvid = get_tv_id(name)
		if tvid == 'DNE':
			await ctx.send('TV Series title not found, check the spellings!')
		else:								
			org_title, poster_url = get_tv_poster(tvid, snum)
			embed = Embed(title=org_title, color=Colour.green())
			embed.set_image(url=poster_url)
			embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
			await ctx.send(embed=embed)
	elif m_tv_c_p in ['c', 'collections', 'collection']:
		cid = get_collection_id(name)
		if cid=='DNE':
			await ctx.send('Collection title not found, check the spellings!')
		else:
			org_ctitle, poster_url = get_collection_poster(cid)
			embed = Embed(title=org_ctitle, color=Colour.red())
			embed.set_image(url=poster_url)
			embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
			await ctx.send(embed=embed)
	elif m_tv_c_p in ['person', 'actor', 'p', 'actress', 'director', 'actors' ]:
		aid = get_person_id(name)
		if aid=='DNE':
			await ctx.send('Person not found, check the spellings!')
		else:
			aname, poster_url = get_person_poster(aid)
			embed = Embed(title=aname, color=Colour.blurple())
			embed.set_image(url=poster_url)
			embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
			await ctx.send(embed=embed)


@client.command(name='genres', help = 'Genres of movie or TV show')
async def _genres(ctx, *, msg):
	rest = msg.split(' ', 1)
	m_tv = rest[0]
	name = rest[1]
	if m_tv in ['m', 'mov', 'movie', 'movies']:
		mid = get_movie_id(name)
		if mid == 'DNE':
			await ctx.send('Title not found, check the spellings!')
		else:
			org_title, genres = get_movie_genres(mid)
			embed = Embed(title=org_title, color=Colour.blue())
			embed.add_field(name='Genres', value=', '.join(genres), inline=True)
			embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
			await ctx.send(embed=embed)
	elif m_tv in ['tv', 'show', 'tv_show', 'tv_series', 'series']:
		tvid = get_tv_id(name)
		if tvid == 'DNE':
			await ctx.send('Title not found, check the spellings!')
		else:
			org_title, genres = get_tv_genres(tvid)
			embed = Embed(title=org_title, color=Colour.green())
			embed.add_field(name='Genres', value=', '.join(genres), inline=True)
			embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
			await ctx.send(embed=embed)


@client.command(name='rating', help = 'Rating and Popularity of movie or TV show')
async def _rating(ctx, *, msg):
	rest = msg.split(' ', 1)
	m_tv = rest[0]
	name = rest[1]
	if m_tv in ['m', 'mov', 'movie', 'movies']:
		mid = get_movie_id(name)
		if mid == 'DNE':
			await ctx.send('Title not found, check the spellings!')
		else:
			org_title, popularity, rating = get_movie_rating(mid)
			embed = Embed(title=org_title, color=Colour.blue())
			embed.add_field(name='Rating', value=rating, inline=True)
			embed.add_field(name='Popularity', value=popularity, inline=True)
			embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
			await ctx.send(embed=embed)
	elif m_tv in ['tv', 'show', 'tv_show', 'tv_series', 'series']:
		tvid = get_tv_id(name)
		if tvid == 'DNE':
			await ctx.send('Title not found, check the spellings!')
		else:
			org_title, popularity, rating = get_tv_rating(tvid)
			embed = Embed(title=org_title, color=Colour.green())
			embed.add_field(name='Rating', value=rating, inline=True)
			embed.add_field(name='Popularity', value=popularity, inline=True)
			embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
			await ctx.send(embed=embed)



@client.command(name='production_companies', help = 'Production Companies of movie or TV show')
async def _production_companies(ctx, *, msg):
	rest = msg.split(' ', 1)
	m_tv = rest[0]
	name = rest[1]
	if m_tv in ['m', 'mov', 'movie', 'movies']:
		mid = get_movie_id(name)
		if mid == 'DNE':
			await ctx.send('Title not found, check the spellings!')
		else:
			org_title, prod_cmps = get_movie_production_companies(mid)
			embed = Embed(title=org_title, color=Colour.blue())
			embed.add_field(name='Production Companies', value=', '.join(prod_cmps), inline=True)
			embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
			await ctx.send(embed=embed)
	elif m_tv in ['tv', 'show', 'tv_show', 'tv_series', 'series']:
		tvid = get_tv_id(name)
		if tvid == 'DNE':
			await ctx.send('Title not found, check the spellings!')
		else:
			org_title, prod_cmps = get_tv_production_companies(tvid)
			embed = Embed(title=org_title, color=Colour.green())
			embed.add_field(name='Production Companies', value=', '.join(prod_cmps), inline=True)
			embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
			await ctx.send(embed=embed)


@client.command(name='tagline', help = 'Tagline of movie or TV show')
async def _tagline(ctx, *, msg):
	rest = msg.split(' ', 1)
	m_tv = rest[0]
	name = rest[1]
	if m_tv in ['m', 'mov', 'movie', 'movies']:
		mid = get_movie_id(name)
		if mid == 'DNE':
			await ctx.send('Title not found, check the spellings!')
		else:
			org_title, tagline = get_movie_tagline(mid)
			if ((tagline==None) or (len(tagline)==0)):
				await ctx.send("We are sorry, a tagline doesn't exist for this title.")
			else:
				embed = Embed(title=org_title, color=Colour.blue())
				embed.add_field(name='Tagline', value=tagline, inline=True)
				embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
				await ctx.send(embed=embed)
	elif m_tv in ['tv', 'show', 'tv_show', 'tv_series', 'series']:
		tvid = get_tv_id(name)
		if tvid == 'DNE':
			await ctx.send('Title not found, check the spellings!')
		else:
			org_title, tagline = get_tv_tagline(tvid)
			if ((tagline==None) or (len(tagline)==0)):
				await ctx.send("We are sorry, a tagline doesn't exist for this title.")
			else:
				embed = Embed(title=org_title, color=Colour.green())
				embed.add_field(name='Tagline', value=tagline, inline=True)
				embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
				await ctx.send(embed=embed)


@client.command(name='summary', help = 'Summary of TV show or a collection or a person')
async def _summary(ctx, *, msg):
	rest = msg.split(' ', 1)
	tv_c_p = rest[0]
	name = rest[1]
	if tv_c_p in ['tv', 'show', 'tv_show', 'tv_series', 'series']:
		tvid = get_tv_id(name)
		if tvid == 'DNE':
			await ctx.send('Title not found, check the spellings!')
		else:
			org_title, summary = get_tv_summary(tvid)
			embed = Embed(title=org_title, color=Colour.green())
			embed.add_field(name='Number of Seasons', value=summary['number_of_seasons'], inline=True)
			embed.add_field(name='Number of Episodes', value=summary['number_of_episodes'], inline=True)
			embed.add_field(name='Average Episode RunTime', value=str(summary['episode_run_time']) + "mins", inline=False)
			embed.add_field(name='First Air Date', value=summary['first_air_date'], inline=True)
			embed.add_field(name='Last Air Date', value=summary['last_air_date'], inline=True)
			embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
			await ctx.send(embed=embed)
	elif tv_c_p in ['c', 'collections', 'collection']:
		cid = get_collection_id(name)
		if cid=='DNE':
			await ctx.send('Title not found, check the spellings!')
		else:
			org_ctitle, summary = get_collection_summary(cid)
			lst = ""
			for i in range(len(summary['years'])):
				lst += "\t" + summary['names'][i] + " - " + summary['years'][i] + "\n" 
			embed = Embed(title=org_ctitle, color=Colour.red())
			embed.add_field(name='Description', value=summary['overview'], inline=True)
			embed.add_field(name='List of Movies', value=lst, inline=False)
			embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
			await ctx.send(embed=embed)
	elif tv_c_p in ['person', 'actor', 'p', 'actress', 'director', 'actors' ]:
		aid = get_person_id(name)
		if aid=='DNE':
			await ctx.send('Person not found, check the spellings!')
		else:
			summary = get_person_summary(name)
			embed = Embed(title=summary['name'], color=Colour.blurple())
			embed.add_field(name='Gender', value=summary['gender'], inline=False)
			embed.add_field(name='Birthday', value=summary['birthday'], inline=True)
			embed.add_field(name='Place of Birth', value=summary['place_of_birth'], inline=True)
			if summary['deathday']!=None:
				embed.add_field(name='Deathday', value=summary['deathday'], inline=False)
			embed.add_field(name='Biography', value=summary['biography'][:1024], inline=False)
			embed.add_field(name='Best known for the department of:', value=summary['known_for_department'], inline=False)
			lst = ""
			for i in range(len(summary['years'])):
				lst += "\t" + summary['bests'][i] + " - " + summary['years'][i] + "\n"
			embed.add_field(name='Best Known For', value=lst, inline=True)
			if summary['homepage']!=None:
				embed.add_field(name='Homepage', value=summary['homepage'], inline=True)
			embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
			await ctx.send(embed=embed)


keep_alive()
client.run(TOKEN)