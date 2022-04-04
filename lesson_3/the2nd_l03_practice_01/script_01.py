import requests
import random

image_list = ["https://images.unsplash.com/photo-1552734839-1e9c4a005a59?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80", "https://images.unsplash.com/photo-1553075712-453f7213c24f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80", "https://images.unsplash.com/photo-1548189856-d9e5926307ed?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1620&q=80", "https://images.unsplash.com/photo-1527062944535-64da38a9cbeb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=662&q=80", "https://images.unsplash.com/photo-1545557475-6ce7e6c63dbc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=580&q=80", "https://images.unsplash.com/photo-1545966239-6fe31602f152?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80", "https://images.unsplash.com/photo-1536625737227-92a1fc042e7e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1650&q=80", "https://images.unsplash.com/photo-1545447011-a875021237ea?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1650&q=80", "https://images.unsplash.com/photo-1542546068979-b6affb46ea8f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80", "https://images.unsplash.com/photo-1537029271773-31e5422be11c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80", "https://images.unsplash.com/photo-1465788786008-f75a725b34e9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1650&q=80"]

for i in range(1,12):
    image_url = random.choice(image_list)
    image_list.remove(image_url)
    response = requests.get(image_url)
    with open(str(i)+".jpeg", "wb") as f:
        f.write(response.content)
