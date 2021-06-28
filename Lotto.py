first = input("Do you want to win the lottery?")
if first == "yes":
    print("Okay, I'll give you some hint")
    import random
    lotto = [0,0,0,0,0,0,0]
    for i in range(0,7): lotto[i] += random.randint(1,46)
    print(lotto)
else: print("Okay, Good luck")
