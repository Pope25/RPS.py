import random

print('Rock or 0')
print('Paper or 1')
print('Scossors or 2')

Player = input ("Player 1, make your move: "). lower()
randnum = random.randint(0,2)
computer = randnum

while randnum <0 or randnum>2 :
    print('Invalid number please try again')
    Player = input ("Player 1, make your move: "). lower()
randnum = random.randint(0,2)

print('You have picked' ,Player)

if randnum == 0:
    computer= 'Rock'
elif randnum == 1:
    computer = 'Paper'
elif randnum == 2:
    computer = 'Scissors'

print(f"Computer plays {computer} ")
if Player == computer:
    	print("It's a tie!")

elif Player == 'Rock' or 0:
    if computer == 'scissors' or 2:
        print("player wins!")
    else:
        print("computer wins!")

elif Player == 'Paper' or 1:
    if computer == 'Rock' or 0:
        print("player wins!")
    else:
        print("computer wins!")

elif Player == 'scissors' or 2:
    if computer == 'Rock' or 1:
        print("computer wins!")
    else:
        print("player wins!")

elif Player == 'scissors' or 2:
    if computer == 'Paper' or 0:
        print("player wins!")
    else:
        print("computer wins!")

while randnum <0 or randnum>2 :
    print('Invalid number please try again')
