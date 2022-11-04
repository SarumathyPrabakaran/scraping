import json

info={}
fp = open('reviews.txt','w')
f = open('amazon.json',)
data = json.load(f)
count =0
for i in data['products']:
#     title = i['title']

    reviews = i['reviews']
    

    for j in reviews:
        try:
            fp.write(j.split('/')[0])
            count+=1
           
        except:
            continue

# print(len(data['products']))
print(count)

