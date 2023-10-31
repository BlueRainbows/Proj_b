import pytest

from functions import get_successful_op, sorted_data, getting_date_output, getting_index, get_op_output, \
    getting_str
from utils import open_json_file


@pytest.fixture
def coll():
    return [
        {
            "id": 580054042,
            "state": "EXECUTED",
            "date": "2018-06-20T03:59:34.851630",
            "operationAmount": {
                "amount": "96350.51",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "МИР 3766446452238784",
            "to": "Счет 86655182730188443980"
        },
        {
            "id": 619287771,
            "state": "EXECUTED",
            "date": "2019-08-19T16:30:41.967497",
            "operationAmount": {
                "amount": "81150.87",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 17691325653939384901",
            "to": "Счет 49304996510329747621"
        },
        {
            "id": 490100847,
            "state": "EXECUTED",
            "date": "2018-12-22T02:02:49.564873",
            "operationAmount": {
                "amount": "56516.63",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Gold 8326537236216459",
            "to": "MasterCard 6783917276771847"
        },
        {
            "id": 179194306,
            "state": "EXECUTED",
            "date": "2019-05-19T12:51:49.023880",
            "operationAmount": {
                "amount": "6381.58",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "МИР 5211277418228469",
            "to": "Счет 58518872592028002662"
        },
        {
            "id": 27192367,
            "state": "CANCELED",
            "date": "2018-12-24T20:16:18.819037",
            "operationAmount": {
                "amount": "991.49",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 71687416928274675290",
            "to": "Счет 87448526688763159781"
        },
        {
            "id": 921286598,
            "state": "EXECUTED",
            "date": "2018-03-09T23:57:37.537412",
            "operationAmount": {
                "amount": "25780.71",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 26406253703545413262",
            "to": "Счет 20735820461482021315"
        },
        {
            "id": 207126257,
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
            "operationAmount": {
                "amount": "92688.46",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 35737585785074382265"
        },
        {
            "id": 957763565,
            "state": "EXECUTED",
            "date": "2019-01-05T00:52:30.108534",
            "operationAmount": {
                "amount": "87941.37",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 46363668439560358409",
            "to": "Счет 18889008294666828266"
        },
        {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {
                "amount": "97853.86",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 1308795367077170",
            "to": "Счет 96527012349577388612"
        }]


@pytest.fixture
def list_data():
    return ["2019-07-13T18:51:29.313309", "2019-01-05T00:52:30.108534", "2019-07-15T11:47:40.496961",
            "2019-08-19T16:30:41.967497", "2019-05-19T12:51:49.023880", "2018-03-09T23:57:37.537412",
            "2018-12-24T20:16:18.819037", "2018-12-22T02:02:49.564873", "2018-06-20T03:59:34.851630"]


@pytest.fixture
def func_val(coll):
    index_list = []
    list_values = []
    for i in range(len(coll)):
        if 'description' in coll[i]:
            if 'from' not in coll[i]:
                coll[i]['from'] = '-'
        for v in coll[i].values():
            list_values.append(v)
    for numb in range(len(list_values)):
        if list_values[numb] == 'CANCELED':
            index_list.append(numb)
    index_list.reverse()
    for ind in index_list:
        del list_values[ind:ind + 7]
    return list_values


def test_open_json_file():
    """ Тест проверяет правильность чтения файла json, по типу: лист с индексом 0 == словарю со значениями"""
    assert open_json_file()[0] == {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }


def test_get_successful_op(coll):
    """
    1 Тест определяет то что в списке имеются только успешные операции
    2 Тест определяет что добавились значения "-" к ключу "from",
    если такого ключа нет в исходном списке
    """
    assert "CANCELED" not in get_successful_op(coll)
    assert '-' in get_successful_op(coll)


def test_sorted_data(func_val):
    """ Тест определяет что список отсортировался по самому большому значению,
    по параметрам ГГ.ММ.ДД. """
    ind = sorted_data(func_val)
    assert ind[0] == '2019-08-19T16:30:41.967497'


def test_getting_date_output(list_data):
    """ Тест проверяет длинну возвращенного списка"""
    assert len(getting_date_output(list_data)) == 5


def test_getting_index(func_val, list_data):
    """ Тест проверяет, что выведенный список функции которая возвращает индекс значений,
    возвращает int """
    string = ''
    for i in getting_index(func_val, list_data):
        string = str(i)
    assert string.isdigit()


def test_get_op_output(func_val, list_data):
    """ Тест проверяет правильность поиска значений по индексу """
    list_index = []
    del list_data[5:]
    for val in list_data:
        ind = func_val.index(val)
        list_index.append(ind)
    assert "Перевод с карты на счет" == get_op_output(func_val, list_index)[0]
    assert "Перевод организации" == get_op_output(func_val, list_index)[-8]


def test_getting_str(list_data, func_val):
    """ Тест проверяет что на выводе образуется строка"""
    del list_data[5:]
    del func_val[0::7]
    ind_list = []
    for i in func_val:
        if type(i) == dict:
            a = func_val.index(i)
            ind_list.append(a)
            func_val.remove(i)
    for i in range(len(ind_list)):
        func_val.append('/')
    getting_str(func_val, list_data)
    assert type(getting_str(func_val, list_data)) == str
