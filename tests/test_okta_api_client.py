import os

from okta_api_client.okta_tool_box import okta_tools

me = os.environ["WORK_EMAIL"]


def test_find_user():
    find_me = okta_tools.find_user(me)
    assert find_me.status_code == 200
    assert isinstance(find_me.json(), list)


def test_all_users():
    every_user = okta_tools.all_users()
    assert isinstance(every_user, list)

    for user in every_user:
        assert isinstance(user, dict)
