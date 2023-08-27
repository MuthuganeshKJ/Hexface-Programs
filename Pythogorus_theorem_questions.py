import Random_data_generation as rdg
import random
import JSON_Data_Formatter
import json

def get_random_pythagorus_triplet(complexity):
   
    complexity_list = [(1, 5), (6, 10), (11, 15), (16, 20), (21, 25)]

    starting_range = complexity_list[complexity-1][0]
    ending_range = complexity_list[complexity-1][1]
    m = random.randint(starting_range+1, ending_range)
    n = random.randint(starting_range, m-1)

    while(rdg.compute_hcf(m, n)==0):
        m = random.randint(starting_range+1, ending_range)
        n = random.randint(starting_range, m-1)

    a = abs((m*m)-(n*n))
    b = 2*m*n
    c = abs((m*m)+(n*n))

    return [a, b, c]

def first_level_question(author_GUID, author_name, reviewer_GUID, reviewer_name, a, b, c, option_count):

    triples = [a, b, c]
    triples = list(triples)
    random.shuffle(triples)
    answer = str(triples[-1])
    question = "find the third side of the right angle triangle if the two side are "+str(triples[0])+" and "+str(triples[1])+" ?"
    options = []

    for e in range(int(answer)+1, int(answer)+5):
        options.append(str(e))
    for e in range(int(answer)-5, int(answer)-1):
        options.append(str(e))
    options.append(str(int(a*b**0.5)))
    options.append(str(int(a*a**0.5)))
    options.append(str(int(b*b**0.5)))
    options.append(str(b+a))
    options.append(str(int(b*a*2**0.5)))
    random.shuffle(options)
    options = list(options[:option_count-1])
    options.append(answer)
    random.shuffle(options)

    return JSON_Data_Formatter.format_to_json(author_GUID, author_name, reviewer_GUID, reviewer_name, question, options, "", answer, option_count)

def create_answer(option_list, correct_option_list, max_answer_count):
    op_no = 1
    ct=0
    answer = ''
    for option in option_list:
        if(option in correct_option_list):
            if(ct==0):
                answer += str(op_no)
            else:
                answer += ' and ' + str(op_no)
            ct+=1
        op_no+=1  
    if(answer == ""):
        answer = "none of the above"
    elif(len(answer) == 1):
        answer = "only " + answer
    elif(ct == max_answer_count):
        answer = "all of the above"
    else:
        answer = "both "+ answer
    return answer

def second_level_question(author_GUID, author_name, reviewer_GUID, reviewer_name, complexity):
    triple_list = []
    question_list = []
    for i in range(3):
        triple_list.append(get_random_pythagorus_triplet(complexity))
        question_list.append(triple_list[-1])

    for i in range(3):
        lst = []
        for j in range(3):
            diff = random.randint(-3,3)
            lst.append(triple_list[i][j]+diff)
        
        while(lst in triple_list):
            for j in range(3):
                diff = random.randint(-3,3)
                lst.append(triple_list[i][j]+diff)
        random.shuffle(lst)
        question_list.append(list(lst))
        
    random.shuffle(question_list)
    question_list = list(question_list[:3])
    answer = ""

    op_no = 1

    answer = create_answer(question_list, triple_list, 3)

    print(triple_list) 
    print(question_list)
    
    answer = answer.strip()
    answer = answer.replace(" ", "\,\,")

    options = ["only\,\,1", "only\,\,2", "only\,\,3", "both\,\,1\,\,and\,\,2", "both\,\,2\,\,and\,\,3", "both\,\,1\,\,and\,\,3", "All\,\,of\,\,the\,\,above", "none\,\,of\,\,the\,\,above"]
    
    # for i in range(len(options)):
    #     options[i] = LatexFormatters.format_text_to_latex(str(options[i]))
        
    op_no = 1

    question = "Find\,\,the\,\,Pythagorian\,\,triplet\,\,among\,\,the\,\,following: "
    for option in question_list:
        question+="\\\\"+ str(op_no) +") "+ str(option)
        op_no+=1
    print(question)
    for option in options:
        print(option)
    print("Answer: " +answer)
    data = JSON_Data_Formatter.format_to_json(author_GUID, author_name, reviewer_GUID, reviewer_name, question, options, "", answer, 8)

    return data

def generate_pythagorous_question(type_complexity, complexity):
    '''
        type_complexity - refers the type of the question
        complexity - refers the complexity of the values in question'''
    author_name  = "J.Muthuganesh"
    author_GUID = "2694eda7-bf11-4164-8dc7-3fade156b81a"
    reviewer_name  = "J.Muthuganesh"
    reviewer_GUID = "2694eda7-bf11-4164-8dc7-3fade156b81a"

    a, b, c = map(int, get_random_pythagorus_triplet(complexity))

    if(type_complexity==1):
        print(json.dumps(first_level_question(author_GUID, author_name, reviewer_GUID, reviewer_name, a, b, c, 4)))
        return json.dumps(first_level_question(author_GUID, author_name, reviewer_GUID, reviewer_name, a, b, c, 4))
    else:
        print(json.dumps(second_level_question(author_GUID, author_name, reviewer_GUID, reviewer_name, 2)))
        return json.dumps(second_level_question(author_GUID, author_name, reviewer_GUID, reviewer_name, 2))

if __name__ == '__main__':
    generate_pythagorous_question(2, 2)







