def q5():
    num = 0
    r = 0
    print("Let's find out how you sleep...")
    while r != 4:
        print("...Baby, how do you sleep when you lie to me?")
        ans = input()
        r = r + 1
        if ans == 'Very well':
            num = num - 10
            print("I'm hopin' that my love will keep you up tonight.")
        elif ans == 'Poorly':
            num = num + 20
            print("All that fear and all that pressure.")
        else:
            print("Love to you is just a game.")
    print("You achieved " + str(num) + " points.")

q5()