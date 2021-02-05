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


q6()