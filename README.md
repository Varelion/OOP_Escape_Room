# OOP_Escape_Room
A small little CLI game, written in Python. A quick little touch into OOP from the perspective of this language.

## Goals:
1. Learn Python classes & objects.
2. Utilize the above to create a short little game.

## Project Definition
Build an escape room in Python, utilizing classes, objects, and other OOP methodologies.

1. Room must contain several objects.
   1. Each Object can be observed, touched, or smelled to provide clues.
2. Player needs a code to escape.
3. Objects provide clues about the code.

Player will need to piece together all the clues. Each item will be able to be interacted with in
three ways, and each way will provide clues to players.

## Project Design
Entire game will be text-based.
 - Run in terminal.
 - Print prompts and capture user inputs.
 - Run until player either wins or loses.

## Game Components
1. Game Object Class
2. Room, list objects and requires code to escape
3. Game, instance of a game keeping tracks of attempts.
