import json

total_links_list =[]

f = open('amazon.json',)
data = json.load(f)

for i in data['products']:
    total_links_list.append(i['ratings'])

print(total_links_list)