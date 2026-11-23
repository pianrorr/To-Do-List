list = []

while True:
    print("TO - DO - LIST")
    print("By: Fian")
    print("1. View Task")
    print("2. Add Task")
    print("3. Delete Task")
    print("0. Exit")
    choose = input("Choose Menu: ")
    
    if choose == "2":
        create = input("\nToDo: ")
        list.append(create)
        print("Succes Add Task To List ✅\n")
    elif choose == "3":
        try:
            delete = input("\nDelete: ")
            list.remove(delete)
            print("Succes Deleted Task ✅\n")
        except ValueError:
            print("Task Not In List!\n")
            print(list)
            continue
    elif choose == "1":
        print("\n-- LIST TASK --")
        print(f"{list}\n")    
    elif choose == "0":
        print("Goodbye 👋")
        break
    else:
        print("\nYour Choose Not In Menu!\n")    