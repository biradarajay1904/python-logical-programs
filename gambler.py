import random

stake = int(input("Enter the stake for playing gambling : "))
goals = int(input("Enter the goals you want to achieve : "))
trial = int(input("Enter number of times you bet : "))
wins = 0
loss = 0
bets = 0
percentageWins = 0.0
percentageLoss = 0.0

for i in range(0, trial):
    cash = stake
    while 0 <= cash < goals:
        bets += 1
        if random.randint(0, 1) < 0.5:
            cash += 1
        else:
            cash -= 1
    if cash == goals:
        wins += 1
    else:
        loss += 1

percentageWins = 100.0 * wins / trial
percentageLoss = 100.0 * loss / trial
percentageBets = wins + loss / trial
print("Number of times won : ", wins)
print("Number of times lost : ", loss)
print("Percentage of wining game : ", percentageWins)
print("Percentage of losing game : ", percentageLoss)
print("Percentages of bets you've make : ", percentageBets)



