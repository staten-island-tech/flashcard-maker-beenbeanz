import json

flashcardsDict = {}

inputQ = input("Input the question: ")
inputA = input("Input the answer: ")

class Flashcard: 
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        
card =  Flashcard(inputQ, inputA)
flashcardsDict[card.question] = card.answer


with open('Flashcards.json', 'w') as json_file:
    json.dump(flashcardsDict, json_file, indent=4)
print(flashcardsDict)