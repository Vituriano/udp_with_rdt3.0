# Cardapio OK
# realizar pedido
# conta do usuario
# Chamar o gerente

from utils.menu import menu


class Waiter:
  name = "CInToFome"
  menu = menu

  def show_menu(self):
    for item in menu:
      print(f"{item['id']} | {item['name']} - {item['price']}")
      print("--------------------------------------------------")


if __name__ == "__main__":
  waiter = Waiter()

  waiter.show_menu()
