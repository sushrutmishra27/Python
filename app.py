import database

MENU_PROMPT = """
CHoose one of the options:

1- Add a new bean
2- See all beans
3- Find a bean by name
4- See which preparation method is best
5- exit

Your selection:
"""

def menu():
    connection = database.connect()
    database.create_tables(connection)

    user_input = input(MENU_PROMPT)
    while (user_input != "5"):
        if user_input == '1':
            name = input('ENter bean name: ')
            method = input('Enter how you''ve prepared: ')
            rating = int(input('Enter rating score (0-100): '))

            databse.add_bean(connection, name, method, rating)

        elif user_input == '2':
            beans = database.get_all_beans(connection)
            for bean in beans:
                print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")

        elif user_input == '3':
            name = input('Enter bean name to find: ')
            beans = database.get_beans_by_name(connection, name)
            for bean in beans:
                print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")

        elif user_input == '4':
            name = input('Enter bean name to find: ')
            best_method = database.get_best_preparation(connection, name)
            print(f"the best preparation for {name} is: {best_methof[2]}")
            
        else:
            print('Invalid Input')

menu()
