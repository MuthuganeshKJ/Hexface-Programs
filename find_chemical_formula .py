from click import option
from requests import options
import find_use_of_coumpound
import openpyxl
import random
import JSON_Data_Formatter
import json
from pylatexenc.latexencode import unicode_to_latex
def generate_find_chemical_formula_question(complexity, path):
    author_name  = "J.Muthuganesh"
    author_GUID = "2694eda7-bf11-4164-8dc7-3fade156b81a"
    reviewer_name  = "T.Jagadeesh"
    reviewer_GUID = "cd475300-1e30-4cc0-9c1a-55af79624af3"
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    row_number = find_use_of_coumpound.get_random_row_number(complexity)
    compound = find_use_of_coumpound.get_compound(row_number, sheet_obj)
    question = "Find the chemical formula of: " + compound.compound_name
    answer = compound.formula

    total_row_count = sheet_obj.max_row
    temp = list(map(str, compound.compound_name))
    first_name = temp[0]
    
    options = []
    for i in range(2, total_row_count+1):
        temp = find_use_of_coumpound.get_compound(i, sheet_obj)

        if(first_name in temp.compound_name and temp.formula not in options and temp.formula!=answer):
            options.append(temp.formula)

    row_count = 2
    while(len(options)<3):
        value = find_use_of_coumpound.get_compound(row_count, sheet_obj).formula
        while(value in options and value != answer):
            row_count+=1
            value = find_use_of_coumpound.get_compound(row_count, sheet_obj).formula
        options.append(value)            

    print(question)
    random.shuffle(options)
    options = list(options[:3])
    options.append(answer)
    random.shuffle(options)
    print(answer)
    print(options)
    data = JSON_Data_Formatter.format_to_json(author_GUID, author_name, reviewer_GUID, reviewer_name, question, options
    , "", answer , 4)
    print(json.dumps(data))
    return json.dumps(data)

generate_find_chemical_formula_question(2, "E:\Hexface Programs\Excel_data\Chemical Compound Uses.xlsx")

