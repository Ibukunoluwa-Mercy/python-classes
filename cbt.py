
# Simple CBT Application

questions = [
    {
        "question": "1. What is the capital of Nigeria?",
        "options": ["A. Lagos", "B. Abuja", "C. Kano", "D. Ibadan"],
        "answer": "B"
    },
    {
        "question": "2. Which language is used for this program?",
        "options": ["A. Java", "B. C++", "C. Python", "D. PHP"],
        "answer": "C"
    },
    {
        "question": "3. What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Utility",
            "D. Control Processing User"
        ],
        "answer": "A"
    },
    {
        "question": "4. Which one is an input device?",
        "options": ["A. Monitor", "B. Printer", "C. Speaker", "D. Keyboard"],
        "answer": "D"
    },
    {
        "question": "5. What is 5 + 5?",
        "options": ["A. 8", "B. 10", "C. 15", "D. 20"],
        "answer": "B"
    }
]

print("================================")
print("     WELCOME TO SIMPLE CBT")
print("================================")

name = input("Enter your name: ")
score = 0

for question in questions:
    print("\n" + question["question"])
    for option in question["options"]:
        print(option)

    answer = input("Choose your answer (A/B/C/D): ").upper()

    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\n================================")
print("          EXAM RESULT")
print("================================")
print("Student Name:", name)
print("Total Questions:", len(questions))
print("Correct Answers:", score)
print("Final Score:", str(score / len(questions) * 100) + "%")

if score >= 3:
    print("Status: PASS")
else:
    print("Status: FAIL")

print("Thank you for taking the test!")
