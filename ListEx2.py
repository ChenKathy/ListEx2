s_list = []

def menu():
    menu = ["0 - exit", "1 - show current list", "2 - add item", "3 - remove item", "4 - complete shopping list"]
    i = 0
    
    while (i < len(menu)):
        print (menu[i])
        i += 1

    choice = raw_input ("Enter the number in correlation to your choice of action: ")

    if choice == "1":
        display()
    elif choice == "2":
        add()
    elif choice == "3":
        remove()
    elif choice =="4":
        print "Shopping List complete"
        display() 
    elif choice == "0":
        return 
    else: 
        print "Your choice is not an option."
        main()
 


def add():
    global item
    item = raw_input ("Enter item:").lower()
    if item not in s_list:
        s_list.append(item)
        display()   
    elif item in s_list:
        print "Item already in list."
        display()
    
    

# def add_new():
#     response = raw_input ("Enter Y to add again, Enter N to finish shopping list, or Enter R to remove an item.").upper()
#     if response == "Y":
#         print "Your response is yes."
#         add()
#         display()
#         menu() 

#     elif response == "N":
#         print "Your response is no."
#         print "Shopping List complete"
#         display() 
#     elif response == "R":
#         remove()
#     else:
#         print "Invalid response."
#         add_new()

def remove():
    r_item = raw_input("Enter item to be removed:").lower()
    if r_item in s_list:
        s_list.remove(r_item)
        display()
        print "Item:", r_item, "is removed."
        add_new()

    elif r_item not in s_list:
        print "Item not on the list."
        display()
        add_new() 
    

def display():
    s_list.sort() 
    print "Current Shopping List: ", s_list 
    menu()


def main():
    menu()


if __name__ == '__main__':
    main()
    
