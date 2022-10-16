import json

info={}

f = open('amazon2.json',)
data = json.load(f)

# for i in data['products']:
#     title = i['title']

#     reviews = i['reviews']
#     info[title] = reviews

#     fp = open('')

print(len(data['products']))

