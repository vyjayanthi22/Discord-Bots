import os
import requests
import json


api_key = os.environ['api_key']


def get_tv_id(tvname):
	url = 'https://api.themoviedb.org/3/search/tv?api_key=' + api_key + '&language=en-US&page=1&query=' + tvname + '&include_adult=false'
	response = requests.get(url)
	json_data = json.loads(response.text)
	if json_data['total_results']==0:
		return 'DNE'
	tvid = json_data['results'][0]['id']
	return tvid

def get_tv_description(tvid):
	url = 'https://api.themoviedb.org/3/tv/' + str(tvid) + '?api_key=' + api_key + '&language=en-US'
	response = requests.get(url)
	json_data = json.loads(response.text)
	org_title = json_data['original_name'] 
	description = json_data['overview']
	return org_title, description

def get_tv_poster(tvid, snum):
	url = 'https://api.themoviedb.org/3/tv/' + str(tvid) + '?api_key=' + api_key + '&language=en-US'
	response = requests.get(url)
	json_data = json.loads(response.text)
	org_title = json_data['original_name'] 
	number_of_seasons = json_data['number_of_seasons']
	if ((snum=='total') or (int(snum)>number_of_seasons)):
		ext = json_data['poster_path']
	else:
		ext = json_data['seasons'][int(snum)]['poster_path']
		if ext==None:
			ext = json_data['poster_path']
	poster_url = 'https://image.tmdb.org/t/p/original/' + ext
	return org_title, poster_url

def get_tv_production_companies(tvid):
	url = 'https://api.themoviedb.org/3/tv/' + str(tvid) + '?api_key=' + api_key + '&language=en-US'
	response = requests.get(url)
	json_data = json.loads(response.text)
	org_title = json_data['original_name']
	prod_cmps = [json_data['production_companies'][index]['name'] for index in range(len(json_data['production_companies']))]
	return org_title, prod_cmps

def get_tv_genres(tvid):
	url = 'https://api.themoviedb.org/3/tv/' + str(tvid) + '?api_key=' + api_key + '&language=en-US'
	response = requests.get(url)
	json_data = json.loads(response.text)
	org_title = json_data['original_name'] 
	genres = [json_data['genres'][index]['name'] for index in range(len(json_data['genres']))]
	print(genres)
	return org_title, genres

def get_tv_rating(tvid):
	url = 'https://api.themoviedb.org/3/tv/' + str(tvid) + '?api_key=' + api_key + '&language=en-US'
	response = requests.get(url)
	json_data = json.loads(response.text)
	org_title = json_data['original_name'] 
	popularity = json_data['popularity']
	rating = json_data['vote_average']
	return org_title, popularity, rating

def get_tv_summary(tvid):
	url = 'https://api.themoviedb.org/3/tv/' + str(tvid) + '?api_key=' + api_key + '&language=en-US'
	response = requests.get(url)
	json_data = json.loads(response.text)
	org_title = json_data['original_name']
	summary = {}	
	summary['number_of_seasons'] = json_data['number_of_seasons']
	summary['number_of_episodes'] = json_data['number_of_episodes']
	summary['episode_run_time'] = json_data['episode_run_time'][0] 
	summary['first_air_date'] = "/".join(json_data['first_air_date'].split("-")[::-1])
	summary['last_air_date'] = "/".join(json_data['last_air_date'].split("-")[::-1])
	return org_title, summary
	
def get_tv_tagline(tvid):
	url = 'https://api.themoviedb.org/3/tv/' + str(tvid) + '?api_key=' + api_key + '&language=en-US'
	response = requests.get(url)
	json_data = json.loads(response.text)
	org_title = json_data['original_name']
	tagline = json_data['tagline']
	return org_title, tagline