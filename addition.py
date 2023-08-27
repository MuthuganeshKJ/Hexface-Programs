import json
import random
import math

# AUTHOR_GUID = '6daace42-bb63-4c2a-8785-038821f1be1a'
# AUTHOR_NAME = "S.Namratha"
# REVIEWVER_GUID = '2694eda7-bf11-4164-8dc7-3fade156b81a '
# REVIEWVER_NAME = 'J.Muthuganesh'


def getRandomFunction(complexity):
    # function to generate two random variables

    start_range = (10 * complexity)
    end_range = 10 * (complexity ** 2)
    a = random.randint(start_range, end_range)
    b = random.randint(start_range, end_range)
    while (a == b and b > 1):
        b = random.randint(1, start_range)

    return [a, b]

def question_generation(complexity, no_of_responses):
    number1 = getRandomFunction(complexity)[0]
    number2 = getRandomFunction(complexity)[1]
    question = f'Question:What is the sum of {str(number1)}+{str(number2)} is?'

    print(question)
    print("Options")
    correct_answer = number1 + number2
    nearest = correct_answer
    options = [correct_answer]
    for _ in range(int(math.ceil(no_of_responses / 2)) - 1):
        nearest = random.randint(1, 5)
        options.append(correct_answer + nearest)

    for _ in range(no_of_responses // 2):
        nearest = random.randint(5, 10)
        options.append(correct_answer - nearest)

    random.shuffle(options)

    return  options, question, correct_answer



def sum(no_of_questions, comlexity, no_of_responses):
    # function to generate random questions
    for i in range(no_of_questions):
        options, question, correct_answer = question_generation(comlexity, no_of_responses)
        data = {}

        # data = {"Question": question, "Answers": []}
        # , "Credits": {"Author": {"id": AUTHOR_GUID, "Name": AUTHOR_NAME},
        #                                                          "Reviever": {"id": REVIEWVER_GUID,
        #                                                                       "Name": REVIEWVER_GUID}}}

        for i in range(len(options)):
            on = i + 1
            answer_dict = {"id": i + 1, "value": options[i], "is_key": False}
            if (options[i] == correct_answer):
                correct_option_number = on
                answer_dict["is_key"] = True

            # data["Answers"].append(answer_dict)

            print(i + 1, ')', options[i])

        # print("Correct Answer is:", correct_option_number, ')', correct_answer)
        data["Correct answer"] = str(correct_answer)

        print(json.dumps(data))
        data.clear()

    return None


no_of_questions = int(input("Enter the no of questions: "))
no_of_responses = int(input("Enter the no of options: "))
complexity = int(input("Enter the level of complexity: "))
sum(no_of_questions, complexity, no_of_responses)