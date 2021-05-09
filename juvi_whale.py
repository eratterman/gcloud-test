import requests


BASE_URL = 'https://eric-juviwhale-pnbrqu3f5a-wl.a.run.app'


def get_documents():
    url = fr'{BASE_URL}/get_tag_stats/'
    result = requests.get(url)
    print(result.status_code)
    return result.json()


def save_doc(name, value):
    args = dict()
    args['name'] = name
    args['value'] = value
    url = f'{BASE_URL}/increment_tag/'
    result = requests.post(url, json=url)
    print(result.status_code)
    return result.json()


if __name__ == '__main__':
    test = get_documents()
    test = save_doc('foo_bar', 8)
    print(test, type(test))
