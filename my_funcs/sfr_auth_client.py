import requests
import json
import datetime

#http://marketplace.sphera.byustudio.in.ua/marketplace/users/signin

# class SfraAuthClient():
#     def __init__(self, url):
#         self.url = url

    # def get_auth_login(self):
    #     resp = requests.get(f'{self.url}/users/signin')
    #     json_data = json.loads(resp.content)
    #     return json_data
base_host = 'http://marketplace.sphera.byustudio.in.ua/marketplace'
def get_auth_login_status():
    headers = {"Content-Type": "application/json; Charset=UTF-8"}
    resp = requests.get(base_host + '/users/signin', headers=headers)
    resp.raise_for_status()  # raises exception when not a 2xx response
    if resp.status_code != 204:
        return resp.json()
    # json_data = resp.status_code
    print(resp)
    # return json_data


# if __name__ == "__main__":

get_auth_login_status( )



    # s = SfraAuthClient('http://marketplace.sphera.byustudio.in.ua/marketplace')
    # print(s.get_auth_login())