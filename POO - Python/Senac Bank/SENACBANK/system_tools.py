import os

class Tools:
    # Divider
    def divider():
        print('+'+'-'*50+'+')

    def showMessage (mensagem):
        os.system('cls')
        print('+'+'-'*50+'+')
        print(f"|{mensagem:^50}|")
        print('+'+'-'*50+'+')