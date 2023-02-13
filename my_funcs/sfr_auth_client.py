import requests
import json
import datetime
import logging
from http.client import HTTPConnection

#http://marketplace.sphera.byustudio.in.ua/marketplace/users/signin

# class SfraAuthClient():
#     def __init__(self, url):
#         self.url = url

    # def get_auth_login(self):
    #     resp = requests.get(f'{self.url}/users/signin')
    #     json_data = json.loads(resp.content)
    #     return json_data

base_host = 'http://marketplace.sphera.byustudio.in.ua/marketplace'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain',  'Charset':'UTF-8', 'User-Agent': 'PostmanRuntime/7.30.1'}

def get_auth_login_status():
    resp = requests.get(base_host + '/users/signin', headers=headers)
    # resp.status_code  # raises exception when not a 2xx response
    # if resp.status_code != [200, 201, 202, 204]:
    #     return resp.json()
    return resp.status_code

def get_auth_json_response_body_status():
    HTTPConnection.debuglevel = 1
    try:
        r = requests.get(base_host + '/users/signin', headers=headers)
        if r.status_code != [200, 201, 202, 204]:
            raise Exception("Raises exception when not a 2xx response")
    finally: resp_json = r.json()
    return  resp_json
    # auth_login = resp_json['authorization'] ['login']
    # auth_exp = resp_json['authorization'] ['exp']
    # print(auth_login , auth_exp)

    # print(f'На цей {r.url} відправляється запит')
    # print("type респонса:", type(r))
    # print("Статус респонса, str:", r) #<Response [403]>
    # print("Це тип відповіді:",type(r.content))
    # print("Це тип decode:",(r.content).decode("utf-8"))
    # print("Це відображення контенту:",r.content)
    # print("Це відображається статус відповіді, int:", r.status_code)
    # print("Відображення респонсу: ", r.text)
    # print(a =json.loads(r.text))
    # print("Це відображення headers респонса: ", r.headers())
    # print("Це декодований респонс в json формат: ", r.json())
    # print("Це декодований респонс в json формат: ", resp_json)

def get_auth_json_response_body():
    HTTPConnection.debuglevel = 1
    r = requests.get(base_host + '/users/signin', headers=headers)
    resp_json = r.json()
    print(resp_json)
    return  resp_json


if __name__ == "__main__":
    get_auth_json_response_body()






















































