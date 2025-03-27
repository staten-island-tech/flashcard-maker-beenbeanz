import json

class Flashcard: 
    def __init__(self, question, answer, image):
        self.question = question
        self.answer = answer
        self.image = image
        
    def displayQuestion(self):
        return self.question

    def displayAnswerAndImage(self):
        return f"{self.answer} {self.image}"

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