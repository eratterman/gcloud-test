import requests


BASE_URL = 'https://eric-juviwhale-pnbrqu3f5a-wl.a.run.app'


def get_documents():
    pass


if __name__ == '__main__':
    result = requests.get(BASE_URL)
    print(result.status_code)
    print(result.text)
