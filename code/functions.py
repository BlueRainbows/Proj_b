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


# print(get_successful_op(remittance))
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


print(sorted_data(list_val))