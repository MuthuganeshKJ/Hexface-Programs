from itertools import permutations
import Random_data_generation
import numpy as np
import LaTexFormatters
import random
import JSON_Data_Formatter
import json
def vector_addition_question_generator(type_complexity, complexity):

    author_name  = "J.Muthuganesh"
    author_GUID = "2694eda7-bf11-4164-8dc7-3fade156b81a"
    reviewer_name  = "T.Jagadeesh"
    reviewer_GUID = "cd475300-1e30-4cc0-9c1a-55af79624af3"

    question_list = []
    options = []
    question = "ADD : "

    for i in range(type_complexity):
        question_list.append(np.array(Random_data_generation.get_random_vector(complexity)))
        if(i==0):
            c = question_list[-1]
            question += LaTexFormatters.format_vector_latex(question_list[-1])
            options.append(LaTexFormatters.format_vector_latex(c))

        else:
            c += question_list[-1]
            question += (" + " + LaTexFormatters.format_vector_latex(question_list[-1]))
            if(i<type_complexity):
                options.append(LaTexFormatters.format_vector_latex(question_list[-1]))
                options.append(LaTexFormatters.format_vector_latex(c))

    diff = permutations([1, 1, 1, -1, -1, -1], 3)

    for ele in list(diff):
        opp = []
        for j in range(3):
            opp.append(c[j]+ele[j])

        options.append(LaTexFormatters.format_vector_latex(opp))

    random.shuffle(options)
    options = list(options)[:3]
    options.append(LaTexFormatters.format_vector_latex(c))
    random.shuffle(options)

    answer = LaTexFormatters.format_vector_latex(c)

    print(question)
    print(options)

    data = JSON_Data_Formatter.format_to_json(author_GUID, author_name, reviewer_GUID, reviewer_name, question, options, "", answer, 4)
    print(json.dumps(data))

    return json.dumps(data)
vector_addition_question_generator(2, 2)
