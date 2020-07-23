answer = input("welcome to the trivia game! I will ask you a question and you will answer. are you ready y or n")
if answer != "y":
  print("bye see you next time") 
if answer != "n":
  answer = input("ok here is you first question, In kerbal space program what is the real life equivilant of jupiters moon ganymade is it a) vall b) eeloo or c) tylo")
  if answer != "c":
   print("sorry thats wrong, the answer was c tylo ")
  if answer == "c":
    print("you got it right")
  answer = input("second question: What truly set in motion the events that started WW1 was it a) the austrian anexation of bosnia or b) the morroco crisis")
  if answer != "a":
    print ("sorry that is wrong")
  if answer == "a":
    print("Yay you got it right")
  answer = input("question 3: who was the designed by a) Nate Waters b) Mtchell Spore or c) Donold trump")
  if answer != "a":
    print ("that is wrong")
  if answer != "a":
    print ("that is right")