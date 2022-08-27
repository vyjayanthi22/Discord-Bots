import os
import requests
import json

api_key = os.environ['api_key']


def get_person_id(aname):
	url = 'https://api.themoviedb.org/3/search/person?api_key=' + api_key + '&language=en-US&query=' + aname + '&page=1&include_adult=false'
	response = requests.get(url)
	json_data = json.loads(response.text)
	if json_data['total_results']==0:
		return 'DNE'
	aid = json_data['results'][0]['id']
	return aid

def get_person_poster(aid):
	url = 'https://api.themoviedb.org/3/person/' + str(aid) + '?api_key=' + api_key + '&language=en-US'
	response = requests.get(url)
	json_data = json.loads(response.text)
	aname = json_data['name']
	ext = json_data['profile_path']
	poster_url = 'https://image.tmdb.org/t/p/original/' + ext
	return aname, poster_url

def get_person_best_known_for(aname):
	url = 'https://api.themoviedb.org/3/search/person?api_key=' + api_key + '&language=en-US&query=' + aname + '&page=1&include_adult=false'
	response = requests.get(url)
	json_data = json.loads(response.text)
	if json_data['total_results']==0:
		return 'DNE'
	aname = json_data['results'][0]['name']
	bests = [json_data['results'][0]['known_for'][index]['original_title'] for index in range(len(json_data['results'][0]['known_for']))]
	return aname, bests

def get_person_summary(aname):
	url = 'https://api.themoviedb.org/3/search/person?api_key=' + api_key + '&language=en-US&query=' + aname + '&page=1&include_adult=false'
	response = requests.get(url)
	json_data = json.loads(response.text)
	if json_data['total_results']==0:
		return 'DNE'	
	aname = json_data['results'][0]['name']
	aid = get_person_id(aname)
	summary = {}
	summary['name'] = aname
	if int(json_data['results'][0]['gender'])==1:
		summary['gender'] = 'Female' 
	else:
		summary['gender'] = 'Male'
	summary['bests'] = [json_data['results'][0]['known_for'][index]['original_title'] for index in range(len(json_data['results'][0]['known_for']))]
	summary['years'] = [json_data['results'][0]['known_for'][index]['release_date'][:4] for index in range(len(json_data['results'][0]['known_for']))]
	url = 'https://api.themoviedb.org/3/person/' + str(aid) + '?api_key=' + api_key + '&language=en-US'
	response = requests.get(url)
	json_data = json.loads(response.text)
	brid = json_data['biography'][:1024].rfind('.')
	summary['biography'] = json_data['biography'][:brid+1]
	summary['birthday'] = json_data['birthday']
	summary['deathday'] = json_data['deathday']
	summary['homepage'] = json_data['homepage']
	summary['known_for_department'] = json_data['known_for_department']
	summary['place_of_birth'] = json_data['place_of_birth']	
	return summary