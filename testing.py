# # from pylatexenc.latexencode import unicode_to_latex

# # str_lst = []

# # str_lst.append(unicode_to_latex("hello hi"))
# # print(str_lst)

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.linspace(-5,5,100)
# y = ((2/3)*x+(1/3))**0.5
# plt.plot(x, y, '-r', label='')
# plt.title('Find Equation Of Graph')
# plt.xlabel('x', color='#1C2833')
# plt.ylabel('y', color='#1C2833')
# plt.legend(loc='upper left')
# plt.grid()
# plt.show()
import random
import json
import math

# AUTHOR_GUID = 'b34daa08-6536-4973-9370-5396307b6897'
# AUTHOR_NAME = "S.Namratha"
# REVIEWVER_GUID = ''
# REVIEWVER_NAME = ''

#Function to generate radius

def getRandomFunction(complexity):
    start_range = (10 * complexity)
    end_range = 10 * (complexity ** 2)
    r = random.randint(start_range, end_range)
    return r
    
#Function to generate sphere question
def generate_circlequestion(complexity,no_of_responses):
    r=getRandomFunction(complexity)
    question = "Find the surface area of sphere with radius ",r," is "
    print(question)
    print("Options")
    correctanswer=float(4*3.14*r*r)
    options=[correctanswer]
    for _ in range(int(math.ceil(no_of_responses/2))):
        nearest=random.randint(1,5)
        options.append(correctanswer+nearest)
    for _ in range(no_of_responses//2):
        nearest=random.randint(5,10)
        options.append(correctanswer-nearest)
        random.shuffle(options)
        return options,question,correctanswer
        
#Function to generate sphere question
def surface_area(no_of_questions,complexity,no_of_responses):
    for i in range(no_of_questions):
        options,question,correctanswer=generate_circlequestion(complexity,no_of_responses)
        data = {}

        # data = {"Question": question, "Answers": []}
        # , "Credits": {"Author": {"id": AUTHOR_GUID, "Name": AUTHOR_NAME},
        #                                                          "Reviever": {"id": REVIEWVER_GUID,
        #                                                                       "Name": REVIEWVER_GUID}}}
        for i in range(len(options)):
            on = i+1
            answerdict={"id":i+1,"value":options[i],"is_key":False}
            if(options[i]==correctanswer):
                correct_option_number=on
                answerdict["is_key"]=True
            # data["Answers"].append(answerdict)
            print(i+1,':',options[i])
        # print("Correct Answer is:",correct_option_number,')',correctanswer)
        data["Correct Answer"]=str(correctanswer)
           
           
        print(json.dumps(data))
        data.clear()
    # return None
       
no_of_questions = int(input("Enter the number of questions: "))
no_of_responses = int(input("Enter the no of responses: "))
complexity = int(input("Enter the level of complexity: "))
print(surface_area(no_of_questions, complexity, no_of_responses))