#program to car simulation

cmd = ""
started = False

while cmd!= "quit":
    com = input(">").lower()
    if com == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit""")
    elif com == "start":
        if started:
            print("Already Car Started")
        else:
            started = True
            print("Car started......ready to go")
    elif com == "stop":
        if not started:
            print("car already stopped")
        else:
            started = False
            print("car stopped")
    elif com == "quit":
        print("exitted")
        break
    else:
        print("don't understand")
