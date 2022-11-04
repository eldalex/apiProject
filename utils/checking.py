''' Методы проверки ответов наших запросов'''
import json

from requests import Response


class Checking():
    '''метод для проверки статус кода'''

    @staticmethod
    def check_status_code(responce: Response, status_code):
        assert status_code == responce.status_code
        if responce.status_code == status_code:
            print('Успешно! Статус код=' + str(responce.status_code))
        else:
            print('Провал! Статус код=' + str(responce.status_code))

    '''Метод для проверки наличия полей в ответе запроса'''

    @staticmethod
    def check_json_token(responce: Response, expected_value):
        token = json.loads(responce.text)
        assert list(token) == expected_value
        print(expected_value)
        print('Все поля присутствут')

    '''Метод для проверки значений полей'''

    @staticmethod
    def check_json_value(responce: Response, field_name, expected_value):
        check = responce.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f"{field_name} верен")