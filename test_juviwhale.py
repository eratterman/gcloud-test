import requests
from tools import DbConnect
from pydantic import ValidationError


URL = 'http://localhost:8000'
DB = DbConnect()


def test_db_connection():
    assert DB.__repr__() == '<Firestore DB Connection: juvi_whale>'


def test_get_tags():
    tags = DB.get_documents()
    assert isinstance(tags, dict)
    print(tags)


def test_api_get_tag_stats():
    result = requests.get(f'{URL}/get_tag_stats')
    assert result.status_code == 200


def test_api_increment_tags():
    args = dict()
    args['name'] = 'foo_bar'
    args['value'] = 2
    url = f'{URL}/increment_tag/'
    result = requests.post(url, json=args)
    assert result.status_code == 200
    print(result.text, type(result.text))


def test_api_fail_increment_uppercase():
    args = dict()
    args['name'] = 'FOO'
    args['value'] = 2
    url = f'{URL}/increment_tag/'
    result = requests.post(url, json=args)
    assert ValidationError
    print(result.status_code)


def test_api_fail_increment_2_chars():
    args = dict()
    args['name'] = 'fm'
    args['value'] = 2
    url = f'{URL}/increment_tag/'
    result = requests.post(url, json=args)
    assert ValidationError
    print(result.status_code)


def test_api_fail_increment_name_too_long():
    args = dict()
    args['name'] = 'fooooooooooobar'
    args['value'] = 2
    url = f'{URL}/increment_tag/'
    result = requests.post(url, json=args)
    assert ValidationError
    print(result.status_code)


def test_api_fail_increment_value_greater_than_10():
    args = dict()
    args['name'] = 'test_bad'
    args['value'] = 10
    url = f'{URL}/increment_tag/'
    result = requests.post(url, json=args)
    assert ValidationError
    print(result.status_code)


def test_api_fail_increment_negative_value():
    args = dict()
    args['name'] = 'test_bad'
    args['value'] = -1
    url = f'{URL}/increment_tag/'
    result = requests.post(url, json=args)
    assert ValidationError
    print(result.status_code)
