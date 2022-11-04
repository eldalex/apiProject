import allure
from requests import Response
from utils.api import Google_maps_api
from utils.checking import Checking

'''Создание/изменение/удаление новой локации'''

@allure.epic('Test create place')
class Test_create_palce():

    @allure.description('Test create, update, delete new place')
    def test_create_new_place(self):
        print(f'\nМетод post')
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post,'status','OK')

        print('\nМетод get_post')
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website','language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print('\nМетод put')
        result_put: Response = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print('\nМетод get_put')
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website','language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print('\nМетод delete')
        result_delete: Response = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete,'status','OK')

        print('\nМетод get_delete')
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")


        print('Тестирование создания/изменения/удаления новой локации прошло успешно')