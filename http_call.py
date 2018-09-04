import requests

for i in range(3):
    r = requests.get('https://webhook.site/cbd99238-0b0d-4515-83a3-54a8d2630737')
    print(r.headers['Date'])