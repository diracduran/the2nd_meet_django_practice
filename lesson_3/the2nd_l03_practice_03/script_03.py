import requests
for i in range(1, 5):
    output_filename = f"unsplash_image_{i}.jpeg"
    BASE_URL = "https://source.unsplash.com/random"

    response = requests.get(BASE_URL)
    print(response.ok)
    with open(output_filename, "wb") as f:
        f.write(response.content)