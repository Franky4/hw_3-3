import requests


def get_common_friends(params, target_id, source_id=None, count='3'):
    # Возвращает список идентификаторов общих друзей между парой пользователей.
    if source_id is not None:
        params['source_uid'] = source_id
    params['target_uid'] = target_id
    params['count'] = count  # количество общих друзей
    return requests.get('https://api.vk.com/method/friends.getMutual', params)


def get_my_friends(params, user_id=None):
    if user_id is not None:
        params['user_id'] = user_id
    response = requests.get('https://api.vk.com/method/friends.get', params)
    return response.json()['response']['items']


def main():
    version = '5.74'
    token = 'd82f8d2f03447e2f9d036f5aee9ed820a5204ce23501253e8804f4d44ba81a87ab8ea52d1da1ea8429372'
    params = {
        'v': version,
        'access_token': token
    }

    my_friends = get_my_friends(params)
    for friend in my_friends:
        common_friends = get_common_friends(params, friend).json()['response']
        print('Ваши общие друзья с {}:'.format(friend))
        if len(common_friends) == 0:
            print('  Нет общих друзей!')
        else:
            for cf in common_friends:
                print('  Friend id: {}, ссылка на страницу: https://vk.com/id{}'.format(cf, cf))


if __name__ == '__main__':
    main()




