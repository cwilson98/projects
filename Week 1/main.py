def q1():
    print("Who broke my heart?")
    name = input()
    print("My first love, " + name + ", broke my heart for the first time.")
    print("And I was like baby, baby, baby oh.")

def q2():
    print("Who sees me rolling (cops, wardens, other)?")
    ans = input()
    if ans == 'cops':
        print("They see me rolling. They hating. They hoping they gonna catch me riding dirty!.")
    elif ans == 'wardens':
        print("My music's so loud. I'm swanging. They hoping they gonna catch me riding dirty!")
    else:
        print("Trying to catch me riding dirty!")

def q3():
    print("How many times should I break free?")
    num = int(input())
    print("I'm stronger than I've been before...")
    while num != 0:
        num = num - 1
        print("..." + str(num) + ": this is the part when I break free.")
    else:
        print("Cause I can't resist it no more")

def q4(what, where):
    if what == "monster" and where == 'bed':
        print("I'm friends with a " + what + " that's under my " + where + ".")
    elif what == 'Doctor' and where == 'Hospital':
        print("You're trying to save me, stop holding your breath.")
    else:
        print("You think I'm crazy, yeah, you think I'm crazy")
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

def describe_friend(friend):
    if friend == '50 Cent':
        print("He be getting rich or die trying.")
    elif friend == 'Dr. Dre':
        print("He be needing California love.")
    elif friend == 'Rihanna':
        print("She be needing an umbrella.")
    else:
        print("They be cool.")

def display_friend(friend):
    print(friend + " can be described as follows: ")
    describe_friend(friend)

def q6():
    friend = input("Enter a friend: ")
    add = input("Describe or Display: ")
    if add == 'Describe':
        describe_friend(friend)
    elif add == 'Display':
        display_friend(friend)
    else:
        print("Invalid command.")



q1()
print("\n")
q2()
print("\n")
q3()
print("\n")
q4("monster", "bed")
q4("Doctor", "Hospital")
q4("Stranger", "Street")
q5()
q6()