import time
import json
import xmltodict
import basic_task
import task_2


def one_hundred(function, arg):
    start = time.time()
    for i in range(100):
        function(arg)
    end = time.time()
    return end - start


if __name__ == '__main__':
    in_file = open('schedule.xml', "r", encoding="utf8").read()
    out_file = open("task_1.json", "w", encoding="utf8")
    print("Стократное время парсинга XML")
    print("Базовое задание:", one_hundred(basic_task.parse_xml, in_file))
    print("Библиотека xmltodict:", one_hundred(xmltodict.parse, in_file))
    print("Регулярные выражения:", one_hundred(task_2.parse_xml, in_file))
    dictionary = xmltodict.parse(in_file)
    print()
    print("Стократное время формирования JSON")
    print("Базовое задание:", one_hundred(basic_task.form_json, dictionary))
    print("Библиотека json:", one_hundred(json.dumps, dictionary))


