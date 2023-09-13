import requests
import datetime
USERNAME = "vanshp"
TOKEN = "fhaifiy832ur92urj2r208rb2safry"
pixela_endpoint = "https://pixe.la/v1/users"
graph_id = "graph11"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph11",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
today = datetime.datetime.now()
# DATE = today.strftime("%Y%m%d")

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cylce today?"),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "5"
}

# response = requests.put(url=pixel_creation_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
