import xmltodict
import csv


def form_headers(dictionary):
    headers = []
    for key, value in dictionary.items():
        if type(value) == dict:
            headers.extend(form_headers(value))
        elif type(value) == list:
            headers.extend(form_headers(value[0]))
        else:
            headers.append(key)
    return headers


def find_content():
    pass


def form_rows(dictionary, headers, current_rows=None):
    if current_rows is None:
        current_rows = [[0] * len(headers)]
    rows = []

    for key, value in dictionary.items():
        if type(value) == dict:
            current_rows = form_rows(value, headers, current_rows)
        elif type(value) == list:
            new_current_rows = []
            for val in value:
                new_current_rows.append(form_rows(val, headers, current_rows)[0].copy())
            current_rows = new_current_rows
        else:
            for current_row in current_rows:
                current_row[headers.index(key)] = value
    rows.extend(current_rows)
    return rows


def form_csv_file(dictionary, name):
    out_file = open(name, 'w', newline='')
    writer = csv.writer(out_file)
    headers = form_headers(dictionary)
    writer.writerow(headers)
    rows = form_rows(dictionary, headers)
    for row in rows:
        writer.writerow(row)


def task_4():
    in_file = open('schedule.xml', "r", encoding="utf8").read()
    dictionary = xmltodict.parse(in_file)
    form_csv_file(dictionary, "main_table.csv")


if __name__ == '__main__':
    task_4()
