s_list = []
def add():
    global item
    item = raw_input ("Enter item:")
    if item not in s_list:
        s_list.append(item)      
    elif item in s_list:
        print "Item already in list."
    

def add_new():
    response = raw_input ("Enter Y to add again, Enter N to finish shopping list, or Enter R to remove an item.").upper()
    if response == "Y":
        print "Your response is yes."
        print main()

    elif response == "N":
        print "Your response is no."
        print "Shopping List complete"
        print display() 
    elif response == "R":
        print remove()
    else:
        print "Invalid response."
        print add_new()

def remove():
    r_item = raw_input("Enter item to be removed:").lower()
    if r_item in s_list:
        s_list.remove(r_item)
        print display()
        print "Item:", r_item, "is removed."
        print add_new()

    elif r_item not in s_list:
        print "Item not on the list."
        print display()
        print add_new() 
    

def display():
    s_list.sort() 
    print "Current Shopping List: ", s_list 


def main():
    print add()
    print display() 
    print add_new()










if __name__ == '__main__':
    main()
