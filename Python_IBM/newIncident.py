from __future__ import print_function 
from requests.auth import HTTPBasicAuth 
import requests 
import json 

def main(): 
	key_id = "d1ca6af0-000a-4ec5-bfa2-67d4bdefd1b5" 
	key_secret = "Yg_83ZydR0jb936q9u4uuzthypPO891MlLA74cgZOhw" 

	server = "192.168.200.100" 
	resource = "rest/orgs/202/incidents" 
	url = "https://{0}/{1}".format(server, resource) 
	headers = {"Content-Type": "application/json"} 

	name_of_the_incident="Incident from the Python script" 
	description_of_the_incident="Description" 


auth = HTTPBasicAuth(key_id, key_secret) 
req = requests.post(url, headers=headers, auth=auth, verify=False, data=json.dumps({"name":name_of_the_incident,"description":description_of_the_incident,"discovered_date":0})) 

if __name__ == "__main__": 
	main() 
