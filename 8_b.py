"""
importing modules and main method
API

"""
import matplotlib as plot
import requests as req
api_url="http://shibe.online/api/shibes?count=1"
param={"count":10}
response=req.get(api_url,params=param)

status_code=response.status_code
print("status code is", status_code)

response_json=response.json()
print(response_json)
 