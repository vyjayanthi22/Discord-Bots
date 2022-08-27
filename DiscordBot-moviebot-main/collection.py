import os
import requests
import json

api_key = os.environ['api_key']

def get_collection_id(cname):
	url = 'https://api.themoviedb.org/3/search/collection?api_key=' + api_key + '&language=en-US&query=' + cname + '&page=1'
	response = requests.get(url)
	json_data = json.loads(response.text)
	if json_data['total_results']==0:
		return 'DNE'
	cid = json_data['results'][0]['id']
	return cid

def get_collection_description(cid):
	url = 'https://api.themoviedb.org/3/collection/' + str(cid) + '?api_key=' + api_key + '&language=en-US'
	response = requests.get(url)
	json_data = json.loads(response.text)
	org_ctitle = json_data['name']
	description = json_data['overview']
	return org_ctitle, description

def get_collection_summary(cid):
	url = 'https://api.themoviedb.org/3/collection/' + str(cid) + '?api_key=' + api_key + '&language=en-US'
	response = requests.get(url)
	json_data = json.loads(response.text)
	org_ctitle = json_data['name']
	summary = {}
	summary['names'] = [json_data['parts'][index]['original_title'] for index in range(len(json_data['parts']))]
	summary['years'] = [json_data['parts'][index]['release_date'][:4]  if 'release_date' in json_data['parts'][index].keys() else ' ' for index in range(len(json_data['parts']))]
	summary['overview'] = json_data['overview']
	return org_ctitle, summary

def get_collection_poster(cid):
	url = 'https://api.themoviedb.org/3/collection/' + str(cid) + '?api_key=' + api_key + '&language=en-US'
	response = requests.get(url)
	json_data = json.loads(response.text)
	org_ctitle = json_data['name']
	ext = json_data['poster_path']
	poster_url = 'https://image.tmdb.org/t/p/original/' + ext
	return org_ctitle, poster_url

