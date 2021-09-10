import requests

url = 'https://api.pwnedpasswords.com/range/' + '51BAE'
res = requests.get(url)
print(res)
