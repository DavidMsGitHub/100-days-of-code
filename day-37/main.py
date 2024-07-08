from datetime import datetime

import requests
import datetime

USERNAME = "davita"
TOKEN = "mix23!23!Dix"
pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

#     CREATING ACCOUNT
#
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
#
# }

# response = requests.get(pixela_endpoint, params= user_params)


#     CREATING GRAPH
#
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "100 Days of Python",
#     "unit": "Lessons",
#     "type": "int",
#     "color": "kuro",
#     "token": TOKEN
# }
#
#
# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

now_date_nf = datetime.datetime(year=2024, month=6, day=27)
now_date = now_date_nf.strftime("%Y%m%d")

a_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{now_date}"

graph_post_config = {
    "quantity": "12",
}
graph_post = requests.delete(a_graph_endpoint, headers=headers)
graph_post.raise_for_status()
print(graph_post.text)