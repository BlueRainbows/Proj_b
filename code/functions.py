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


def getting_date_output(list_sorted):
    """Функция возвращает список последних 5ти дат операций"""
    list_of_op = []
    del list_sorted[5:]
    for st in list_sorted:
        raw_string = st
        string = raw_string.replace('-', 'T')
        string = string.split('T')
        del string[-1]
        data_string = string[2] + '.' + string[1] + '.' + string[0]
        list_of_op.append(data_string)
    return list_of_op


def getting_index(list_val, list_sorted):
    """Функция находит индексы последних 5ти операций"""
    list_index = []
    del list_sorted[5:]
    for val in list_sorted:
        ind = list_val.index(val)
        list_index.append(ind)
    return list_index


def get_op_output(list_val, list_index):
    list_data = []
    for ind in list_index:
        list_values = list_val[ind+1:ind+5]
        string_description = list_values[1]
        list_data.append(string_description)
        string_to = list_values[-2]
        raw_to = string_to.split(' ')
        creating_to = raw_to[-1]
        slices = creating_to.replace(creating_to[6:-4], '** **** ')
        srt_dig_to = creating_to[:4] + ' '
        slices = slices.replace(creating_to[:4], srt_dig_to)
        del raw_to[-1]
        raw_to = ' '.join(raw_to)
        slices = raw_to + ' ' + slices
        list_data.append(slices)
        string_from = list_values[-1]
        if string_from != '-':
            raw_from = string_from.split(' ')
            creating_from = raw_from[-1]
            slices_from = creating_from.replace(creating_from[6:-4], '** **** ')
            srt_dig_from = creating_from[:4] + ' '
            slices_from = slices.replace(creating_from[:4], srt_dig_from)
            del raw_from[-1]
            raw_from = ' '.join(raw_from)
            slices_from = raw_from + ' ' + slices_from
            list_data.append(slices_from)
        else:
            list_data.append(string_from)
        string_summ = list_values[0]['amount'] + ' ' + list_values[0]['currency']['name']
        list_data.append(string_summ)
    return list_data


def getting_str(text_data, data_output):
    operation = text_data[0::4]
    account_to = text_data[1::4]
    account_from = text_data[2::4]
    summ = text_data[3::4]
    list_of_str = []
    clear_str = ''
    for d in range(len(data_output)):
        string_1 = data_output[d] + ' ' + operation[d] + '\n' + account_to[d] + ' -> ' + account_from[d] + '\n' + summ[d] + '\n'
        list_of_str.append(string_1)
    for st in list_of_str:
        clear_str += st + '\n'
    return clear_str
