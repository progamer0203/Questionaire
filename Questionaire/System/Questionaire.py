import math

class Questionaire:
    def __init__(self, questions):
        self.questions = questions
        self.gayPoint = 0

    def Answer(self, answer, gayValue):
        convertedToBool = True

        if answer.lower() == "yes":
            convertedToBool = True
        elif answer.lower() == "no":
            convertedToBool = False
        else:
            self.gayPoint += 1
            
            return

        if convertedToBool == gayValue:
            self.gayPoint += 1

    def Result(self):
        print(f"Your gay point is {self.gayPoint} point.")
        
        if self.gayPoint > round(len(self.questions) / 4):
            print("You are gay.")
        else:
            print("You are not gay.")

        input("Enter to exit.")

    def Start(self):
        for title, value in self.questions.items():
            print(title)

            answer = input("Yes Or No: ")

            self.Answer(answer, value)

            print()

        self.Result()

questions = {
    "Do you think Dave is gay?": False,
    "Do you support LGBTQ?": True,
    "Are you pedophilia?": True,
    "Do you think Dave's lover is DJ?": False,
    "Are you racist?": False,
    "Do you think everyone deserves respect?": True,
    "Do you think one Gorilla is stronger than one hundred Dave?": False,
    "Do you love bromance?": False,
    "Are you vietnamese?": True,
    "Do you feel your heart pounding when your best friend is there?": False,
    "Do you think Dave touched grass on September 6th 2025?": True,
    "Do you think black lives matter?": True,
    "Do you think Dave is one of member in epstein island?": False,
    "Do you prefer taking shit in grass than toilet?": True,
    "Did you eat breakfast at 8 AM?": True,
    "Do you prefer Coca-Cola than Sprite?": True,
}

questionaire = Questionaire(questions)
questionaire.Start()