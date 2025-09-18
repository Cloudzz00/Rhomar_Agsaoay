mydict={}
size = int(input("Matrix size: "))

for x in range (size):
    val = str(input(f"Shopping Item {x+1}: "))
    mydict[x] = val

while(True):
    print("What would you like to do: [C]hange item [R]emove [D]isplay [S]earch")
    item = str(input())
    
    if item == '*':
        print("Bye")
        break

    if item.lower() == "d":
        print("Displaying Values")
        print("Key   Value")
        for i, j in mydict.items():
            print(f"{i}     {j}", end=" ")
            print()
    elif item.lower() == "s":
        search = int(input("Enter key to search: "))
        if search in mydict:
            print(f"Found {mydict[search]} item")
        else:
            print("I'm sorry, not in the cart")
    elif item.lower() == "r":
        search = int(input("Enter key to remove: "))
        if search in mydict:
            remove = mydict.pop(search)
            print(f"The key {search} with value {remove} has been deleted")
        else:
            print("Key not found")
    elif item.lower() == "c":
        search = int(input("Enter key to change: "))
        if search in mydict:
            print(f"Found {mydict[search]} item")
            change = str(input("Enter new value: "))
            mydict[search] = change 
        else:
            print("I'm sorry, not in the cart")