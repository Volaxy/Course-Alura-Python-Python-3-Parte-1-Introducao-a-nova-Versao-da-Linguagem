import  hangmanGame
import  divination

print("*********************************")
print("*******Chose a game!*******")
print("*********************************")

print("(1) Hangman Game (2) Divination")

game = int(input("which game? "))

if game == 1:
    print("Playing Hangman")
elif game == 2:
    print("Playing Divination")