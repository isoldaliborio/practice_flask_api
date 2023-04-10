import json
import requests

# new_item = {
#     "s_id": 8,
#     "f_id": 8,
#     "item": "papaya",
#     "quantity": 2,
#     "expiration_date": "2023-04-30"
#             }
#
# response = requests.post("http://127.0.0.1:5000/stock",
# headers={"content_type": "application/json"}, data=json.dumps(new_item))
# print(response)
# headers: just indicates the type of response that we're getting
# data: the data that we are sending
# json.dumps() allows us to convert a python object into an equivalent JSON object


# updated_item = {
#     "s_id": 2,
#     "f_id": 2,
#     "item": "bananas",
#     "quantity": 18,
#     "expiration_date": "2023-04-15"
# }
#
# fid = 2
# response = requests.put(f"http://127.0.0.1:5000/stock/{fid}",
#                         headers={"content_type": "application/json"},
#                         data=json.dumps(updated_item))
# print(response)


fid = 5
response = requests.delete(f"http://127.0.0.1:5000/stock/{fid}",
                           headers={"content_type": "application/json"})
# we don't use data in this request because we are doing nothing with the data
print(response)
