#!/usr/bin/env python3
"""A simple flash card quiz about Maryland."""

import json
from pathlib import Path


def load_questions():
    """Load quiz questions from questions.json in this folder."""
    script_folder = Path(__file__).resolve().parent
    questions_file = script_folder / "questions.json"

    with questions_file.open("r", encoding="utf-8") as file:
        return json.load(file)


def ask_question(question_data, question_number, total_questions):
    """Ask one question and return 1 for correct or 0 for incorrect."""
    print(f"\nQuestion {question_number} of {total_questions}")
    print(question_data["question"])

    user_answer = input("Your answer: ").strip().lower()
    correct_answers = [answer.strip().lower() for answer in question_data["answers"]]

    if user_answer in correct_answers:
        print("Correct! Nice job.")
        print(f"Fun fact: {question_data['fun_fact']}")
        return 1

    print(f"Not quite. One correct answer is: {question_data['answers'][0]}")
    print(f"Fun fact: {question_data['fun_fact']}")
    return 0


def main():
    """Run the flash card quiz in the terminal."""
    print("Welcome to the Maryland Flash Card Quiz!")
    print("Type your answers and press Enter.\n")

    try:
        questions = load_questions()
    except FileNotFoundError:
        print("Could not find questions.json. Make sure it is in the same folder as this script.")
        return
    except json.JSONDecodeError:
        print("questions.json is not valid JSON.")
        return

    score = 0
    total_questions = len(questions)

    for index, question_data in enumerate(questions, start=1):
        score += ask_question(question_data, index, total_questions)

    print("\nQuiz complete!")
    print(f"Your final score: {score}/{total_questions}")

    if score == total_questions:
        print("Perfect score! You really know Maryland.")
    elif score >= total_questions / 2:
        print("Great work! You know quite a bit about Maryland.")
    else:
        print("Good try! Play again and learn more Maryland facts.")


if __name__ == "__main__":
    main()
