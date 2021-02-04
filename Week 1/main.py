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

q1()
q2()