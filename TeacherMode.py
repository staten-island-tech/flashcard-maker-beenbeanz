import json

flashcardsDict = {}

class Flashcard: 
    def __init__(self, question, answer, image):
        self.question = question
        self.answer = answer
        self.image = image
        
    def displayQuestion(self):
        return self.question

    def displayAnswerAndImage(self):
        return f"{self.answer} {self.image}"
    
inputQ = input("Input the question: ")
inputA = input("Input the answer: ")

card =  Flashcard(inputQ, inputA)
flashcardsDict[card.question] = card.answer

with open('Flashcards.json', 'w') as json_file:
    json.dump(flashcardsDict, json_file, indent=4)
print(flashcardsDict)