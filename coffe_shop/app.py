import database
import os

MENU="""-------COFFEE BEAN SHOP---------

Please Choose one of these options:

1)Add a New Bean

2)See All Bean

3)Find a Bean ny Name

4)Best Preparation Method For Bean

5)Delete Entry

6)Exit

Your Selection:  """



def menu():
    connection = database.connect()
    database.create_tables(connection)

    
    while(user_input :=input(MENU)) != "6":
        os.system('cls')
        if user_input =="1":
            name=input("Enter name of bean: ")
            method=input("Enter the method of preparation of bean: ")
            rating=int(input("Enter your rating score (0-100): "))

            database.add_beans(connection,name,method,rating)
        elif user_input=="2":
            beans= database.get_beans(connection)

            print("""------------------------COFFEE SHOP---------------------------
_____________________________________________________________""")
            print("NAME                      METHOD                 RATING")
            print("________________________________________________________")

            for i in beans:
                #using f string # 
               print(f"{i[1]}                  {i[2]}                {i[3]}/100\n")
        elif user_input=="3":
            name=input("Enter The Name of the Bean: ")
            bean=database.get_beans_by_name(connection,name)

            print("NAME                      METHOD                 RATING")
            print("________________________________________________________")

            for i in bean:
            #using f string # 
               print(f"{i[1]}                  {i[2]}                {i[3]}/100\n")
        elif user_input=="4":
            name=input("Enter the name: ")
            bean=database.get_best_preparation_for_bean(connection,name)

          

            print(f"the best method is {bean[2]}")
        elif user_input=="5":
            name=input("Enter the name: ")
            database.delete_entry(connection,name)

        else:print("Inavlid input ,Please enter again: ")
    
menu()