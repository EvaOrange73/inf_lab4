def parse_xml(file):
    dictionary = {}
    tag = ""
    text = ""
    tag_start = False
    text_start = False
    for i, ch in enumerate(file):
        if not text_start:
            if not tag_start:
                if ch == '<':
                    tag_start = True
            else:
                if ch == '>':
                    tag_start = False
                    text_start = True
                else:
                    tag += ch
        else:
            if ch == '<':
                if tag + '>' == file[i + 2: i + len(tag) + 3]:
                    text_start = False
                    if tag in dictionary.keys():
                        old_text = dictionary[tag]
                        if type(old_text) == list:
                            old_text.append(text)
                            text = old_text
                        else:
                            text = [old_text, text]
                    dictionary[tag] = text
                    tag = ""
                    text = ""
                    continue
            text += ch

    for tag in dictionary.keys():
        text = dictionary[tag]
        if type(text) == list:
            new_list = []
            for item in text:
                if item.find('<'):
                    new_list.append(parse_xml(item))
                else:
                    new_list.append(item)
            dictionary[tag] = new_list
        else:
            if text.find('<') != -1:
                dictionary[tag] = parse_xml(text)
    return dictionary


def form_json(dictionary):
    json = "{"
    for tag in dictionary.keys():
        json += "\"" + tag + "\": "
        text = dictionary[tag]
        if type(text) == dict:
            json += form_json(text)
        elif type(text) == list:
            json += "["
            for item in text:
                json += form_json(item) + ", "
            json = json[:-2]
            json += "]"
        else:
            json += "\"" + text + "\""
        json += ", "
    json = json[:-2]
    json += "}"
    return json


def basic_task():
    in_file = open('schedule.xml', "r", encoding="utf8").read()
    out_file = open("basic_task.json", "w", encoding="utf8")
    out_file.write(form_json(parse_xml(in_file)))


if __name__ == '__main__':
    basic_task()
