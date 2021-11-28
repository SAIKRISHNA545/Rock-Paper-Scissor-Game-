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

uchoice=int(input("enter choice? o for rock, 1 for paper, 2 for scissor\n"))
if uchoice>2 or uchoice<0:
    print("invalid choice")
else:
    moves=[rock,paper,scissors]
    z=moves[uchoice]
    print(z)
    x=random.randint(0,2)
    y=moves[x]
    print("computers choicei is :",x)
    print(y)
    if (uchoice==0 and x==2) or  (uchoice==2 and x==0) or (uchoice==1 and x==0) or (uchoice==2 and x==1):
        print("you win")
    elif (uchoice==1 and x==2) or (uchoice==0 and x==1) or  (uchoice==2 and x==0) or (uchoice==0 and x==1):
        print("you lose and computer will win")
    else:
        print("draw")

