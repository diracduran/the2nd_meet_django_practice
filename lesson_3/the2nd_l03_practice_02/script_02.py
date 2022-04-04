import requests

BASE_URL = "https://api.giphy.com/v1/stickers/random"
params = dict(
        api_key="W6EMr1jb53HK9peoJ7SJsv9e4J3A98us",
        tag="python",
        rating="g",
        fmt='json'
        )
response = requests.get(BASE_URL, params=params)
print(response.ok)
gif_url = response.json()['data']['images']['fixed_height_small']['url']
resp_gif = requests.get(gif_url)
with open("test.gif", "wb") as f:
    f.write(resp_gif.content)
