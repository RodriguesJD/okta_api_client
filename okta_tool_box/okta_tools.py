from pprint import pprint
import os

import requests


base_url = os.environ["OKTA_BASE_URL"]
key = os.environ["OKTA_KEY"]


def find_user(user_email: str) -> object:
    url = f"{base_url}/api/v1/users?q={user_email}&limit=1"

    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'Authorization': f"SSWS {key}"
        }

    response = requests.get(url=url, headers=headers)

    return response