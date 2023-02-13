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
def get_auth_login_status():
    headers = {"Content-Type": "application/json; Charset=UTF-8"}
    resp = requests.get(base_host + '/users/signin', headers=headers)
    resp.raise_for_status()  # raises exception when not a 2xx response
    if resp.status_code != [200, 201, 202, 204]:
        return resp.json()
    print(resp)
    # return json_data


# if __name__ == "__main__":

# get_auth_login_status( )

json_file_path = 'http://marketplace.sphera.byustudio.in.ua/marketplace/users/signin'
headers = {"Content-Type": "application/json; Charset=UTF-8"}

def get_auth_viastoreto_file():
    # r = requests.get('http://marketplace.sphera.byustudio.in.ua/marketplace/users/signin', headers={'Content-Type': 'application/json; charset=UTF-8'})
    # print (requests.get('http://marketplace.sphera.byustudio.in.ua/marketplace/users/signin', headers={'Content-Type': 'application/json; charset=UTF-8'}))
    HTTPConnection.debuglevel = 1
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain',  'Charset':'UTF-8', 'User-Agent': 'PostmanRuntime/7.30.1'}
    r = requests.get('http://marketplace.sphera.byustudio.in.ua/marketplace/users/signin', headers=headers)

    print("Це урл на який відправляється запит", r.url)
    print("type респонса:", type(r))
    print("Статус респонса, str:", r) #<Response [403]>
    # print("Це тип відповіді:",type(r.content))
    # print("Це тип decode:",(r.content).decode("utf-8"))
    # print("Це відображення контенту:",r.content)
    # print("Це відображається статус відповіді, int:", r.status_code)
    # print("Відображення респонсу: ", r.text)
    # print(a =json.loads(r.text))
    # print("Це відображення headers респонса: ", r.headers())
    print("Це декодований респонс в json формат: ", r.json())

    # data = r.text
    # # try:
    # data_json = json.loads(data)
    # print(data_json)
    # # except json.JSONDecodeError:
    # #     print("Empty response")


if __name__ == "__main__":
    get_auth_viastoreto_file()