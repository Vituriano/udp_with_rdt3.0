from Waiter import Waiter
from User import User

users = {}
idcount = 0
waiter = Waiter()
def menu():
    output = "\n\n1 - cardápio\n"
    output += "2 - pedido\n"
    output += "3 - conta individual\n"
    output += "4 - não fecho com robô, chame seu gerente\n"
    output += "5 - nada não, tava só testando\n"
    output += "6 - conta da mesa\n"
    return output

def option(content:str, address:str):
    if address not in users:    
        users[address] = {"id": idcount, "table": None, "name": None}
        return "Digite sua mesa"
    else:
        if users[address]["table"] == None:
            users[address]["table"] = int(content)
            return "Digite seu nome"
        elif users[address]["name"] == None:
            users[address]["name"] = content
            user = User(users[address]["id"],users[address]["name"], address, users[address]["table"])
            waiter.add_user_to_list_of_clients(user)
            return menu()
        else:
            if int(content) == 1:
                return waiter.show_menu()
