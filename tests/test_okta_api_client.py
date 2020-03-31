import os

from okta_api_client.okta_tool_box import okta_tools
import requests

base_url = os.environ["OKTA_BASE_URL"]
key = os.environ["OKTA_KEY"]

me = os.environ["WORK_EMAIL"]


def test_find_user():
    find_me = okta_tools.find_user(me)
    assert find_me.status_code == 200
    assert isinstance(find_me.json(), list)


def test_user_role():
    # TODO this test takes too long need to re-do this.
    for user in okta_tools.all_users():
        user_id = user['id']
        url = f"{base_url}/api/v1/users/{user_id}/roles"
        headers = {
            'Accept': "application/json",
            'Content-Type': "application/json",
            'Authorization': f"SSWS {key}"
        }
        # this is a mock of the find_user_role()
        response = requests.get(url=url, headers=headers).json()

        # this compares it to the actual find_user_role()
        find_role = okta_tools.find_user_role(user_id)

        # Confirm you the data type is as expected
        if response:
            # Confirm you the data type is as expected
            assert isinstance(find_role, list)
            assert isinstance(find_role[0], dict)
        else:
            assert not find_role

def test_all_users():
    every_user = okta_tools.all_users()
    assert isinstance(every_user, list)

    for user in every_user:
        assert isinstance(user, dict)
