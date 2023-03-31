questions = [
    {
        "question": "Which Team won IPL 2018 Cup?",
        "options": ["CSK", "RCB", "MI", "DC"],
        "answer": "CSK"
    },
    {
        "question": " Who is the 1st Player to score 6000 IPL Runs?",
        "options": ["KL Rahul", "Virat Kohli", "MS Dhoni", "Smith"],
        "answer": "Virat Kohli"
    },
    {
        "question": "When was first IPL started",
        "options": ["2007", "2008", "2009", "2010"],
        "answer": "2007"
    }
]

def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    answer = input("Enter your answer (1-4): ")
    return question["options"][int(answer)-1] == question["answer"]

def play_quiz():
    score = 0
    for question in questions:
        if ask_question(question):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {question['answer']}")
    print(f"Your final score is {score}/{len(questions)}")

play_quiz()







