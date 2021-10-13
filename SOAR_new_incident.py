import sys
import requests
import json

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    new_incident = {"sequence_code": "string","name": "Name of the incident","discovered_date": 0,"due_date": 0, "create_date": 0,
                    "description":{
                    "format": "text",
                    "content": "Description of the icnident"}
                    }
    uri = 'https://172.16.178.50/rest/orgs/201/incidents?want_full_data=true&want_tasks=false'
    incident = requests.post(uri,json=new_incident,headers={'Content-Type': 'application/json', 'Authorization': "Basic OGMzZTA1MGEtZThjOC00YzcyLTgyOGYtOGY4ZGZkNWNlNDk1Okp1Ni1KRnM2YTRXUDZlSzFWN2xaYUt2cFQ3cTVxTUQ5N082N2RBcXlRNUU="},verify=False) #Basic authentication is login:password or APIkey:password base64 encoded
    print (incident)
    return incident

main()
