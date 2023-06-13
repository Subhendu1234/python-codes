from Question import Question

question_prompts = ["what is the correct meaning of render?\n(a)deliver\n(b)please\n\n",
                    "what is the correct meaning of delimit?\n(a)punish\n(b)define\n\n",
                    "what is the correct meaning of resume?\n(a)pause\n(b)continue\n\n",
                    "what is the correct meaning of wary?\n(a)worried\n(b)careful\n\n",
                    "what is the correct meaning of voracious?\n(a)satiable\n(b)insatiable\n\n"]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "b"),
     Question(question_prompts[3], "b"),
     Question(question_prompts[4], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)