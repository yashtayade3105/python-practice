import requests

res = requests.get("https://api.github.com")
print("Status Code:", res.status_code)
print("Headers:", res.headers['content-type'])
