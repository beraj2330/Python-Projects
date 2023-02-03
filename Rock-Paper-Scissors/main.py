import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# rock beats scissors
# scissors beats paper
# paper beats rock

# denote following numbers to rock paper scissor
# generate random number between 0 to 2 for computer
# if else for rules
computer_choice = random.randint(0, 2)

if choice == 0:
  print(rock)
  print("Computer chose :")
  if computer_choice == 0:
    print(rock)
    print("Draw")
  elif computer_choice == 1:
    print(paper)
    print("You Lose")
  elif computer_choice == 2:
    print(scissors)
    print("You Win")

elif choice == 1:
  print(paper)
  print("Computer chose :")
  if computer_choice == 0:
    print(rock)
    print("You Win")
  elif computer_choice == 1:
    print(paper)
    print("Draw")
  elif computer_choice == 2:
    print(scissors)
    print("You Lose")

elif choice == 2:
  print(scissors)
  print("Computer chose :")
  if computer_choice == 0:
    print(rock)
    print("You Lose")
  elif computer_choice == 1:
    print(paper)
    print("You Win")
  elif computer_choice == 2:
    print(scissors)
    print("Draw")
