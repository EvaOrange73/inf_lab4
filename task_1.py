import xmltodict
import json


def task_1():
    in_file = open('schedule.xml', "r", encoding="utf8").read()
    out_file = open("task_1.json", "w", encoding="utf8")
    out_file.write(json.dumps(xmltodict.parse(in_file), ensure_ascii=False))


if __name__ == '__main__':
    task_1()



