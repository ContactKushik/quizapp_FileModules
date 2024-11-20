import sys
import os

# File paths for storing user data and scores
USER_FILE = "users.txt"
SCORE_FILE = "scores.txt"


#⚠️⚠️ RESPECTED SIR THESE QUESTIONS ARE GENERATED WITH THE HELP OF GPT SO NEVER MIND I NEEDED TO SPEED UP THE DEV
quizzes = {
    'python': [
        {'question': "What is the output of print(2 ** 3)?", 'options': ['6', '8', '9', '12'], 'answer': '8'},
        {'question': "Which keyword is used to create a function?", 'options': ['fun', 'def', 'func', 'define'], 'answer': 'def'},
        {'question': "What is the correct file extension for Python files?", 'options': ['.py', '.python', '.pyt', '.txt'], 'answer': '.py'},
        {'question': "What is the result of len('Hello')?", 'options': ['3', '4', '5', '6'], 'answer': '5'},
        {'question': "Which of these is not a Python data type?", 'options': ['List', 'Tuple', 'Dictionary', 'Queue'], 'answer': 'Queue'}
    ],
    'dsa': [
        {'question': "What is the time complexity of binary search?", 'options': ['O(n)', 'O(n^2)', 'O(log n)', 'O(1)'], 'answer': 'O(log n)'},
        {'question': "What data structure works on FIFO principle?", 'options': ['Stack', 'Array', 'Queue', 'Graph'], 'answer': 'Queue'},
        {'question': "What is the maximum number of nodes in a binary tree of height h?", 'options': ['2^h', '2^h - 1', '2^(h+1) - 1', 'h^2'], 'answer': '2^(h+1) - 1'},
        {'question': "Which sorting algorithm has the worst-case time complexity of O(n^2)?", 'options': ['Merge Sort', 'Quick Sort', 'Bubble Sort', 'Heap Sort'], 'answer': 'Bubble Sort'},
        {'question': "What does a stack use to function?", 'options': ['FIFO', 'LIFO', 'DFS', 'BFS'], 'answer': 'LIFO'}
    ],
    'cse': [
        {'question': "What does CPU stand for?", 'options': ['Central Process Unit', 'Central Processing Unit', 'Computer Personal Unit', 'Central Processor'], 'answer': 'Central Processing Unit'},
        {'question': "Which part of the computer is the brain?", 'options': ['RAM', 'CPU', 'Motherboard', 'Hard Drive'], 'answer': 'CPU'},
        {'question': "What does RAM stand for?", 'options': ['Random Access Memory', 'Read Access Memory', 'Ready And Memory', 'Run All Memory'], 'answer': 'Random Access Memory'},
        {'question': "What is the main function of an operating system?", 'options': ['Manage hardware resources', 'Compile code', 'Run applications', 'Store data'], 'answer': 'Manage hardware resources'},
        {'question': "Which of these is an example of system software?", 'options': ['MS Word', 'Linux', 'Photoshop', 'Chrome'], 'answer': 'Linux'}
    ]
}


# Helper function to read users from file
def load_users():
    users = {}
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            for line in file:
                username, password = line.strip().split(',')
                users[username] = password
    return users

# Helper function to save a new user to the file
def save_user(username, password):
    with open(USER_FILE, "a") as file:
        file.write(f"{username},{password}\n")

# Helper function to delete a user
def delete_user(username):
    users = load_users()
    if username in users:
        del users[username]
        with open(USER_FILE, "w") as file:
            for user, password in users.items():
                file.write(f"{user},{password}\n")
        print("User deleted successfully.")
    else:
        print("User not found.")

# Function to register a new user
def register():
    print("\nRegister")
    username = input("Enter username: ")
    users = load_users()
    if username in users:
        print("Username already exists. Please try again.")
    else:
        password = input("Enter password: ")
        save_user(username, password)
        print("Registration successful! Please login to continue.")

# Function to login
def login():
    print("\nLogin")
    username = input("Enter username: ")
    users = load_users()
    if username not in users:
        print("Username not found. Please register first.")
        return None
    password = input("Enter password: ")
    if users[username] == password:
        print("Login successful!")
        return username
    else:
        print("Incorrect password.")
        return None

# Function to get the highest score from the file
def get_high_score(username, quiz_type):
    scores = load_scores()
    return scores.get(username, {}).get(quiz_type, 0)

# Helper function to load scores
def load_scores():
    scores = {}
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as file:
            for line in file:
                username, quiz_type, score = line.strip().split(',')
                if username not in scores:
                    scores[username] = {}
                scores[username][quiz_type] = int(score)
    return scores

# Helper function to save or update the score in the file
def save_score(username, quiz_type, score):
    scores = load_scores()
    if username not in scores:
        scores[username] = {}
    if quiz_type not in scores[username] or score > scores[username][quiz_type]:
        scores[username][quiz_type] = score
        with open(SCORE_FILE, "w") as file:
            for user, quizzes in scores.items():
                for quiz, s in quizzes.items():
                    file.write(f"{user},{quiz},{s}\n")

# Function to display and handle quiz attempts
def attempt_quiz(username):
    print("\nSelect a quiz:")
    print("1. Python")
    print("2. DSA")
    print("3. CSE")
    
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        quiz_type = 'python'
    elif choice == '2':
        quiz_type = 'dsa'
    elif choice == '3':
        quiz_type = 'cse'
    else:
        print("Invalid choice. Returning to main menu.")
        return

    # Start the selected quiz
    score = 0
    for question in quizzes[quiz_type]:
        print("\n" + question['question'])
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")
        
        try:
            # Get user input and validate
            user_choice = int(input("Enter your choice (1-4): "))
            if 1 <= user_choice <= len(question['options']):
                selected_option = question['options'][user_choice - 1]
                if selected_option == question['answer']:
                    score += 1
            else:
                print("Invalid choice. Moving to next question.")
        except ValueError:
            print("Invalid input. Please enter a number. Moving to next question.")

    print(f"\nQuiz completed! Your score: {score}/{len(quizzes[quiz_type])}")
    save_score(username, quiz_type, score)
    high_score = get_high_score(username, quiz_type)
    print(f"Your highest score in {quiz_type} quiz: {high_score}")


# Main application loop
while True:
    print("\nMain Menu")
    print("1. Register")
    print("2. Login")
    print("3. Delete User")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        register()
    elif choice == '2':
        user = login()
        if user:
            while True:
                print("\nQuiz Menu")
                print("1. Attempt Quiz")
                print("2. View High Scores")
                print("3. Logout")
                
                sub_choice = input("Enter your choice (1-3): ")
                
                if sub_choice == '1':
                    attempt_quiz(user)
                elif sub_choice == '2':
                    print(f"High Scores for {user}:")
                    scores = load_scores().get(user, {})
                    for quiz, score in scores.items():
                        print(f"{quiz}: {score}")
                elif sub_choice == '3':
                    print("Logged out. Returning to main menu.")
                    break
                else:
                    print("Invalid choice.")
    elif choice == '3':
        username = input("Enter the username to delete: ")
        delete_user(username)
    elif choice == '4':
        print("Exiting the quiz app. Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
