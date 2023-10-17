import requests
import json
import pickle
response_users = requests.get("https://jsonplaceholder.typicode.com/users")
json_user = response_users.json()
response_post = requests.get("https://jsonplaceholder.typicode.com/posts")
json_post = response_post.json()
response_comment = requests.get(
    "https://jsonplaceholder.typicode.com/comments")
json_comment = response_comment.json()

for user in json_user:
    number_comment = 0
    number_post = 0
    for post in json_post:
        if post['userId'] == user['id']:
            number_post += 1
    for comment in json_comment:
        if comment['email'] == user['email']:
            number_comment += 1
dictit = dict()
dictit['id'] = user['id']
dictit['username'] = user['username']
dictit['email'] = user['email']
dictit['posts'] = number_post
dictit['comments'] = number_comment
json_str = dict()
json_str['statistics'] = dictit
json_str1 = json.dumps(json_str, indent=4, ensure_ascii=False)


json_str2 = requests.post(
    "https://webhook.site/e7d71920-8774-4012-bd9f-7cd842192ee6", json_str1)
with open("solution.pickle", 'wb') as file:
    pickle.dump(json_str2, file)
with open("solution.pickle", 'rb') as file:
    print(file.read())
