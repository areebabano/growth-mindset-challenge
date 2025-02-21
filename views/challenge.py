import streamlit as st
import random
import time
import re

# Title
st.title("🌱🚀 Growth 🎓 Mindset Coding Challenge! 💻🔥")

# Daily Coding Challenges
st.header("💡Daily Coding 💻  Challenge!")
challenges = [
    "Write a function to reverse a string without using built-in functions.",
    "Create a program that takes a number and prints whether it's prime or not.",
    "Write a function that finds the factorial of a number using recursion.",
    "Implement a Python program to check for balanced parentheses in an expression.",
    "Find the second largest number in an array without sorting it.",
    "Write a function to check if a number is a palindrome.",
    "Generate the Fibonacci sequence up to a given number.",
    "Implement a function to check if two strings are anagrams.",
    "Find the longest common prefix in a list of strings.",
    "Write a program to find duplicate elements in a list.",
    "Create a function that returns the first non-repeating character in a string.",
    "Implement a simple calculator that supports basic arithmetic operations.",
    "Write a function to check if a given Sudoku board is valid.",
]
if st.button("Get Today's Challenge 🎯"):
    st.write(f"🚀 **Your Challenge:** {random.choice(challenges)}")

# Debugging Challenge Title
st.header("🐞🔍 Debugging Challenge!")

# Dictionary of Buggy Code
buggy_code = {
    "Python_1": """
employees = {"pam" 30,
             "jim": 28}

for name, age in employees.items():
    print(f"{name.capitalize()} is {age} years old.")
""",
    "Python_2": """
def display_name():
    print(name)
    name = "John"

display_name()
""",
    "Python_3": """
# initialize the amount variable
amount = 10000

# check that You are eligible to
#  purchase Dsa Self Paced or not
if(amount>2999)
    print("You are eligible to purchase Dsa Self Paced")
""",
    "JavaScript": """
function multiply(a, b) {
return a * b  // Missing semicolon (Fix it!)
}
console.log(multiply(5, 3));
""",
    "TypeScript": """
let age: number = "twenty";  // Type Error (Fix it!)
console.log(age);
"""
}

# Corrected Code for Validation
correct_fixes = {
    "Python_1": """
employees = {"pam": 30,
             "jim": 28}

for name, age in employees.items():
    print(f"{name.capitalize()} is {age} years old.")
""",
    "Python_2": """
def display_name():
    name = "John"
    print(name)

display_name()
""",
    "Python_3": """
# initialize the amount variable
amount = 10000

# check that You are eligible to
#  purchase Dsa Self Paced or not
if amount > 2999:
    print("You are eligible to purchase Dsa Self Paced")
""",
    "JavaScript": """
function multiply(a, b) {
    return a * b; // Fixed: Added semicolon
}
console.log(multiply(5, 3));
""",
    "TypeScript": """
let age: number = 20;  // Fixed: Changed string to number
console.log(age);
"""
}

# Initialize session state for random selection
if "random_question" not in st.session_state:
    st.session_state.random_question = random.choice(list(buggy_code.keys()))

# Show Buggy Code
if st.button("Show Buggy Code 🐞"):
    # Select a new random question
    st.session_state.random_question = random.choice(list(buggy_code.keys()))
    st.code(buggy_code[st.session_state.random_question], st.session_state.random_question.split("_")[0])
    st.write("👀 🔥 **Challenge:** Find and fix the error in the above code! 🚀")

# Function to Normalize Code (Advanced Handling)
def normalize_code(code):
    """ Remove all whitespace, indentation, newlines, and hidden characters """
    return re.sub(r'\s+', '', code).strip().lower()

# User Input for Fixed Code
user_fix = st.text_area("Submit your fixed code below:")

# Submit Button
if st.button("Submit Fix ✍️"):
    if normalize_code(user_fix) == normalize_code(correct_fixes[st.session_state.random_question]):
        st.success("🎉✨ Great job! Keep debugging🐞 and improving your skills! 💪💡")
    else:
        st.error("❌ Oops! Your fix has some issues. Try again! 🔄")

# QUiz Challenge

st.header("📝 Quick Python🐍 Quiz")

# Define questions, options, and correct answers
questions = [
    ("What is the output of `print(type(10))`?", ["<class 'str'>", "<class 'int'>", "<class 'float'>", "<class 'bool'>"], "<class 'int'>"),
    ("What does the `len()` function do?", ["Returns the type", "Finds length of an object", "Converts to int", "Deletes a variable"], "Finds length of an object"),
    ("Which keyword is used to define a function in Python?", ["func", "def", "define", "function"], "def"),
    ("Which of the following is an immutable data type?", ["List", "Dictionary", "Tuple", "Set"], "Tuple"),
    ("What is the purpose of `if __name__ == '__main__':`?", ["Check variable type", "Run script when executed directly", "Print name", "Create class"], "Run script when executed directly"),
    ("Which operator is used for exponentiation in Python?", ["*", "**", "^", "//"], "**"),
    ("How do you open a file in write mode in Python?", ["open('file.txt', 'r')", "open('file.txt', 'w')", "open('file.txt', 'a')", "open('file.txt', 'x')"], "open('file.txt', 'w')"),
    ("What is the output of `2 ** 3` in Python?", ["6", "8", "9", "4"], "8"),
    ("What is the difference between `is` and `==` in Python?", ["No difference", "`is` checks identity, `==` checks value", "`is` compares values", "`==` checks memory location"], "`is` checks identity, `==` checks value"),
    ("Which method removes the last element of a list?", ["remove()", "pop()", "delete()", "discard()"], "pop()"),
]

# Initialize session state
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.correct_answers = 0
    st.session_state.wrong_answers = 0
    st.session_state.selected_answers = []  # Stores (question, user_answer, correct_answer)

# If quiz is not completed, show next question
if st.session_state.question_index < len(questions):
    question, options, correct_answer = questions[st.session_state.question_index]
    
    st.write(f"❓ {question}")
    answer = st.radio("Choose the correct answer:", options, key=st.session_state.question_index)

    if st.button("Submit Answer ✅"):
        # Save the user's response
        is_correct = answer == correct_answer
        st.session_state.selected_answers.append((question, answer, correct_answer))
        
        if is_correct:
            st.success("✅ Correct! Keep it up!")
            st.session_state.correct_answers += 1
        else:
            st.error(f"❌ Wrong! The correct answer is **{correct_answer}**")
            st.session_state.wrong_answers += 1
        
        st.session_state.question_index += 1  # Move to next question
        st.rerun()  # Refresh for next question

# Show final results when all questions are answered
else:
    st.subheader("📊 Quiz Results")
    
    st.write(f"✅ Correct Answers: {st.session_state.correct_answers}")
    st.write(f"❌ Incorrect Answers: {st.session_state.wrong_answers}")

    # Show correct & incorrect answers
    for q, user_ans, correct_ans in st.session_state.selected_answers:
        st.write(f"**Q:** {q}")
        st.write(f"**Your Answer:** {user_ans}")
        st.write(f"**Correct Answer:** {correct_ans}")
        st.write("---")

    # Show final message based on correct answers count
    if st.session_state.correct_answers >= 6:
        st.success("🎉 Congratulations! You did great! 🎯")
    else:
        st.warning("📚 Keep working on your skills and improve your knowledge! 🚀")

    # Restart button
    if st.button("Restart Quiz 🔄"):
        st.session_state.question_index = 0
        st.session_state.correct_answers = 0
        st.session_state.wrong_answers = 0
        st.session_state.selected_answers = []
        st.rerun()  # Restart the quiz

# List of words for the game
word_list = [
    "python", "typescript", "javascript", "streamlit", "react", "frontend", 
    "backend", "developer", "coding", "programming", "machine", "learning", "tailwind", "nextjs", "ethical"
]

# Function to scramble words
def scramble_word(word):
    return "".join(random.sample(word, len(word)))

# Initialize session state
if "word" not in st.session_state:
    st.session_state.word = None
    st.session_state.scrambled = None
    st.session_state.start_time = None
    st.session_state.end_time = None
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.game_over = False  # Track if game is completed

# Title
st.header("🔠 Word Scramble Challenge 🚀")

# Start New Game (Only if no active game)
if st.session_state.word is None and not st.session_state.game_over:
    if st.button("🎮 Start Game"):
        st.session_state.word = random.choice(word_list)
        st.session_state.scrambled = scramble_word(st.session_state.word)
        st.session_state.start_time = time.time()
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.rerun()

# Show scrambled word if game is active
if st.session_state.word:
    st.write(f"**Unscramble this word:** `{st.session_state.scrambled}`")

    # Attempts Counter
    st.write(f"🔄 Attempts: `{st.session_state.attempts}`")

    # Hint Feature
    if st.button("💡 Get a Hint (First Letter)"):
        st.info(f"Hint: The word starts with **`{st.session_state.word[0]}`**")

    # Input box for user guess
    user_guess = st.text_input("Your Guess:", key="user_guess")

    # Submit button
    if st.button("✅ Submit Answer"):
        st.session_state.attempts += 1
        st.session_state.end_time = time.time()
        elapsed_time = st.session_state.end_time - st.session_state.start_time

        if user_guess.lower() == st.session_state.word:
            st.session_state.score += 10  # Increase score on correct answer
            st.success(f"🎉 Correct! The word was `{st.session_state.word}`.")
            st.write(f"⏳ You solved it in `{elapsed_time:.2f} seconds`!")
            st.write(f"🏆 Your Score: `{st.session_state.score}`")
            st.session_state.game_over = True  # Mark game as completed
            st.session_state.word = None  # Reset current word

# Show Restart Button **only after game is completed**
if st.session_state.game_over:
    if st.button("🔄 Restart Game"):
        st.session_state.word = None
        st.session_state.scrambled = None
        st.session_state.start_time = None
        st.session_state.end_time = None
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.rerun()



# Leaderboard & Streak System
st.header("🏆💪 Your Challenge Streak")
streak = st.number_input("Enter your current streak (days):", min_value=0)
if st.button("Check Streak 🔥"):
    if streak > 10:
        st.success("🔥 Amazing! You're mastering coding challenges! 🚀")
    elif streak > 5:
        st.info("⭐ Great consistency! Keep pushing forward!")
    elif streak > 0:
        st.warning("💡 Keep going! Every step matters.")
    else:
        st.error("😢 Start today! Growth begins with the first challenge.")

# User Engagement Section
st.header("📣📊 Share Your Progress")
reflection = st.text_area("Reflect on today's challenge: What did you learn?")
if st.button("Share Insights ✨"):
    if reflection:
        st.success("Awesome! Reflection helps you grow! 🌱")
    else:
        st.error("Please write something before sharing!")


