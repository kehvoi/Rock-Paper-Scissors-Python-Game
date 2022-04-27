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

print('WELCOME TO ROCK\n'
      'PAPER\n'
      'SCISSORS!')
print("Choose 0 for Rock, 1 for Paper and 2 for Scissors then hit enter")
Player = int(input())
AIpick = random.randint(0, 2)

if Player == 0 and AIpick == 0:
    print("it's a Draw\n"
          f"Player chose: {rock}\n"
          f"Computer chose: {rock}")
elif Player == 1 and AIpick == 1:
    print("it's a Draw\n"
          f"Player chose: {paper}\n"
          f"Computer chose: {paper}")
elif Player == 2 and AIpick == 2:
    print("it's a Draw\n"
          f"Player chose: {scissors}\n"
          f"Computer chose: {scissors}")
elif Player == 0 and AIpick == 1:
    print("Computer wins \n"
          f"Player chose: {rock}\n"
          f"Computer chose: {paper}")
elif Player == 1 and AIpick == 2:
    print("Computer wins \n"
          f"Player chose: {paper}\n"
          f"Computer chose: {scissors}")
elif Player == 2 and AIpick == 0:
    print("Computer wins \n"
          f"Player chose: {scissors}\n"
          f"Computer chose: {rock}")
elif Player == 0 and AIpick == 2:
    print("Player wins \n"
          f"Player chose: {rock}\n"
          f"Computer chose: {scissors}")
elif Player == 2 and AIpick == 1:
    print("Player wins \n"
          f"Player chose: {scissors}\n"
          f"Computer chose: {paper}")
elif Player == 1 and AIpick == 0:
    print("Player wins \n"
          f"Player chose: {paper}\n"
          f"Computer chose: {rock}")
if Player > 2:
      print("Invalid move\n try again")
