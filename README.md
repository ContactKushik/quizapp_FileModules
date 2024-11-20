# Quiz App

A simple quiz application built in Python that allows users to register, login, attempt various quizzes, view high scores, and delete their accounts. The quizzes cover three categories: Python, DSA, and CSE, and track the scores of users across multiple attempts.

## Features

- **User Registration**: Users can create an account by providing a username and password.
- **Login**: Existing users can log in using their username and password.
- **Attempt Quizzes**: Users can choose from three categories of quizzes:
  - Python
  - DSA (Data Structures and Algorithms)
  - CSE (Computer Science Engineering)
- **Score Tracking**: The application tracks and stores the highest scores achieved by users for each quiz.
- **View High Scores**: Users can view their highest scores in each quiz category.
- **Delete User**: Users can delete their accounts from the system.

## File Structure

- `users.txt`: A file that stores the usernames and passwords of registered users.
- `scores.txt`: A file that stores the highest scores for each user and quiz category.

## Setup

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ContactKushik/quiz-app.git
    cd quiz-app
    ```

2. Run the application:

    ```bash
    python3 quiz_app.py
    ```

### Usage

1. **Register**: Choose the "Register" option to create a new user account.
2. **Login**: After registering, you can log in with your username and password.
3. **Attempt Quiz**: Once logged in, select a quiz category (Python, DSA, CSE) and answer the questions.
4. **View High Scores**: View the highest scores you’ve achieved in each quiz category.
5. **Delete User**: If you want to delete your account, select the "Delete User" option from the main menu.

## Code Explanation

- The program uses a simple text file system (`users.txt` and `scores.txt`) to store user credentials and quiz scores.
- It supports three types of quizzes (`python`, `dsa`, `cse`), each containing multiple-choice questions.
- The user can select answers for each question, and the score is calculated based on correct answers.
- After completing a quiz, the score is saved, and the highest score is displayed.
