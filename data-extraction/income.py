import re
import json
import os

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
    table_name = f'Tabell 1.1 Specifikation av budgetens inkomster för {year}'
    structure = {
        "name": table_name,
        "child": []
    }
    current_path = structure["name"] + "|"
    previous_bold = True
    last_bold_node = {}

    for item in data:
        print(item)
        if len(item[0]) == 2:
            print("tja")
  
        else:
            node = {
                    "name": item[0][0] + item[0][2],
                    "value": item[0][4],
                    "is_bold": "BOLD" in item[0][2],
                    "is_italic": "ITALIC" in item[0][2],
                }

            if "BOLD" in item[0][2] or "ITALIC" in item[0][2]:
                if previous_bold == False:
                    splited = current_path.split("|")
                        
                    splited = splited[:-2]
                    # if int(last_bold_node["name"].split(" ")[0]) +1 != int(node["name"].split(" ")[0]):
                    print(last_bold_node)
                    if last_bold_node["name"].split(" ")[0][0] != 0:
                        if len(splited[:-1]) != 0:
                            splited = splited[:-1]

                    current_path = ""
                    for split in splited:
                        current_path += split + "|" 

                node["child"] = []
                print(item[0])
                current_path += f'{item[0][0]}{item[0][2]}' + "|"

                if len(structure) == 0:
                    structure = node
                else: 
                    print("-find--res---")
                    print(current_path.split("|")[:-2][-1])
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

if __name__ == "__main__":
    folder_path = "budgettxt/income"
    for filename in os.listdir(folder_path):
        year = filename.split("-income.txt")[0]

        f = open(f'{folder_path}/{filename}')
        newlines = []

        for line in f:
            split_line = line.split(" ")
            if "00" in split_line[0]:
                split_line.insert(1, " BOLD")
            elif "0" in split_line[0]:
                split_line.insert(1, " ITALIC")
            else: 
                split_line.insert(1, " ")
            newlines.append(" ".join(split_line))
        pattern = "^([0-9]{4}(–[0-9]{4})?) ([A-Za-ö ,.:-]+([0-9]{4}–[0-9]{4})?) (-?[0-9]{1,3}.*)"
        # if pattern 1 does not give result then use pattern 2
        pattern2 = "^([A-ö ]+)([0-9]{1,3}.+)"
        data = []
        
        for line in newlines:
            matches = re.findall(pattern,line)
            if len(matches) == 0:
                matches = re.findall(pattern2, line)
                data.append([('', '', "BOLD " + matches[0][0], '', matches[0][1])])
            else:
                print(matches)
                data.append(matches)
        parsed_data = create_json(data, year)
        
        with open (f'json/income/new_{year}_budget_income.json', 'w', encoding="utf-8") as f:
            json.dump(parsed_data, f, indent=2,ensure_ascii=False)
        with open(f'json/income/new_{year}_budget_income_minimized.json', 'w', encoding="utf-8") as f:
            json.dump(parsed_data, f, ensure_ascii=False, separators=(',', ':'))