from utils import open_json_file

remittance = open_json_file()


def get_successful_op(remittance):
    """Функция обрабатывает документ, выводя список значений операций,
    если ключ 'from' отсутствует в словаре, то он заменяется на значение '-'.
    Затем из общего списка операций убирает не удачные, возвращает успешные"""
    index_list = []
    list_values = []
    for i in range(len(remittance)):
        if 'description' in remittance[i]:
            if 'from' not in remittance[i]:
                remittance[i]['from'] = '-'
        for v in remittance[i].values():
            list_values.append(v)
    for numb in range(len(list_values)):
        if list_values[numb] == 'CANCELED':
            index_list.append(numb)
    index_list.reverse()
    for ind in index_list:
        del list_values[ind:ind+7]
    return list_values


list_val = get_successful_op(remittance)


def sorted_data(list_val):
    """Функция вытаскивает из списка дату операции,
    определяет последний год совершенной операции и сортирует от самой последней в данном году,
    до самой первой"""
    list_age = []
    list_month = []
    list_of_data = list_val[2::7]
    for i in list_of_data:
        if i[:4] not in list_age:
            list_age.append(i[:4])
        max_age = max(list_age)
        if i[:4] == max_age:
            list_month.append(i)
    list_month.sort(reverse=True)
    return list_month


list_sorted = sorted_data(list_val)


def getting_index(list_val, list_sorted):
    """Функция находит индексы последних 5ти операций"""
    list_index = []
    del list_sorted[5:]
    for val in list_sorted:
        ind = list_val.index(val)
        list_index.append(ind)
    return list_index


list_index = getting_index(list_val, list_sorted)


def getting_date_output(list_val, list_sorted, list_index):
    """Функция возвращает список значений 5ти совершенных операций:
    дата-операция-откуда-куда-сумма"""
    list_data = []
    del list_sorted[5:]
    for st in list_sorted:
        raw_string = st
        string = raw_string.replace('-', 'T')
        string = string.split('T')
        del string[-1]
        data_string = string[2] + '.' + string[1] + '.' + string[0]
        list_data.append(data_string)
        for ind in list_index:
            list_values = list_val[ind+1:ind+5]
            string_description = list_values[1]
            list_data.append(string_description)
            string_to = list_values[-2]
            list_data.append(string_to)
            list_data.append('->')
            string_from = list_values[-1]
            list_data.append(string_from)
            string_summ = list_values[0]['amount'] + ' ' + list_values[0]['currency']['name']
            list_data.append(string_summ)
    return list_data


print(getting_date_output(list_val, list_sorted, list_index))