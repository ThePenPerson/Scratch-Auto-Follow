import scratchconnect
import time
file = open("usernames.txt", "r+")
login = scratchconnect.ScratchConnect("ScratchConnectBot", "azTm3vKhwFRVPz4")
print("Site health: " + str(login.site_health()))
while True:
    print("1 in to see stats of a scratcher")
    print("2 is to follow or un-follow a user")
    print("3 is to follow 1 million people")
    message = int(input("Enter a number to choose a function: "))
    if message ==1:
        scratcher = input("Enter the scratcher you want the stats of: ")
        global user
        user = login.connect_user(username=str(scratcher))
        
        print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print("Id of user: " + str(user.id()))
        print("Message Count: " + str(user.messages_count()))
        print("Join Date: " + str(user.joined_date()))
        print("Total Users Followed: " + str(user.following_count()))
        print("Total Users Following: " + str(user.following_count()))
        print("Total Views: " + str(user.total_views_count()))
        print("Total Loves: " + str(user.total_loves_count()))
        print("Total Favourites: " + str(user.total_favourites_count()))
        print(": " + str())
        print(": " + str())
        
    elif message ==2:
        print()
    elif message == 3:
        print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        message = input("Are you sure you want to do this? (enter yes to continue)")
        if message =="yes":
            message = input("Enter passcode to continue: ")
            if message == "badapple":
                print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
                print("Welcome to 1 million scratcher programme...")
                print("Do you want there to be a pause between following people?")
                print("(for example a pause of 1 would take 1 million seconds to complete...")
                pause = float(input("Enter a pause value (0.1 or 0.01 is good. Make sure value is a number): "))
                length = int(input("Enter the amount of people you want to follow(Maximum is 1065092): "))
                message = input("Are you SURE you want to do this?(enter yes to continue...): ")
                if message == "yes":
                    print("Starting in 5 seconds...")
                    time.sleep(5)
                    for x in range(length):
                        name = file.readline().strip()
                        login.follow_user(username=name)
                        time.sleep(pause)
                        print(str(name)+ " followed. Total followed: " + str(x+1))
                        
                            
                                
                else:
                    break
                             
                
            else:
                print("incorrect")
                break
        else:
            print("Execution Cancelled...")
            break
        
    else:
        print("Input incorrect!")










        
        


