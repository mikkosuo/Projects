from game import Game


PlayVsComputer = True

if not PlayVsComputer:
    print("Started player vs player game!")
    game = Game()
    game.start()
    exit

print("Started player vs computer game!")
playerMark = input("Choose X/O:")
while (playerMark != "X") and (playerMark != "O"):
    playerMark = input("Choose X/O:")

computerMark = "O"
if playerMark == "O":
    computerMark = "X"
game = Game(True)
game.start()