answer = input("welcome to the trivia game! I will ask you a question and you will answer. are you ready y or n")
if answer != "y":
  print("bye see you next time") 
if answer != "n":
  answer = input("ok here is you first question, In kerbal space program what is the real life equivilant of jupiters moon ganymade is it a) vall b) eeloo or c) tylo:")
  if answer != "c":
   print("sorry thats wrong, the answer was c tylo ")
  if answer == "c":
    print("you got it right")
  answer = input("second question: What truly set in motion the events that started WW1 was it a) the austrian anexation of bosnia or b) the morroco crisis:")
  if answer != "a":
    print ("sorry that is wrong")
  if answer == "a":
    print("Yay you got it right")
  answer = input("question 3: who was the designed by a) Nate Waters b) Mtchell Spore or c) Donold trump:")
  if answer != "a":
    print ("that is wrong")
  if answer != "a":
    print ("that is right")
  answer = input("question 4: what is the largest desert:")
  if answer != "venus":
    print ("that is wrong")
  if answer == "venus":
    print ("hooray you got it right")
  answer = input(" question 5 what could be the most insane idea ever a) the orion drive b) project A119 c) the salyut 3 gun or d) all of the above:")
  if answer == "d":
    print("you got it right yay")
  if answer != "d":
    print ("booooooooooooo you got it wrong")
  answer = input(" question 6: what was the first battle of ww1 a) the fist battle of the marne b) the battle of verdun or c) the battle of passendale:")
  if answer != "a":
    print ("sorry that is wrong the correct answer was a")
  if answer == "a":
    print("yay you got it right")
  answer = input("question 7: what is the diffrence between a nutron star and a pulsar a) nutron stars spinn faster than pulsars or b) pusars shoot out jets of gamma rays from thier poles while nutron stars dont:")
  if answer != "b":
    print("that is wrong")
  if answer == "b":
    print ("that is right")
  answer = input("question 8: this president is in the wrestling hall of fame:")
  if answer == "Abraham Lincon":
    print("yay you get it right")
  if answer !=  "Abraham Lincon":
    print("sorry that is wrong")
  answer = input("question 9 in which state is this a law, bear wrestling matches are forbidden. a) virginia b) alabama or c) wyoming:")
  if answer != "b":
    print("sorry the answer was b")
  if answer == "b":
    print("you got it right")
  answer = input("question 10 what is older a) html or b) python")
  if answer == "a":
    print("you got it right")
  if answer != "a":
    print ("you get it right")
  input("well that's it, come play again later")