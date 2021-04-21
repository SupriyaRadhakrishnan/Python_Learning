

from Question import  Question
questions_prompts = ["What Color are Apples?\n(a) Red/Green\n(b) Pruple\n(c) Orange\n\n",
                     "What Color are Bananas?\n(a) Teal\n(b) Yellow\n(c) Orange\n\n",
                     "What Color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
                     ]

questions = [Question(questions_prompts[0],"a"),
Question(questions_prompts[1],"b"),
Question(questions_prompts[2],"b")
             ]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("You got " + str(score) + "/" + str(len(questions)))

run_test(questions)