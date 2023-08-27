# Credits: J.Muthuganesh program version: 1.0
from gtts import gTTS
import openpyxl
import os
import random
import JSON_Data_Formatter

from sqlalchemy import column

def get_word(sheet_obj, complexity):
    row_number = random.randint(2, 173)
    word = sheet_obj.cell(row = row_number, column = complexity)
    return word.value

def generate_spell_bee_question(path):
    '''
        Path: path of excel file with words
        Complexity is determined by length of word
        Audio file saved with name of the word
    '''

    author_name  = "J.Muthuganesh"
    author_GUID = "2694eda7-bf11-4164-8dc7-3fade156b81a"
    reviewer_name  = "T.Jagadeesh"
    reviewer_GUID = "cd475300-1e30-4cc0-9c1a-55af79624af3"
    question = "Spell the word after listening to the audio carefully"

    wb_obj = openpyxl.load_workbook("E:\\Hexface Programs\\Excel_data\\words.xlsx")
    sheet_obj = wb_obj.active
    word = get_word(sheet_obj, 1)
    print(word)
    language = 'en'
    myobj = gTTS(text=word, lang=language, slow=None)
    file_name = word+".mp3"
    print(file_name)
    answer = word
    myobj.save(file_name)
    os.system(file_name)
    data = JSON_Data_Formatter.format_spell_bee_question_to_json(author_GUID, author_name, reviewer_GUID, reviewer_name, question, file_name, "", answer)
    print(data)
    return data

generate_spell_bee_question("E:\\Hexface Programs\\Excel_data\\words.xlsx")
