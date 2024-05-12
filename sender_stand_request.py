import configuration
import requests
import data
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
responsePost = post_new_user(data.user_body);
print(responsePost.status_code)
print(responsePost.json())

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
responseGet = get_users_table()
print(responseGet)