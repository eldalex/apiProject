import requests
import allure
from utils.loging import Logger

'''Список HTTP методов'''


class Http_methods:
    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod
    def get(url):
        with allure.step('GET'):
            Logger.add_reuqest(url,method='GET')
            result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_responce(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step('POST'):
            Logger.add_reuqest(url, method='POST')
            result = requests.post(url, headers=Http_methods.headers, cookies=Http_methods.cookie, json=body)
            Logger.add_responce(result)
            return result

    @staticmethod
    def put(url,body):
        with allure.step('PUT'):
            Logger.add_reuqest(url, method='PUT')
            result = requests.put(url, headers=Http_methods.headers, cookies=Http_methods.cookie, json=body)
            Logger.add_responce(result)
            return result

    @staticmethod
    def delete(url,body):
        with allure.step('DELETE'):
            Logger.add_reuqest(url, method='DELETE')
            result = requests.delete(url, headers=Http_methods.headers, cookies=Http_methods.cookie, json=body)
            Logger.add_responce(result)
            return result
