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

q1()
print("\n")
q2()
print("\n")
q3()
print("\n")
q4("monster", "bed")
q4("Doctor", "Hospital")
q4("Stranger", "Street")