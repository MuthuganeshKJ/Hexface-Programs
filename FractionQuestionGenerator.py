# J.Muthuganesh - 2694eda7-bf11-4164-8dc7-3fade156b81a

import random
import math;
from fractions import Fraction ;
import json
from unicodedata import name
from click import option

from numpy import true_divide
from pyrsistent import l;

#\frac{a}{b}
#FUNCTION TO GENERATE A RANDOM FRACTION USING THE GIVEN COMPLEXITY
def get_random_fraction(complexity):
    
    startRange = (10**(complexity-1));
    endRange = 10**complexity + 1;
    a = random.randint(startRange, endRange)
    b = random.randint(startRange, endRange)
    while(a==b):
        b = random.randint(startRange, endRange)
    
    return Fraction(a, b);

def gen_latex(frac):
    if('/' not in str(frac)):
        return str(frac)

    num, den = str(frac).split('/')
    return "\frac{"+str(num)+"}{"+(str(den))+"}"


#RANDOM QUESTION GENERATING FUNCTION    
def generate_fraction_question(operation, complexity, option_count):

    '''Parameters
    -> Operations - operation + or - Optional
    -> complexity - Integer 1 to 5
    -> option_count - Integer represents number of options maximum 4'''
    author_name  = "J.Muthuganesh"
    author_GUID = "2694eda7-bf11-4164-8dc7-3fade156b81a"
    reviewer_name  = "J.Muthuganesh"
    reviewer_GUID = "2694eda7-bf11-4164-8dc7-3fade156b81a"
    operation_list = ["+", "-"]
    
    if(not operation):
        random.shuffle(operation_list)
        operation_list = list(operation_list)
        operation = operation_list[0]
        
    f1 = get_random_fraction(complexity)
    f2 = get_random_fraction(complexity)
    if('/' not in str(f1)):
        while('/' not in str(f2)):
            f2 = get_random_fraction(complexity)

    lf1 = gen_latex(f1)
    
    lf2 = gen_latex(f2) 
    question = lf1+ operation + lf2+' = '+ '?';
    print("Options")
    if(operation == '+'):
        correct_answer = f1+f2
    else:
        correct_answer = f1-f2
   
    options = []
    temp_option_count = option_count
    
    '''Most Common Mistakes In Fraction Addition
        -> wrong LCM
        -> just adding numerator and dinominator
        -> just adding numerator or dinominator
        '''

    options.append(Fraction(f1.numerator+f2.numerator, f1.denominator+f2.denominator))

    options.append(Fraction(f1.numerator+f2.numerator, f1.denominator))
  
    options.append(Fraction(f1.numerator+f2.numerator, f2.denominator))
    
    options.append(Fraction(f1.numerator+f2.numerator, f1.denominator*f2.denominator))

    opp = (Fraction(f1.numerator+f2.numerator, correct_answer.denominator))
    if(opp != correct_answer):
        options.append(opp)
        option_count-=1

    options.append(Fraction(correct_answer.numerator+1, correct_answer.denominator-1))    
    options.append(Fraction(correct_answer.numerator-1, correct_answer.denominator+1))    
    options.append(Fraction(correct_answer.numerator+1, correct_answer.denominator+1))
    options.append(Fraction(correct_answer.numerator-1, correct_answer.denominator-1))

    random.shuffle(options)

    options = list(options[:3])

    #Adding Correct answer to list
    options.append(correct_answer)

    #shuffling th options
    random.shuffle(options)

    for i in range(option_count):
        ans = get_random_fraction(complexity)
        while(ans in options):
            ans = get_random_fraction(complexity)
        options.append(ans)
        
    random.shuffle(options)
    data = {}
    data={"content" : question, "answer":[], "hint": "", "credits": {
    "author": { "id": author_GUID, "name": author_name},
    "reviewer": { "id": reviewer_GUID, "name": reviewer_name}
    }}

    print(options)
    for i in range(temp_option_count):
        answer_dict = {}
        answer_dict["id"] = i+1;
        answer_dict["value"] = gen_latex(options[i]);
        if(options[i] == correct_answer):
            answer_dict["is_key"] = True
        data["answer"].append(answer_dict)    
        print(options[i])
            
    print(json.dumps(data)); 
    return json.dumps(data)

if __name__ == "__main__": 
    generate_fraction_question(False, 1, 3)