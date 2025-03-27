import json

try:
    with open("Flashcards.json", "r") as file:
        cards_data = json.load(file)
except FileNotFoundError:
    cards_data = []

for card in cards_data:
    print(cards_data[0]["question"])