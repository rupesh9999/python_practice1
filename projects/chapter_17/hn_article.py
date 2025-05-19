import requests

import json

# make an API call, and store the response

url = 'https://hacker-news.firebaseio.com/v0/item/1915826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
response_dict = r.json()
readable_file = '/home/ubuntu/python_practice1/projects/chapter_17/data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)