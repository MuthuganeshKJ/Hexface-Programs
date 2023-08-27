# Contributions: J.Muthuganesh
import random
import json
import JSON_Data_Formatter
from click import option
import Random_data_generation
import LatexFormatters

def add_complex_numbers(complex_number_list):
    '''Function to add a list of complex numbers'''

    answer = complex_number_list[0]
    for cn in complex_number_list[1:]:
        answer+=cn
    return answer

def generate_complexnumber_addition_question(complexity, option_count):

    '''Parameters
    -> complexity Integer between 1-5
    -> option_count Integer represents the number of options to be generated
    '''

    author_name  = "J.Muthuganesh"
    author_GUID = "2694eda7-bf11-4164-8dc7-3fade156b81a"
    reviewer_name  = "Jhon Buer"
    reviewer_GUID = "2694eda7-bf11-4164-8dc7-3fade156b81a"
    complex_number_list = []

    '''Generating Qustion String'''
    question = "Solve: "
    for i in range(complexity+1):
        cn = Random_data_generation.get_random_complexnumber(complexity)

        if(i == 0):
            question += LatexFormatters.format_complexnumber_latex(cn.real, cn.imag)
        else:
            question += " + "+ LatexFormatters.format_complexnumber_latex(cn.real, cn.imag)
        complex_number_list.append(cn)

    answer = add_complex_numbers(complex_number_list)

    '''Generating Options based on common mistakes done by user in solving the question'''
    options = []
    ct = option_count-1
    options.append(complex(answer.imag, answer.real))
    ct-=1
    options.append(complex(answer.imag, 0))
    ct-=1
    options.append(complex(answer.real + answer.imag, 0))
    ct-=1
    options.append(complex(answer.imag, answer.imag))
    ct-=1
    options.append(complex(answer.real, answer.real))
    ct-=1
    index = 1
    while(ct>0):
        options.append(add_complex_numbers(complex_number_list[index:]))
        index+=1
        ct-=1
    random.shuffle(options)
    
    print(question)
    options = options[:option_count-1]
    options.append(answer)
    random.shuffle(options)
    print(options)
    print(answer)
 
    latex_answer = LatexFormatters.format_complexnumber_latex(answer.real, answer.imag)
    print(latex_answer)
    latex_formatted_options  = []
    for cn in options:
        latex_formatted_option = LatexFormatters.format_complexnumber_latex(cn.real, cn.imag)
        latex_formatted_options.append(latex_formatted_option)

    data = JSON_Data_Formatter.format_to_json(author_GUID, author_name, reviewer_GUID, reviewer_name, question, latex_formatted_options, "", latex_answer, option_count)
    print(json.dumps(data))

    return json.dumps(data)

    
if __name__ == "__main__":
    generate_complexnumber_addition_question(3, 4)