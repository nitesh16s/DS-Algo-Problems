import json 
import requests

api_token = 'your_api_token'
api_url_base = 'https://api.digitalocean.com/v2/'

headers = {
	'Content-Type': 'application/json',
	'Authorization': 'Bearer {0}'.format(api_token)
}