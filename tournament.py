def display_menu():
    
    f = open("menu.txt")
    print(f.read())
    f.close()

def add_participant():

    print("\n    Sign Up")
    name = input("    Participant name: ")
    slot = int(input("    Desired slot (1-%u): " % num_participants)) - 1
    if ( participants[slot] is None ):
        participants[slot] = name
        print("\n%s has been signed up for slot %u" % (name, slot+1))

def remove_participant():
    
    print("\n    Cancel Sign Up")
    name = input("    Participant name: ")
    slot = int(input("    Slot (1-%u): " % num_participants)) - 1
    if ( participants[slot] == name ):
        participants[slot] = None
        print("\n%s has been removed from slot %u" % (name, slot+1))

def view_participants():
    
    print("\n    View participants")
    slot = int(input("    Select slot (1-%u): " % num_participants)) - 1
    start = max(0,slot-5)
    end = min(len(participants),slot+6)
    for i in range(start,end):
        print("\n%u: %s" % (i+1, participants[i]))

def save_changes():

    print("\n    Save Changes")
    decision = input("    Save your changes to CSV? (y/n): ")
    if ( decision == "y" ):
        result = ""
        f = open("participants.csv", "w")
        for i in range(len(participants)):
            result += "%u,%s," % (i+1, participants[i])
        f.write(result[0:-1])
        f.close()
        print("\nChanges saved")

def exit():

    print("\n    Exit")
    decision = input("    Any unsaved changes will be lost.\n    Are you sure you want to exit? (y/n): ")
    if ( decision == "y" ):
        return True
    return False

num_participants = int(input("Enter the number of participants: "))
participants = [None for i in range(num_participants)]

while ( True ):
    display_menu()
    action = int(input("Choose an action (1-5): "))
    if ( action == 1 ):
        add_participant()
    elif ( action == 2 ):
        remove_participant()
    elif ( action == 3 ):
        view_participants()
    elif ( action == 4 ):
        save_changes()
    elif ( action == 5 ):
        if ( exit() ):
            break