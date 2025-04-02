import json
from PIL import Image

class Flashcard: 
    def __init__(self, question, answer, image):
        self.question = question
        self.answer = answer
        self.image = image
        
    def displayQuestion(self):
        return self.question

    def displayAnswerAndImage(self):
        return f"{self.answer} {self.image}"

    def displayImage(self):
        if self.image:
            try:
                img = Image.open(self.image)
                img.show()
            except FileNotFoundError:
                print("Error: Image file not found.")
        else:
            print("No image provided.")

teacherOrStudent = input("Teacher or Student mode? ")
if teacherOrStudent == "Teacher":
    newCardQuestion = input("Input the question: ")
    newCardAnswer = input("Input the answer: ")
    newCardImage = input("Input  file: ")
    newCard = Flashcard(newCardQuestion, newCardAnswer, newCardImage)

    try:
        with open("FlashCards.json", "r") as file:
            cardsData = json.load(file)
    except FileNotFoundError:
        cardsData = []

    cardsData.append(newCard.__dict__)

    with open('Flashcards.json', 'w') as file:
        json.dump(cardsData, file, indent=4)
elif teacherOrStudent == "Student":
    try:
        with open("Flashcards.json", "r") as file:
            cards_data = json.load(file)
    except FileNotFoundError:
        cards_data = []

    score = 0
    streak = 0
    for i in range(len(cards_data)):
        print(cards_data[i]["question"])
        ans = input('Your answer:')
        if(ans == cards_data[i]["answer"]):
            print("You're correct!")
            score += 1
            streak += 1
            if(streak % 3==0):
                print("Bonus activated. +3 points.")
                score+=3
        else:
            print("That is so wrong are you stupid.")
            streak = 0
    print(f"Your final score is {score}")
else: print("SELECT A VALID MODE YOU BOZO")