import json

try:
    with open("Flashcards.json", "r") as file:
        cards_data = json.load(file)
except FileNotFoundError:
    cards_data = []

for i in range(len(cards_data)):
    print(cards_data[i]["image"])