import random
print("Rock, Paper, Scissors...")
a = list(('rock', 'paper', 'scissor'))
def game(d,b):
    if b=='rock':
        if d=='rock' or d=='ROCK' or d=='Rock':
            print("it is a tie")
        if d=='paper' or d=='PAPER' or d=='Paper':
            print("you win computer chose", b)
        if d=='scissor' or d=='SCISSOR' or d=='Scissor':
            print("you loose computer chose", b)
    if b=='paper':
        if d=='rock' or d=='ROCK' or d=='Rock':
            print("you loose computer chose", b)
        if d=='paper' or d=='PAPER' or d=='Paper':
            print("it is a tie")
        if d=='scissor' or d=='SCISSOR' or d=='Scissor':
            print("you win computer chose", b)
    if b=='scissor':
        if d=='rock' or d=='ROCK' or d=='Rock':
            print("you loose computer chose", b)
        if d=='paper' or d=='PAPER' or d=='Paper':
            print("you win computer chose", b)
        if d=='scissor' or d=='SCISSOR' or d=='Scissor':
            print("it is a tie")
while True:
    b = random.choice(a)
    d = input("your choice :- ")
    game(d,b)
    e=input("enter yes to continue and no to exit :- ")
    if e=='yes' or e=='y' or e=='Y' or e=='YES' or e=='Yes':
        continue
    else:
        print("goodbye...")
        break
