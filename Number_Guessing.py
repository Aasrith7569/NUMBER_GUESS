import random
name = input('ENTER YOUR NAME: ')
print("HI", name)
a = random.randint(100, 999)
chances = 10
while chances > 0:
    n = int(input('ENTER YOUR GUESS: '))
    chances = chances-1
    if a == n:
        print("HORRAY, YOU ARE RIGHT")
        break
    elif a < n:
        print("ANS IS LESSER\nYOU HAVE", chances, "CHANCES LEFT")
    elif a > n:
        print("ANS IS GREATER\nYOU HAVE", chances, "CHANCES LEFT")

print('NICE TRY BUT ANS IS', a)
