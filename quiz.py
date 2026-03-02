from questions import questions

def login():
    print("===== Online Quiz Login =====")
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open("users.txt", "r") as file:
        users = file.readlines()
    for user in users:
        stored_user, stored_pass = user.strip().split(",")
        if username == stored_user and password == stored_pass:
            print("\nLogin Successful!\n")
            return username
    print("\nInvalid Credentials!")
    return None
  
def start_quiz(username):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ").upper()
        if answer == q["answer"]:
            score += 1
    percentage = (score / len(questions)) * 100
    print("\n===== Quiz Completed =====")
    print(f"Score: {score}/{len(questions)}")
    print(f"Percentage: {percentage:.2f}%")
    save_score(username, score, percentage)

def save_score(username, score, percentage):
    with open("scores.txt", "a") as file:
        file.write(f"{username},{score},{percentage:.2f}%\n")

if __name__ == "__main__":
    user = login()
    if user:
        start_quiz(user)
