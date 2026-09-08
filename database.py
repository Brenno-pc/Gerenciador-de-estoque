#imports
from os import system
from time import sleep

import sqlite3



#ordem tabela:
    #-código
    #-nome
    #-preço
    #-categoria
    #-quantidade em estoque


#funcs
def nominator(what: str) -> str:
    """
        -Função que nomeia database, tables, etc.
        -O "what" representa o que será nomeado, database, tabela, etc.
    """
    name: str = ""
    has_number: bool = False
    while True:
        try:
            name = str(input(f"Write the name of {what}:  ")).capitalize()
            has_number = any(letter.isnumeric() for letter in name)
            if len(name) >= 2:
                if has_number == False:
                    print(f"Name of {what} valid.")
                    sleep(1)
                    system("clear")
                    return name
                else:
                    print(f"Name of {what} invalid, has number.")
                    sleep(1)
                    system("clear")
            else:
                print(f"Name of {what} invalid.")
                sleep(1)
                system("clear")
        except KeyboardInterrupt:
            print("Program ended.")
            sleep(1)
            system("clear")
            return f"{what.capitalize()} No Name"

def create_database() -> None:
    pass

def manipulation_database() -> None:
    pass

with sqlite3.connect("data.db") as database:
    pass




def add_registers():
    pass
def remove_registers():
    pass
def show_registers():
    pass



#main program