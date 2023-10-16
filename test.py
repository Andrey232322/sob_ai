import json
#
# import requests
#
# BASE_URL = 'https://jservice.io/api/random?count=1'
#
# response = requests.get(BASE_URL)
# a = response.json()
# w = {}
# for i in a:
#     w = i
# print(w['id'])
# for k,v in w.items():
#     print(k,v)

gun = int(input())
mony = int(input())
b= []
for i in range(gun):
    b.append(int(input()))
m= 0
for i in b:
    if i <= mony:
        m = max(m,i)
print(m)