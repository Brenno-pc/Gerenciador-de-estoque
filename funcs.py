#imports
from os import system
from time import sleep
from random import randint
from copy import copy


#funcs
def validator_name() -> str:
    """
        -Função que valida o nome do produto.
        -Retornará o valor somente caso ele atenda às condições propostas.
    """
    name_product: str = ""
    has_number: bool = False
    while True:
        try:
            name_product = str(input("Write the name product:  ")).capitalize()
            has_number = any(letter.isnumeric() for letter in name_product)
            if len(name_product) >= 2:
                if has_number == False:
                    print("Name product valid.")
                    sleep(1)
                    system("clear")
                    return name_product
                else:
                    print("Name product invalid, has number.")
                    sleep(1)
                    system("clear")
            else:
                print("Name product invalid.")
                sleep(1)
                system("clear")
        except KeyboardInterrupt:
            print("Program ended.")
            sleep(1)
            system("clear")
            return "No name"
def validator_code() -> int:
    """
        -Função que gera um número de 10 casas (todos aleatórios)
        -Apenas gera o código do produto automaticamente.
    """
    code_product: int = 0
    list_nums: list[int] = []

    list_nums = [randint(1, 9) for _ in range(10)] #precisei tirar randint(0, 9), o 0 acaba não contando...
    code_product = "".join(map(str, list_nums))
    code_product = int(code_product)
    return code_product
def validator_category() -> str:
    """
        -Função que valida a categoria do produto.
        -Todas as categorias disponíveis estão contidas dentro de set.
    """
    list_categorys: list[str] = [
        "electronics", "computers", "gaming", "toys",
        "clothing", "footwear", "jewelry", "beauty",
        "home", "kitchen", "food",
        "pets", "sports", "automotive", "books", "garden",
        "its not contain"
    ]
    category: int = 0
    while True:
        try:
            for index, item in enumerate(list_categorys):
                print(f"[{index}] - {item.upper()}")
            print()

            category = int(input("Write the number of category product:  "))
            if category >= 0 and category <= len(list_categorys)-1:
                print("Category of product valid.")
                sleep(1)
                system("clear")
                return list_categorys[category].capitalize()
            else:
                print("Category of product invalid.")
                sleep(1)
                system("clear")

        except ValueError:
            print("Value is not integer, try again.")
            sleep(1)
            system("clear")
        except KeyboardInterrupt:
            print("Program ended.")
            sleep(1)
            system("clear")
            return "Without category"
def validator_price() -> float:
    """
        -Função que determina o preço do produto.
        -Não permite valores negativos ou nulos.
    """
    price: float = 0.0
    while True:
        try:
            price = float(input("Write the price of product:  $"))
            if price > 0:
                print("Price valid.")
                sleep(1)
                system("clear")
                return price
            else:
                print("Price invalid.")
                sleep(1)
                system("clear")
        except ValueError:
            print("Value decimal invalid, try again.")
            sleep(1)
            system("clear")
        except KeyboardInterrupt:
            print("Program ended.")
            sleep(1)
            system("clear")
            return "Don't has price."
def validator_quantity_stock() -> int:
    """
        -Função que adiciona a quantidade de determinado item.
        -Não permite valores negativos ou nulos.
    """
    quantity: int = 0
    while True:
        try:
            quantity = int(input("Write the quantity of product in stock:  "))
            if quantity > 0:
                print("Quantity valid.")
                sleep(1)
                system("clear")
                return quantity
            else:
                print("Quantity invalid.")
                sleep(1)
                system("clear")
        except ValueError:
            print("Value integer invalid, try again.")
            sleep(1)
            system("clear")
        except KeyboardInterrupt:
            print("Program ended.")
            sleep(1)
            system("clear")
            return "There's no quantity."

def validator_quantity_products() -> int:
    """
        -Função que verifica a quantidade de produtos que será adicionada no banco de dados.
    """
    quantity: int = 0
    while True:
        try:
            quantity = int(input("Write the quantity of product:  "))
            if quantity > 0 and quantity <= 10:
                print("Quantity valid.")
                sleep(1)
                system("clear")
                return quantity
            else:
                print("Quantity invalid.")
                sleep(1)
                system("clear")
        except ValueError:
            print("Value integer invalid, try again.")
            sleep(1)
            system("clear")
        except KeyboardInterrupt:
            print("Program ended.")
            sleep(1)
            system("clear")
            return "Zero items in stock."
def generator_product():
    """
        -Função que gera o "log" do produto completo, acrescentando-o na lista de produtos.
        -Essa lista de produtos será adicionada no banco de dados com o insert
    """
    list_products: list[tuple] = []
    product: tuple = ()

    for _ in range(validator_quantity_products()):
        product = (
            validator_code(),
            validator_name(),
            validator_price(),
            validator_category(),
            validator_quantity_stock()
        )
        list_products.append(copy(product))
        sleep(1)
        system("clear")
    print(list_products)
    for item in list_products:
        print(item)

    return list_products