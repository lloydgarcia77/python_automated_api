import json
import requests 
from requests.auth import HTTPBasicAuth  
# https://www.programiz.com/python-programming/csv
# https://realpython.com/python-csv/
# https://www.geeksforgeeks.org/authentication-using-python-requests/ 
 
def get_fetch(url,auth):
    response = requests.request("GET", url, headers={},data={}, auth=auth)
    if response.text:
        data = json.loads(response.text)
        return data
    else: 
        return False
 