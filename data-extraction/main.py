import re
from datetime import datetime
import json
import os
from PyPDF2 import PdfWriter, PdfReader

def current_Time(string):
    """
    prints current time
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("{} Time = {}".format(string, current_time))

def create_json(matches, end):
    """
    
    """
    nodes = []
    i = 0
    for match in matches:
        if i >= end-1:
            node = {
                "id": 0,
                "title": match[0][3],
                "value": match[0][6]
            }
            nodes.append(node)
            break
        row_number = match[0][0].split(" ")
        node = {
            "id": row_number[0],
            "title": match[0][0],
            "value": match[0][2]
        }
        nodes.append(node)
        i+=1
    return nodes

#full budget file
current_Time("Start")
filename = "budgetpropositionen-for-2023.pdf"
pattern = r"(Prop\. \d{4}\/\d{2}:1 Bilaga 1|Prop\.\d{4}\/\d{2}:1Bilaga1)"
match_data = []
pdf_writer = PdfWriter()

pdf_reader = PdfReader("budget/" + filename)
for index, page in enumerate(pdf_reader.pages): 
    print(index)

    text = page.extract_text()

    if re.search(pattern, text):
        match_data.append(index)
print(match_data)

print("time to create pdf")

with open("budget/" + filename, "rb") as pdf_file:
    pdf_reader = PdfReader(pdf_file)

    for page_number in match_data:

        page = pdf_reader.pages[page_number - 1]

        pdf_writer.add_page(page)

    output_file = f"revision/revision_{filename}"

with open(output_file, "wb") as output_pdf:
    pdf_writer.write(output_pdf)

current_Time("End")


#revision file
# filename = f"budgetpropositionen-for-2021.pdf"
path = f"revision/revision_{filename}"


pattern1 = "^([0-9]+[-–]?[0-9]* ?[A-ö][^\d]+\n?([0-9]{4}–\n?[0-9]{4})?) (-?[0-9 ]+$)"
pattern2 = "^(S[a-ö ]+|T[a-ö ]+|O[a-ö ]+)[A-ö ]+([0-9]\.[0-9])?([A-ö ]+)?([0-9 ]+)$"

regex = f'{pattern1}|{pattern2}'

match_data = []
with pdfplumber.open(path) as pdf:
    for page in pdf.pages: 

        text = page.extract_text_lines(x_tolerance=1)

        for tex in text:
            is_bold = False
            matches = re.findall(regex, tex["text"])
            if "bold" in tex["chars"][0]['fontname'].lower():
               is_bold = True

            if len(matches) != 0:
                match_data.append((matches, is_bold))
                matches = []


row_number = ""
index=""
for idx, match in enumerate(match_data):
    if match[0][0][3] == 'Tabell' and match[0][0][4]  == "2.2" or match[0][0][4]  == "2.1":

        index = idx
        break


json_structure = {}
current_parent = None
current_parent_id = 0
for i, (text, is_bold) in enumerate(match_data):
  if i == index:
      break
  if i == 0:
    current_parent = {'id': i+1, 'name': f'{text[0][3]} {text[0][4]} {text[0][5]} {text[0][6]}', 'child': []}
    json_structure = current_parent
  elif text[0][0] == '': 
    current_parent = {'id': i+1, 'name': text[0][3], 'value': text[0][6], 'is_bold': is_bold}
    json_structure['child'].append(current_parent)
  else: 
    child = {'id': i+1, 'name': text[0][0], 'value': text[0][2], 'is_bold': is_bold}
    current_parent['child'].append(child)

start_index = path.find('/') + 1
end_index = path.rfind('.')
if not os.path.exists("json/" + path[start_index:end_index] + ".json"):
    f = open("json/" + path[start_index:end_index] + ".json", "x")
else:
    f = open("json/" + path[start_index:end_index] + ".json", "w")
f.write(json.dumps(json_structure, indent=2, ensure_ascii=False))
f.close()

current_Time("End")
