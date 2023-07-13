# Guess the number
# A game where the algorithm set a random number up to 100 and you try to guess it.
import random
import PySimpleGUI as sg

class GuessTheNumber:
    def __init__(self):
        self.random_value = 0
        self.min_value = 1
        self.max_value = 100
        self.try_again = True

    def Start(self):
        # Layout
        layout = [
            [sg.Text('Your Guess',size=(39,0))],
            [sg.Input(size=(18,0),key='GuessValue')],
            [sg.Button('Guess it!')],
            [sg.Output(size=(39,10))]
        ]
        # Window
        self.window = sg.Window('Guess the number!', layout=layout)
        self.SetRandomNumber()
        try:
            while True:
                # Get the values
                self.event, self.values = self.window.Read()
                # Use the values
                if self.event == 'Guess it!':
                    self.guess_value = self.values['GuessValue']
                    while self.try_again == True:
                        if int(self.guess_value) > self.random_value:
                            print('Guess lower!')
                            break
                        elif int(self.guess_value) < self.random_value:
                            print('Guess higher!')
                            break
                        if int(self.guess_value) == self.random_value:
                            self.try_again = False
                            print("Congratulations you are correct!!")
                            break
        except:
            print('Please, do type only numbers!')
            self.Start()

    def SetRandomNumber(self):
        self.random_value = random.randint(self.min_value,self.max_value)

guess = GuessTheNumber()
guess.Start()