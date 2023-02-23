from dotenv import load_dotenv
import os
import base64
from requests import post
import json


clientid = "5ccfd932697d421f9865999d2ea1a403"
clientSecret = "39cdf7f9bfc541d28d4f53d2b647b2e6"

def get_token():
    auth_string = clientid + ":" + clientSecret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic" + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "authorization_code"}
    
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result
    print(token)
    return token

    

token = get_token()
print(token)