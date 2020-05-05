questions = [
    {
        "question": "What keyword Python uses to star defining a function?",
        "possible_answer": [
            '1. def\n'
            '2. fun\n'
            '3. dir\n'
            '4. function\n'
            ],
        "correct_answer": '1'
        },
    {
        "question": "Which line Represenet Boolen true in Python?",
        'possible_answer': [
            "1 - true\n"
            "2 - True\n"
            "3 - TRUE\n"
            "4 - trUE\n"
        ],
        "correct_answer": "2"
    },
]

result = 0

for question_definition in questions:
    print(question_definition["question"])
    for possible_answer in question_definition["possible_answer"]:
        print(possible_answer)

    answer = input(">>>")
    if answer.strip() == question_definition['correct_answer']:
        result = result + 1


print("Your score is: {} out of 2 questions".format(result))
