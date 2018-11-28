"""Fetching github stargazer information"""

import json
import csv
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import datetime
import time
import argparse

parser = argparse.ArgumentParser(description='pass input file as arguments')
parser.add_argument('--repository',type=str, help='github repository name')
parser.add_argument('--access_token',type=str, help='github access_token')
args= parser.parse_args()

config = json.loads(open('config.json', 'r').read())

ACCESS_TOKEN = args.access_token or config['ACCESS_TOKEN']
REPO = args.repository or config['REPOSITORY_NAME']
FIELDS_TO_EXTRACT = config['FIELDS_TO_EXTRACT']
EXPORT_FILE_NAME  = config['EXPORT_FILE_NAME']

GITHUB_ENTRY_POINT = "https://api.github.com/"
STARGAZER_ENDPOINT = "repos/{0}/stargazers"
USERS_ENDPOINT = "users/{0}"


def request(url, params, headers=None):
	url = url + '?' + urlencode(params)
	req = Request(url)
	if headers:
		req.add_header(*headers)
	response = urlopen(req)
	return json.loads(response.read().decode('utf-8'))


def initialize_csv(file_obj, column_names):
	stars_writer = csv.writer(file_obj)
	stars_writer.writerow(column_names)
	return stars_writer

def write_csv_row(csv_file, row_data):
	csv_file.writerow(row_data)

def fetch_stars(repository_name, list_stars=[], page_number=0):

	print("Gathering Stargazers for {0}, page {1}".format(REPO, page_number))

	query_url = GITHUB_ENTRY_POINT + \
				STARGAZER_ENDPOINT.format(repository_name)

	params = {'page': page_number, 'access_token': ACCESS_TOKEN}
	headers = ('Accept', 'application/vnd.github.v3.star+json')

	data = request(query_url, params, headers)

	for user in data:
		username = user['user']['login']
		star_time = datetime.datetime.strptime(
		    user['starred_at'], '%Y-%m-%dT%H:%M:%SZ')
		star_time = star_time.strftime('%Y-%m-%d %H:%M:%S')
		list_stars.append((username, star_time))

	#if we hit the last page, return the results list
	if len(data) == 0:
		list_stars = list(set(list_stars))  # remove dupes
		print("Done Gathering Stargazers for ", REPO)
		print("Now Gathering Stargazers' GitHub Profiles...")
		return list_stars

	# else go to next page
	else:
		return fetch_stars(repository_name, list_stars=list_stars, page_number=page_number + 1)

def fetch_and_write_user_to_csv(users_list, repository_name):
	users_processed = 0
	file_name = EXPORT_FILE_NAME.format(repository_name.split('/')[1])
	with open(file_name, 'w') as stars:
		stars_writer = initialize_csv(stars, FIELDS_TO_EXTRACT)

		for user in users_list:
			query_url = GITHUB_ENTRY_POINT + USERS_ENDPOINT.format(user[0])
			params = {'access_token': ACCESS_TOKEN}
			data = request(query_url, params)

			d = {key:data[key] for key in FIELDS_TO_EXTRACT if key in data }

			# UTF-8 conversion for some fields
			for field in ['name', 'location', 'company']:
				if d[field]:
						d[field] = d[field].encode('utf-8').decode('utf-8')

			#Inject remaining fields time to data
			created_at = datetime.datetime.strptime(
					data['created_at'], '%Y-%m-%dT%H:%M:%SZ')
			created_at = created_at.strftime('%Y-%m-%d %H:%M:%S')

			d['username'] = user[0]
			d['star_time'] = user[1]
			d['created_at'] = created_at

			to_write = [d[key] for key in FIELDS_TO_EXTRACT]

			write_csv_row(stars_writer, to_write)
			users_processed += 1
			if users_processed % 100 == 0:
				print("%s Users Processed: %s",
						(users_processed, datetime.datetime.now()))

	        # stay within API rate limit of 5000 requests / hour
			# 1 hours = 3600 seconds
			# Could do 5000/3600 (~ 1,3) requests per second or a request every ~0,7 seconds
			# Adding some buffer time, so we make a request every 0.8 seconds
			time.sleep(0.8)

if __name__ == '__main__':
	list_stars = fetch_stars(REPO)
	fetch_and_write_user_to_csv(list_stars, REPO)
