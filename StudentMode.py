import json

try:
    with open("Flashcards.json", "r") as file:
        cards_data = json.load(file)
except FileNotFoundError:
    cards_data = []

score = 0
for i in range(len(cards_data)):
    print(cards_data[i]["question"])
    ans = input('Your answer:')
    if(ans == cards_data[i]["answer"]):
        print("You're correct!")
        score += 1
    else:
        print("That is so wrong are you stupid.")
print(f"Your final score is {score}")