import os
import requests
import json

api_key = os.environ['api_key']


def get_movie_id(mname):
	url = 'https://api.themoviedb.org/3/search/movie?api_key=' + api_key + '&language=en-US&query=' + mname + '&page=1&include_adult=false'
	response = requests.get(url)
	json_data = json.loads(response.text)
	if json_data['total_results']==0:
		return 'DNE'
	mid = json_data['results'][0]['id']
	return mid

def get_movie_description(mid):
	url = 'https://api.themoviedb.org/3/movie/' + str(mid) + '?api_key=' + api_key + '&language=en-US'
	response = requests.get(url)
	json_data = json.loads(response.text)
	org_title = json_data['original_title'] 
	description = json_data['overview']
	return org_title, description 

def get_movie_poster(mid):
	url = 'https://api.themoviedb.org/3/movie/' + str(mid) + '?api_key=' + api_key + '&language=en-US'
	response = requests.get(url)
	json_data = json.loads(response.text)
	org_title = json_data['original_title'] 
	ext = json_data['poster_path']
	poster_url = 'https://image.tmdb.org/t/p/original/' + ext
	return org_title, poster_url

def get_movie_production_companies(mid):
	url = 'https://api.themoviedb.org/3/movie/' + str(mid) + '?api_key=' + api_key + '&language=en-US'
	response = requests.get(url)
	json_data = json.loads(response.text)
	org_title = json_data['original_title'] 
	prod_cmps = [json_data['production_companies'][index]['name'] for index in range(len(json_data['production_companies']))]
	return org_title, prod_cmps

def get_movie_genres(mid):
	url = 'https://api.themoviedb.org/3/movie/' + str(mid) + '?api_key=' + api_key + '&language=en-US'
	response = requests.get(url)
	json_data = json.loads(response.text)
	org_title = json_data['original_title'] 
	genres = [json_data['genres'][index]['name'] for index in range(len(json_data['genres']))]
	return org_title, genres

def get_movie_rating(mid):
	url = 'https://api.themoviedb.org/3/movie/' + str(mid) + '?api_key=' + api_key + '&language=en-US'
	response = requests.get(url)
	json_data = json.loads(response.text)
	org_title = json_data['original_title'] 
	popularity = json_data['popularity']
	rating = json_data['vote_average']
	return org_title, popularity, rating

def get_movie_tagline(mid):
	url = 'https://api.themoviedb.org/3/movie/' + str(mid) + '?api_key=' + api_key + '&language=en-US'
	response = requests.get(url)
	json_data = json.loads(response.text)
	org_title = json_data['original_title']
	tagline = json_data['tagline']
	return org_title, tagline