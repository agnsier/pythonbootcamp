coins = 0
step_change = 0

while True:
    user_input = input("O hai! How much change is owed?")
    user_input = float(user_input)
    if user_input > 0:
        break
# 1 dollar is 100 cents
cents = user_input * 100
cents = int(cents)

if cents % 25 == 0 or cents//25 >= 1:
    step_change = (cents // 25)
    coins = coins + step_change
    cents = cents - step_change * 25
if cents % 10 == 0 or cents // 10 >= 1:
    step_change = (cents // 10)
    coins = coins + step_change
    cents = cents - step_change * 10
if cents % 5 == 0 or cents // 5 >= 1:
    step_change = (cents // 5)
    coins = coins + step_change
    cents = cents - step_change * 5
if cents % 1 == 0 or cents //1 >= 1:
    step_change = (cents // 1)
    coins = coins + step_change
    cents = cents - step_change * 1
print coins