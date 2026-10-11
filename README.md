A simple, interactive Python script that helps you solve the popular daily word game, Wordle. By applying the principles of elimination, this script filters through the official Wordle dictionary to provide you with a list of all possible remaining words based on your current hints.

Features

Live Dictionary Fetching: Dynamically downloads both the official Wordle answers list (~2,300 words) 
and the allowed guesses list (~10,000 words) directly from the web, ensuring the dictionary is always complete and up to date.

Interactive Loop: The script runs continuously alongside your game. 
You only need to input the new hints you discover after each guess, and it remembers your previous constraints.

Easy Input Format: Simple and intuitive syntax for entering your green, yellow, and gray letters.
How to Run

Make sure you have Python installed on your system.

Clone this repository or download the wordle_solver.py file.

Open your terminal or command prompt and run the script:

python wordle_posseible_words_finder.py

Follow the on-screen prompts to input your hints after your first guess in the game.

Input Guide

GREEN (Correct letter, correct spot): Enter the position (1-5) and the letter. Example: 2o 4e 5l (if 'O' is 2nd, 'E' is 4th, 'L' is 5th).
YELLOW (Correct letter, wrong spot): Enter the position you tried and the letter. Example: 1a 3m.
GRAY (Letter not in word): Enter all the gray letters together without spaces. Example: rtuias.
YELLOW (Correct letter, wrong spot): Enter the position you tried and the letter. Example: 1a 3m.

GRAY (Letter not in word): Enter all the gray letters together without spaces. Example: rtuias.
