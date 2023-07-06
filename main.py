from screen import Screen

class Main:
    def __init__(self) :
        self.screen =Screen()

    def run_game(self):
        self.screen.run()
main = Main()
main.run_game()