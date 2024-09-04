# # Exercise 3: KOn banega karorpati:
# Create a program capable of displaying questions to the user like KBC.
#  Use List data type to store the questions and their correct answers.
#  Display the final amount the person is taking home after playing the game.

# ********************************************************************answer=========================================================================


# Exercise 3: Kaun Banega Crorepati
# Create a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.

# List of questions, options and answers
questions = [
    "1. Who is known as the father of the Indian Constitution?",
    "2. What is the capital of France?",
    "3. Who wrote the famous play 'Romeo and Juliet'?",
    "4. What is the smallest planet in our solar system?",
    "5. Who discovered gravity?"
]

options = [
    ["a) Jawaharlal Nehru", "b) Mahatma Gandhi", "c) B. R. Ambedkar", "d) Sardar Vallabhbhai Patel"],
    ["a) London", "b) Paris", "c) Rome", "d) Berlin"],
    ["a) Charles Dickens", "b) William Shakespeare", "c) Mark Twain", "d) Jane Austen"],
    ["a) Mercury", "b) Venus", "c) Earth", "d) Mars"],
    ["a) Isaac Newton", "b) Albert Einstein", "c) Galileo Galilei", "d) Nicolaus Copernicus"]
]

answers = ['c', 'b', 'b', 'a', 'a']

# Prize money list
prize_money = [1000, 5000, 10000, 20000, 50000]

# Variable to keep track of winnings
total_prize = 0

# Welcome message
print("Welcome to Kaun Banega Crorepati!\n")

# Asking each question
for i in range(len(questions)):
    print(questions[i])
    for option in options[i]:
        print(option)
    
    # Taking input from the user
    user_answer = input("\nYour answer (a/b/c/d): ").lower()
    
    # Checking if the answer is correct
    if user_answer == answers[i]:
        print("Correct Answer! You won ₹", prize_money[i])
        total_prize = prize_money[i]
    else:
        print("Wrong Answer! You are taking home ₹", total_prize)
        break
    
    print()

# Final amount won by the user
print("Congratulations! You are taking home ₹", total_prize)
