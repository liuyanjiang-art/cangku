# Welcome the user to the quiz program
# Explain that they will answer multiple-choice questions

# Initialize a score counter to keep track of correct answers

# Present the first question
# Display the question text and the multiple-choice answers
# you can think of questions yourself, or find them online

# Get the user's input for their answer to the first question

# Check if the answer is correct
# If the answer is correct, print a success message and increase the score
# If the answer is incorrect, print the correct answer

# Repeat the above steps for additional questions (Question 2, Question 3, etc.)

# After all questions are answered, display the final score to the user
# Thank them for participating in the quiz

###### Extensions ######

# Use a loop to let people re-try the quiz
# create a leaderboard which stores users with the highest score
# Create a menu to let people access the leaderboard or the quiz
# Modularise the code to make it shorter and more maintainable
def welcome():
    print("Welcome to the Quiz Program!")
    print("You will answer multiple-choice questions. Let's begin!\n")

def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer == correct_answer:
        print("Correct! Great job.\n")
        return 1
    else:
        print(f"Wrong! The correct answer is {correct_answer}.\n")
        return 0

def quiz():
    score = 0
    # Question 1
    q1 = "What is the capital of France?"
    q1_options = ["London", "Paris", "Berlin", "Madrid"]
    score += ask_question(q1, q1_options, 2)
    # Question 2
    q2 = "Which planet is known as the Red Planet?"
    q2_options = ["Venus", "Mars", "Jupiter", "Saturn"]
    score += ask_question(q2, q2_options, 2)
    # Question 3
    q3 = "What is 2 + 2?"
    q3_options = ["3", "4", "5", "6"]
    score += ask_question(q3, q3_options, 2)
    print(f"Your final score is {score}/3. Thank you for participating!")
    return score

def leaderboard(score):
    import datetime
    name = input("Enter your name: ")
    entry = f"{name} - {score} - {datetime.datetime.now()}\n"
    with open("leaderboard.txt", "a") as f:
        f.write(entry)
    print("Leaderboard updated!\n")
    with open("leaderboard.txt", "r") as f:
        print("Current Leaderboard:")
        for line in f:
            print(line.strip())

def main():
    while True:
        print("\n--- Menu ---")
        print("1. Take Quiz")
        print("2. View Leaderboard")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            welcome()
            score = quiz()
            leaderboard(score)
        elif choice == 2:
            try:
                with open("leaderboard.txt", "r") as f:
                    print("Leaderboard:")
                    for line in f:
                        print(line.strip())
            except FileNotFoundError:
                print("Leaderboard is empty. Take the quiz first!")
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()