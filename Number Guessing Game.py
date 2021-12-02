import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess a number between 1 and 9 ")

while chances < 5 :
         guess = int(input("Enter Your Guess "))

         if guess == number :
                  print("Congraduations You Win !!!")
                  break
         elif guess < number :
                  print("Your Guess was to Low, Guess a number higher than ", guess)

         else:
                   print("Your Guess was to High, Guess a number lower than ", guess)

         chances = chances+1

if not chances < 5:
         print("Better Luck Next time")
         print("The Correct answer was",number)
