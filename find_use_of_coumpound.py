import openpyxl
import random
import JSON_Data_Formatter
import json

class Compound:
    def __init__(self, common_name, compound_name, formula ,uses):
        self.common_name = common_name
        self.compound_name = compound_name
        self.formula = formula
        self.uses = uses    

def get_random_row_number(complexity):
    complexity-=1
    ranges = [(1, 5), (10, 15), (16, 20), (21, 25), (26, 30), (31, 56)]
    return random.randint(ranges[complexity][0], ranges[complexity][1])

def get_compound(row_number, sheet_obj):
    
    lst = []
    for i in range(1, 5):
        cell_obj = sheet_obj.cell(row = row_number, column = i)
        value = str(cell_obj.value)
        lst.append(value)
    compound = Compound(lst[0], lst[1], lst[2], lst[3])
    return compound

def generate_useof_compound_question(complexity, path):
    
    author_name  = "J.Muthuganesh"
    author_GUID = "2694eda7-bf11-4164-8dc7-3fade156b81a"
    reviewer_name  = "T.Jagadeesh"
    reviewer_GUID = "cd475300-1e30-4cc0-9c1a-55af79624af3"
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    question = "What is the use of "
    row_number = get_random_row_number(complexity)
    compound = get_compound(row_number, sheet_obj)

    if(complexity == 1):
        question += compound.common_name
    elif(complexity == 2):
        question += compound.compound_name
    else:
        question += compound.formula
    answer = compound.uses
    options = []

    for i in range(3):
        row_number = get_random_row_number(complexity)
        use = get_compound(row_number, sheet_obj).uses
        while(use in options):
            row_number = get_random_row_number(complexity)
            use = get_compound(row_number, sheet_obj).uses

        options.append(use)

    options.append(answer)
    random.shuffle(options)
    data = JSON_Data_Formatter.format_to_json(author_GUID, author_name, reviewer_GUID, reviewer_name, question, options
    , "", answer , 4)
    print(json.dumps(data))
    return json.dumps(data)
    