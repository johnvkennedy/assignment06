# ------------------------------------------------------------------------ #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoFile.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Jack Kennedy,11/23/2020,Combining Scripts for Assignment):
# RRoot,1.1.2030,Created started script
# Jack Kennedy, 11/17/2020, Finished Original Script
# Jack Kennedy, 11/23/2020, Added Class and Functions
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection
txtdata = []  # ADDED = Data for the text document


# -- Processing -- #
class Processor:
    @staticmethod
    def read_data_from_file(file_name, lstTable):
        objFile = open(file_name)
        for row in objFile:
            txtdata = row.split(",")
            dicRow = {"Task": txtdata[0], "Priority": txtdata[1].strip()}
            lstTable.append(dicRow)
        objFile.close()
        return lstTable

    @staticmethod
    def reload_file(file_name, lstTable):
        objFile = open(file_name)
        for row in objFile:
            txtdata = row.split(",")
            dicRow = {"Task": txtdata[0], "Priority": txtdata[1].strip()}
            lstTable.append(dicRow)
        objFile.close()
        return lstTable

    @staticmethod
    def print_current_tasks_in_list(lstTable):
        print("--------------------------------------------\n"
              "\tThis is the current data in the table.\n"
              "--------------------------------------------\n"
              "==============")
        print("Row - Task - Priority")
        counter = 0
        for row in lstTable:
            print(f'{counter} | {row["Task"]} | {row["Priority"]} |')
            counter += 1
        print("==============")
        return lstTable

    @staticmethod
    def add_data_to_list(task, priority, lstTable):
        dicRow = {"Task": task, "Priority": priority}
        lstTable.append(dicRow)
        print("\n=====", task, "has been added with priority", priority, "=====")

    @staticmethod
    def remove_data_from_list(removal):
        lstTable.pop(removal)
        print("\n===== Row", removal, "has been taken out of the table =====")

    @staticmethod
    def save_data_to_file():
        objFile = open("C:\_PythonClass\mytodolist.txt", "w")
        for row in lstTable:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()
        print("===== The current table has been saved =====\n")


# Presentation (Input/Output)
class IO:
    @staticmethod
    def greetings():
        print("==============================================\n"
              "\t Hello amazing user!\n"
              "\t This script is made to allow you to\n"
              "\t view, add, and remove items of a\n"
              "\t list made in -mytodolist.txt-. There is\n"
              "\t also an option to save that data.\n\n"
              "\t First it will open the file to keep\n"
              "\t previously existing data then you the\n"
              "\t user may interact with that data.\n\n"
              "\t            !IMPORTANT!\n"
              "\t DATA IS ONLY SAVED WHEN THE OPTION\n"
              "\t       IS CHOSEN IN THE MENU!\n"
              "==============================================")

    #Menu
    @staticmethod
    def print_menu_tasks():
        print("""
            *** Menu of Options ***
            1) Add a new Task
            2) Remove an existing Task
            3) Save Data to File        
            4) Reload Data from File
            5) Exit Program
            """)

    # Choosing Menu Option
    def input_menu_choice(self):
        choice = str(input("Which option would you like to perform? [1 to 5] - "))
        print()
        return choice

    # Yes or No Input
    @staticmethod
    def input_yes_no_choice(message):
        return str(input(message)).strip().lower()

    # Continue Option
    @staticmethod
    def input_press_to_continue(optional_message=''):
        print(optional_message)
        input('Press the [Enter] key to continue.')


# -- Main Script -- #
Processor.read_data_from_file("C:\_PythonClass\ToDoFile.txt", lstTable)
IO.greetings()
while True:
    # Selection Menu
    Processor.print_current_tasks_in_list(lstTable)
    IO.print_menu_tasks()
    strChoice = IO.input_menu_choice("self")
    # Add Data
    if strChoice.strip() == '1':
        Processor.add_data_to_list(input("-------------------------------------------------\n"
                                         "\tYou've chosen to add to the current table.\n"
                                         "\tWhat task do you wish to add?\n"
                                         "-------------------------------------------------\n"
                                         "\tEnter New Task: "),
                                   input("\n---------------------------------------------------------------\n"
                                         "\tWhat priority do you wish to designate to this task?\n"
                                         "\tExamples: 1-10, Not Important to Important, Low to High.\n"
                                         "---------------------------------------------------------------\n"
                                         "\tEnter Priority for New Task: "), lstTable)
    # Remove Data
    elif strChoice.strip() == '2':
        Processor.remove_data_from_list(int(input("--------------------------------------------------\n"
                                                  "\tThe option to remove a row has been chosen\n"
                                                  "\tWhich row do you wish to delete?\n"
                                                  "--------------------------------------------------\n"
                                                  "\tRow to Delete: ")))
    # Save Data
    elif strChoice.strip() == '3':
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == 'y':
            Processor.save_data_to_file()
        else:
            IO.input_press_to_continue("Save Cancelled!")

    # Reload Data
    elif strChoice.strip() == '4':
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) - ")
        if strChoice.lower() == 'y':
            Processor.reload_file("C:\_PythonClass\ToDoFile.txt",lstTable)
        else:
            IO.input_press_to_continue("File Reload Canceled!")
    # Leave Loop/Script
    elif strChoice == '5':  #  Exit Program
        print("Goodbye!")
        break   # and Exit