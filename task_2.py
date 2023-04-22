from basic_task import form_json
import re


def parse_xml(file):
    dictionary = {}
    while file.find("<") != -1:
        tag = re.findall("<.*?>", file)
        if len(tag) == 0:
            break
        tag = tag[0][1:-1]
        open_tag = "<" + tag + ">"
        close_tag = "<\/" + tag + ">"
        text = re.findall(open_tag + "[\\S\\s]*?" + close_tag, file)[0][len(open_tag):-len(close_tag) + 1]

        file = file.replace("<" + tag + ">" + text + "</" + tag + ">", "", 1)

        if tag in dictionary.keys():
            old_text = dictionary[tag]
            if type(old_text) == list:
                old_text.append(text)
                text = old_text
            else:
                text = [old_text, text]
        dictionary[tag] = text

        for tag in dictionary.keys():
            text = dictionary[tag]

            if type(text) == list:
                new_list = []
                for item in text:
                    if type(item) == str and item.find('<'):
                        new_list.append(parse_xml(item))
                    else:
                        new_list.append(item)
                dictionary[tag] = new_list
            elif type(text) == str:
                if text.find('<') != -1:
                    dictionary[tag] = parse_xml(text)

    return dictionary


def task_2():
    in_file = open('schedule.xml', "r", encoding="utf8").read()
    out_file = open("task_2.json", "w", encoding="utf8")
    out_file.write(form_json(parse_xml(in_file)))


if __name__ == '__main__':
    task_2()
