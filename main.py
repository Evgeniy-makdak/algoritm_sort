import csv


def select_sorted(sort_columns=["high"], limit=30, group_by_name=False, order='desc', filename='dump.csv'):
    is_reverse = True if order == 'asc' else False
    fields = ['date', 'open', 'high', 'low', 'close', 'volume', 'Name']

    dictobj = csv.DictReader(open('all_stocks_5yr.csv'))  # чтение данных
    if len(sort_columns) == 1:  # сортировка по одному полю
        list_rows = sorted(dictobj, key=lambda d: d[sort_columns[0]], reverse=is_reverse)
    elif len(sort_columns) == 2:  # сортировка по 2 полям
        list_rows = sorted(dictobj, key=lambda d: (d[sort_columns[0]],
                                                   d[sort_columns[1]]), reverse=is_reverse)
    elif len(sort_columns) == 3:  # сортировка по 3 полям
        list_rows = sorted(dictobj, key=lambda d: (d[sort_columns[0]],
                                                   d[sort_columns[1]],
                                                   d[sort_columns[2]]), reverse=is_reverse)
    elif len(sort_columns) == 4:  # сортировка по 4 полям
        list_rows = sorted(dictobj, key=lambda d: (d[sort_columns[0]],
                                                   d[sort_columns[1]],
                                                   d[sort_columns[2]],
                                                   d[sort_columns[3]]), reverse=is_reverse)
    elif len(sort_columns) == 5:  # сортировка по 5 полям
        list_rows = sorted(dictobj, key=lambda d: (d[sort_columns[0]],
                                                   d[sort_columns[1]],
                                                   d[sort_columns[2]],
                                                   d[sort_columns[3]],
                                                   d[sort_columns[4]]), reverse=is_reverse)
    elif len(sort_columns) == 6:  # сортировка по 6 полям
        list_rows = sorted(dictobj, key=lambda d: (d[sort_columns[0]],
                                                   d[sort_columns[1]],
                                                   d[sort_columns[2]],
                                                   d[sort_columns[3]],
                                                   d[sort_columns[4]],
                                                   d[sort_columns[5]]), reverse=is_reverse)
    else:
        list_rows = sorted(dictobj, key=lambda d: d["high"], reverse=is_reverse)

    list_rows = list_rows[:limit]  # берем срез нужного количества

    dict_rows = {}  # если нужна группировка по имени
    if group_by_name:
        for each in list_rows:
            name = each["Name"]
            if name in dict_rows:
                m_dict = dict_rows[name]
                m_dict['date'] = min(m_dict['date'], each['date'])
                for i in fields[1:-2]:
                    m_dict[i] = str((float(m_dict[i]) + float(each[i])) / 2)
                m_dict['volume'] = str(int(m_dict['volume']) + int(each['volume']))
                m_dict['Name'] = each['Name']
                dict_rows[name] = m_dict

            else:
                dict_rows[name] = each
        list_rows = dict_rows.values()

    writer = csv.DictWriter(open(filename, "w", newline=''), fieldnames=fields)  # запись данных
    writer.writeheader()
    for i in list_rows:
        writer.writerow(i)
    return list(list_rows)

if __name__ == '__main__':
    # пример использования
    rez = select_sorted(sort_columns=["high", "close"], limit=10, group_by_name=False, order='asc', filename='dump.csv')
    for each in rez:
        print(each)

