import scratchconnect
import time
file = open("usernames.txt", "r+")
login = scratchconnect.ScratchConnect("ENTER YOUR USERNAME", "ENTER PASSCODE")
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
message = input("Are you sure you want to do this? (enter yes to continue)")
if message == "yes":
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    print("Welcome to 1 million scratcher programme...")
    print("Do you want there to be a pause between following people?")
    print("(for example a pause of 1 would take 1 million seconds to complete...")
    pause = float(input("Enter a pause value (10 or 15 is good. Make sure value is a number): "))
    length = int(input("Enter the amount of people you want to follow(Maximum is 1065092): "))
    message = input("Are you SURE you want to do this?(enter yes to continue...): ")
    if message == "yes":
        print("Starting in 5 seconds...")
        time.sleep(5)
        for x in range(length):
            name = file.readline().strip()
            login.follow_user(username=name)
            print(str(name)+ " followed. Total followed: " + str(x+1))
            time.sleep(pause)      
                            
              







        
        


