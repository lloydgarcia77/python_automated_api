import json
import requests 
from requests.auth import HTTPBasicAuth  
# https://www.programiz.com/python-programming/csv
# https://realpython.com/python-csv/
# https://www.geeksforgeeks.org/authentication-using-python-requests/ 

# auth = HTTPBasicAuth('qualys', 'wUsK3j8WBK2xFT9HsQ2YyhCA')
# auth= HTTPBasicAuth('bckne3as', 'juAeFXsL')
def get_fetch(url,auth):
    response = requests.request("GET", url, headers={},data={}, auth=auth)
    if response.text:
        data = json.loads(response.text)
        return data
    else: 
        return False
 