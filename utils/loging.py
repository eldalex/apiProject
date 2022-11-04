import datetime
import os
from requests import Response

class Logger:
    file_name = f"logs/log_{str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))}.log"

    @classmethod
    def write_log_to_file(cls,data:str):
        with open(cls.file_name, 'a', encoding='utf-8') as file:
            file.write(data)
    @classmethod
    def add_reuqest(cls, url:str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')
        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += f"\n"
        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_responce(cls, result: Response):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)
        data_to_add = f"Responce code: {result.status_code}\n"
        data_to_add += f"Responce text: {result.text}\n"
        data_to_add += f"Responce Headers: {headers_as_dict}\n"
        data_to_add += f"Responce Cookies: {cookies_as_dict}\n"
        data_to_add += f"\n-----\n"
        cls.write_log_to_file(data_to_add)