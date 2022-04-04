import requests

output_filename = "unsplash_image.jpeg"
BASE_URL = "https://source.unsplash.com/random"

response = requests.get(BASE_URL)
print(response.ok)
with open(output_filename, "wb") as f:
    f.write(response.content)
