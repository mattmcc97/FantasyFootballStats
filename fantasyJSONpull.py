import requests
import json
import sys
from collections import defaultdict

try:
    json_response = requests.get("https://fantasy.premierleague.com/drf/bootstrap-static").json()
except requests.exceptions.RequestException as e:
    # catastrophic error. bail.
    print("There has been a problem connecting to the fantasy football servers. Please check your" + 
    	" internet connection or try again later.")
    sys.exit(1)

teams = defaultdict(list)

def build_teams():
	
	for i in range(len(json_response['elements'])):
		teams[json_response['elements'][i]['team']].append(json_response['elements'][i]['first_name'] 
			+ " " + json_response['elements'][i]['second_name'])

def get_team_list(team):

	target_id = 0
	for i in range(len(json_response['teams'])):
		if team == json_response['teams'][i]['name']:
			target_id = json_response['teams'][i]['id']
			return teams[target_id]


def filter_by_position(team, position):
	position_list = []
	for i in range(len(json_response['elements'])):
		if (json_response['elements'][i]['element_type'] == position) and (json_response['elements'][i]['team'] == team):
			position_list.append(json_response['elements'][i]['first_name'] + " " + json_response['elements'][i]['second_name'])
	
	return position_list

def team_name_from_id(team_id):
	for team in json_response['teams']:
		if int(team['id']) == int(team_id):
			return team['name']

def position_name_from_element_type(element_type):
	for position in json_response['element_types']:
		if int(position['id']) == int(element_type):
			return position['plural_name']

##https://platform-static-files.s3.amazonaws.com/premierleague/photos/players/110x140/p<photo>.jpg

	
# build_teams()
# print(filter_by_position(1, 2))

#print(json_response['elements'][0])	
# for i in json_response['elements']:
# 	json_response['elements'][i]

# print("*"*48)
# print(team['id'])
# print(team_id)
# print("*"*48)