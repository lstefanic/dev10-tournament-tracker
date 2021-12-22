def display_menu():
    
    f = open("menu.txt")
    print(f.read())
    f.close()

def add_participant():
    
    name = input("Participant name: ")
    slot = int(input("Desired slot (1-%u): " % num_participants)) - 1
    if ( participants[slot] is None ):
        participants[slot] = name

def remove_participant():

    name = input("Participant name: ")
    slot = int(input("Slot (1-%u): " % num_participants)) - 1
    if ( participants[slot] == name ):
        participants[slot] = None

def view_participants(slot):

    start = max(0,slot-5)
    end = min(len(participants),slot+6)
    for i in range(start,end):
        print("%u: %s" % (i+1, participants[i]))

def write_to_file():

    result = ""
    f = open("participants.csv", "w")
    for i in range(len(participants)):
        result += "%u,%s," % (i+1, participants[i])
    f.write(result[0:-1])
    f.close()

num_participants = int(input("Enter the number of participants: "))
participants = [None for i in range(num_participants)]

while ( True ):
    display_menu()
    action = int(input("Choose an action (1-5): "))
    if ( action == 1 ):
        print("Sign Up")
        add_participant()
    elif ( action == 2 ):
        print("Cancel Sign Up")
        remove_participant()
    elif ( action == 3 ):
        print("View participants")
        slot = int(input("Select slot (1-%u): " % num_participants)) - 1
        view_participants(slot)
    elif ( action == 4 ):
        print("Save Changes")
        decision = input("Save your changes to CSV? (y/n): ")
        if ( decision == "y" ):
            write_to_file()
    elif ( action == 5 ):
        print("Exit")
        decision = input("Any unsaved changes will be lost.\nAre you sure you want to exit? (y/n): ")
        if ( decision == "y" ):
            break