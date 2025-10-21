import re
import os
import json


def find(structure, target_name):
    if structure["name"] == target_name:
        return structure
    if "child" in structure:
        for child in structure["child"]:
            result = find(child,target_name)
            if result:
                return result
    return None

def create_json(data, year):
    table_name = f'Tabell 1.1 Specifikation av budgetens utgifter för {year}'
    structure = {
        "name": table_name,
        "child": []
    }
    current_path = structure["name"] + "|"
    previous_bold = True
    last_bold_node = {}
    # for idx, item in enumerate(data):
    #     if item == []:
    #         print(data[idx-1])
    for item in data[:-1]:
        if item[0][0] == "15 BOLD Tillsyn över spelmarknaden":
            print("hej")
        node = {
                "name": item[0][0],
                "value": item[0][3],
                "is_bold": "BOLD" in item[0][0],
            }
        if node["name"] == '2 Konsumentpolitik':
            print("hello")

        if "BOLD" in item[0][0]:
            if previous_bold == False:
                splited = current_path.split("|")
                    
                splited = splited[:-2]
                if int(last_bold_node["name"].split(" ")[0]) +1 != int(node["name"].split(" ")[0]):
                    if len(splited[:-1]) != 0:
                        print("tjatja - splitted ska vara här")
                        splited = splited[:-1]

                current_path = ""
                for split in splited:
                    print(split)
                    current_path += split + "|" 
                    print(structure["name"] + "|")

            node["child"] = []
            current_path += item[0][0] + "|"

            print(current_path) 
            if len(structure) == 0:
                structure = node
            else: 
                findRes = find(structure, current_path.split("|")[:-2][-1]) 
                findRes["child"].append(node)
            
            last_bold_node = node
            previous_bold = True
        else: 

            findRes = find(structure, current_path.split("|")[:-1][-1])
            findRes["child"].append(node)
            previous_bold = False
    print(structure)
    return structure

if __name__ =="__main__":
    folder_path = "budgettxt"
    print(os.listdir(folder_path))
    for filename in os.listdir(folder_path):

        year = filename.split("-budget.txt")[0]
        print(year)
        print(f'{folder_path}/{filename}')
        f = open(f'{folder_path}/{filename}')
    
        data = []
        pattern1 = "^([0-9]+[-–]?[0-9]* ?[A-ö][^\d]+\n?([0-9]{4}(-|–)\n?[0-9]{4})?) (-?[0-9 ]+$)"
        pattern2 = "^(S[a-ö ]+|T[a-ö ]+|O[a-ö ]+)[A-ö ]+([0-9]\.[0-9])?([A-ö ]+)?([0-9 ]+)$"

        regex = f'{pattern1}|{pattern2}'
        for line in f:
            matches = re.findall(regex, line)
            data.append((matches))

        parsed_data = create_json(data, year)
        # return json
        with open (f'json/new_{year}_budget.json', 'w', encoding="utf-8") as f:
            json.dump(parsed_data, f, indent=2,ensure_ascii=False)
        with open(f'json/new_{year}_budget_minimized.json', 'w', encoding="utf-8") as f:
            json.dump(parsed_data, f, ensure_ascii=False, separators=(',', ':'))