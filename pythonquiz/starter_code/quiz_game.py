# quiz_game.py - Python Quiz Game
# Starter code for e004-exercise-control-flow (Collaborative Project)

"""
Python Quiz Game
----------------
A multiple-choice quiz game that tests Python knowledge.

This is a collaborative project - use pair programming!
- Driver: Types the code
- Navigator: Reviews and guides

Switch roles every 20-30 minutes!
"""

# =============================================================================
# TODO: Task 1 - Question Bank (Driver 1)
# =============================================================================

def create_question_bank():
    """
    Return a list of quiz questions.
    
    Each question is a dictionary with:
    - question: The question text
    - options: List of 4 options (A, B, C, D)
    - answer: Correct answer letter
    - explanation: Why this answer is correct
    
    Add at least 10 questions covering Week 1 topics.
    """
    questions = [
        {
            "question": "What keyword is used to define a function in Python?",
            "options": ["A) func", "B) def", "C) function", "D) define"],
            "answer": "B",
            "explanation": "The 'def' keyword is used to define functions in Python."
        },
        {
            "question": "Which of the following will return the number of items in a list?",
            "options" : ["A) list.length", "B) list.length()", "C) length(list)", "D) len(list)"],
            "answer" : "D",
            "explanation" : "len(list) is the only valid function of these."
        },
        {
            "question" : "Which of the following datatypes are immutable?",
            "options" : ["A) list", "B) string", "C) set", "D) dictionary"],
            "answer" : "B",
            "explanation": "The correct answer is B, string. lists are mutable. while the items in sets are immutable, sets themselves are mutable. dictionaries are mutable."
        },
        {
            "question" : "Which of the following bash commands will create a directory?",
            "options" : ["A) cat", "B) touch", "C) mkdir", "D) cd"],
            "answer" : "C",
            "explanation": "The correct answer is C, mkdir. cat prints the contents of a file to the terminal. touch can be used to create a file or update its timestamp of last edit. cd is used for changing current directory."
        },
        {
            "question" : "What data type in Python deals with whole numbers?",
            "options" : ["A) integer", "B) float", "C) string", "D) double"],
            "answer" : "A",
            "explanation": "The answer is A, integer. floats are not whole numbers. strings are sequences of characters, doubles are not in Python."
        },
        {
            "question": "What is the purpose of the str.count() function?",
            "options" : ["A) Count the total number of character in the string", "B) Count the number of times a given substring occurs in str", "C) Converts the given string to an integer", "D) This function does not exist"],
            "answer" : "B",
            "explanation" : "The answer is B. str.count(substring) returns the number of times substring occurs in str."
        },
        {
            "question": "Why is indentation important in Python?",
            "options": ["A) Python doesn't have end of statement special characters (like ';')", "B) Python doesn't use ( ) or { } to enclose large blocks of code", "C) Python is white space dependent", "D) All of the above"],
            "answer" : "D",
            "explanation": "All are true of Python."
        },
        {
            "question": "What is printed with the following statement? print(12 / 3 + 6 * 4)",
            "options" : ["A) 40.0", "B) 28", "C) 6", "D) 28.0"],
            "answer" : "D",
            "explanation" : "The answer is D, 28.0, following PEMDAS. 40.0 and 6 don't follow the order of operations. The inclusion of a / operator means the answer will print as a float with a decimal."
        },
        {
            "question": "What enclosing characters do dictionaries use in Python?",
            "options": ["A) Parenthesis ()", "B) square brackets []", "C) curly braces {}", "D) vertical bar |"],
            "answer": "C",
            "explanation": "Dictionaries use {curly braces}"
        },
        {
            "question": "What is the difference between else and elif?",
            "options" : ["A) elif must come after an if while an else does not", "B) elif evaluates a condition while else does not", "C) else evaluates a condition while elif does not", "D) elif doesn't exist in Python; else if must be used"],
            "answer": "B",
            "explanation" : "The correct answer is B. else and elif must both follow if. C is the reverse of the correct answer. D is incorrect since elif valid."
        }
        # TODO: Add 9 more questions covering:
        # - Python syntax and indentation
        # - Data types (strings, lists, dictionaries)
        # - Control flow (if/else, loops)
        # - Functions and parameters
        # - Variables and operators
    ]
    return questions


# =============================================================================
# TODO: Task 2 - Core Game Functions (Driver 2)
# =============================================================================

def display_question(question, number, total):
    """
    Display a question and its options.
    
    Args:
        question: A question dictionary
        number: The current question number (1-based)
        total: Total number of questions
    
    Output format:
    --------------------------------------------------
    Question 1 of 10
    --------------------------------------------------
    [question text]
    
    A) option A
    B) option B
    C) option C
    D) option D
    """
    # TODO: Implement this function
    print("--------------------------------------------------")
    print(f"Question {number} of {total}")
    print("--------------------------------------------------")
    print(f"{question["question"]}")
    print()
    for option in question["options"]:
        print(option)
    pass


def get_user_answer():
    """
    Get and validate user input.
    
    Keep prompting until the user enters a valid answer (A, B, C, or D).
    Accept both uppercase and lowercase input.
    
    Returns:
        A valid answer in uppercase (A, B, C, or D)
    """
    # TODO: Implement input validation loop
    while True:
        choice = input("Answer: ")
        choice = choice.upper()
        if choice == "A" or choice == "B" or choice == "C" or choice == "D":
            return choice
        else:
            print("Please enter A, B, C, or D")
    pass


def check_answer(question, user_answer):
    """
    Check if the user's answer is correct.
    
    Args:
        question: The question dictionary
        user_answer: The user's answer (uppercase letter)
    
    Returns:
        True if correct, False otherwise
    """
    if user_answer == question["answer"]:
        return True
    else:
        return False
    # TODO: Compare user_answer with question["answer"]


def display_feedback(question, user_answer, is_correct):
    """
    Display feedback after answering a question.
    
    If correct: Print "Correct!" with green styling (or just text)
    If incorrect: Print "Incorrect. The answer was X."
    Always show the explanation.
    """
    # TODO: Display appropriate feedback based on is_correct
    if is_correct:
        print("Correct")
    else:
        print(f"Incorrect. The answer was {question["answer"]}")
    print(f"{question["explanation"]}")


# =============================================================================
# TODO: Task 3 - Game Loop (Driver 1)
# =============================================================================

def run_quiz(questions):
    """
    Run the complete quiz game.
    
    1. Display welcome message
    2. Loop through all questions
    3. For each question:
       - Display the question
       - Get user answer
       - Check if correct
       - Display feedback
       - Update score
    4. Return final score
    
    Args:
        questions: List of question dictionaries
    
    Returns:
        Tuple of (score, total_questions)
    """
    score = 0
    total = len(questions)
    
    # Welcome message
    print("=" * 50)
    print("     WELCOME TO THE PYTHON QUIZ GAME!")
    print("=" * 50)
    print(f"\nYou will answer {total} questions.")
    print("Enter A, B, C, or D for each question.\n")
    input("Press Enter to start...")
    
    # TODO: Implement the game loop
    # Hint: Use a for loop with enumerate
    for i, q in enumerate(questions, start=1):
        display_question(q,i,total)
        user_answer = get_user_answer()
        is_correct = check_answer(q, user_answer)
        if is_correct:
            score += 1
        display_feedback(q, user_answer, is_correct)
    
    return score, total


# =============================================================================
# TODO: Task 4 - Results and Grading (Driver 2)
# =============================================================================

def calculate_grade(score, total):
    """
    Calculate letter grade based on percentage.
    
    Grading scale:
    - 90-100%: A
    - 80-89%:  B
    - 70-79%:  C
    - 60-69%:  D
    - Below 60%: F
    
    Args:
        score: Number of correct answers
        total: Total number of questions
    
    Returns:
        Letter grade as string
    """
    # TODO: Calculate percentage and return grade
    score_percent = score/total * 100
    if score_percent >= 90:
        return "A"
    elif score_percent >= 80:
        return "B"
    elif score_percent >= 70:
        return "C"
    elif score_percent >= 60:
        return "D"
    return "F"



def display_results(score, total):
    """
    Display final results with grade and encouragement.
    
    Include:
    - Score (e.g., 8/10)
    - Percentage
    - Letter grade
    - Encouraging message based on performance
    """
    # TODO: Calculate percentage and grade
    score_percent = score / total * 100
    letter_grade = calculate_grade(score, total)
    # TODO: Display formatted results
    print("=" * 50)
    print("Your Results")

    print("=" * 50)
    print(f"Score:        {score}")
    print(f"Percentage:   {score_percent}")
    print(f"Letter grade: {letter_grade}")
    print()
    # TODO: Add encouragement message
    match(letter_grade):
        case "A":
            print("Wow! You must be a Python extrordinaire! I'm so impressed. - Abraham Lincoln")
        case "B":
            print("It's not perfection but look at how much you already know. This is pretty good but you can still do better. - Thomas Edison")
        case "C":
            print("This is a passing grade. Cs get degrees, but maybe not the big internship. - Teddy Roosevelt")
        case "D":
            print("This is passing in some jurisdictions. Ds may also get degrees depending on your school and where you live. C'mon though, you have more in you than that. - Bill Gates, creator of Python")
        case "F":
            print("You only learn by failing. Python is really hard but it gets easier - Mahatma Ghandi")


# =============================================================================
# Main Program
# =============================================================================

def main():
    """Main entry point for the quiz game."""
    # Create question bank
    questions = create_question_bank()
    
    # Run the quiz
    score, total = run_quiz(questions)
    
    # Display results
    display_results(score, total)
    
    # Ask to play again
    play_again = input("\nWould you like to play again? (yes/no): ")
    if play_again.lower() in ["yes", "y"]:
        main()
    else:
        print("\nThanks for playing! Goodbye!")


if __name__ == "__main__":
    main()
