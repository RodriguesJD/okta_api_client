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


def all_users() -> list:
    """Return a list of all okta users.

    Use okta's rest api to get a list of all users including Active, PROVISIONED, 'SUSPENDED'
    and 'PASSWORD_EXPIRED' status.

    :return:
        users (list): List of all okta users.
    """
    all_user_collected = False
    users = []

    url = f"{base_url}/api/v1/users"
    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'Authorization': f"SSWS {key}"
        }

    while not all_user_collected:
        response = requests.get(url=url, headers=headers)
        for user in response.json():
            users.append(user)

        if 'next' in response.links.keys():
            url = response.links["next"]["url"]
        else:
            all_user_collected = True

    return users