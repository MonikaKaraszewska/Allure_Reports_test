import requests

r = requests.get("https://elt.oup.com/")

print(r.status_code)
print(r.text)
print(r.ok)