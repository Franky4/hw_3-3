import requests

TOKEN = 'd82f8d2f03447e2f9d036f5aee9ed820a5204ce23501253e8804f4d44ba81a87ab8ea52d1da1ea8429372'


class MyVkClient:

    def __init__(self, token):
        self.version = '5.74'
        self.token = token
        self.params = {
            'v': self.version,
            'access_token': self.token
        }

    def get_common_friends(self, target_id, source_id=None, count='3'):
        # Возвращает список идентификаторов общих друзей между парой пользователей.
        if source_id is not None:
            self.params['source_uid'] = source_id
        self.params['target_uid'] = target_id
        self.params['count'] = count  # количество общих друзей
        return requests.get('https://api.vk.com/method/friends.getMutual', self.params).json()['response']

    def get_my_friends(self, user_id=None):
        if user_id is not None:
            self.params['user_id'] = user_id
        response = requests.get('https://api.vk.com/method/friends.get', self.params)
        return response.json()['response']['items']

    def print_common_friends(self, my_friends):
        for friend in my_friends:
            common_friends = self.get_common_friends(friend)
            print('Ваши общие друзья с {}:'.format(friend))
            if len(common_friends) == 0:
                print('  Нет общих друзей!')
            else:
                for cf in common_friends:
                    print('  Friend id: {}, ссылка на страницу: https://vk.com/id{}'.format(cf, cf))


def main():
    vk_data = MyVkClient(TOKEN)
    my_friends = vk_data.get_my_friends()
    vk_data.print_common_friends(my_friends)


if __name__ == '__main__':
    main()




