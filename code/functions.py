from utils import open_json_file

remittance = open_json_file()


def get_successful_op(remittance):
    """Функция обрабатывает документ, выводя список значений операций.
    Затем из общего списка операций убирает не удачные, возвращает успешные"""
    index_list = []
    list_values = []
    for i in range(len(remittance)):
        for v in remittance[i].values():
            list_values.append(v)
    for numb in range(len(list_values)):
        if list_values[numb] == 'CANCELED':
            index_list.append(numb)
    index_list.reverse()
    for ind in index_list:
        del list_values[ind:ind+7]
    return list_values

