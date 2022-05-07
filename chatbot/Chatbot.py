# cardapio OK
# criar usuário e adicionar à mesa OK
# realizar pedido OK
# conta do usuário OK
# conta da mesa OK
# chamar o gerente

from User import User
from utils.menu import menu


class Waiter:
  name = "CInToFome"
  menu = menu
  table = []

  def show_menu(self) -> None:
    print("Menu:\n")

    for item in menu:
      print(f"{item['id']} | {item['name']} - {item['price']}")
      print("--------------------------------------------------")

    print("\n")

  def add_user_to_table(self, user: User):
    self.table.append(user)

  def show_table_orders(self):
    table_total = 0

    for user in self.table:
      table_total += user.get_orders()

    print(f"\nTotal da mesa: R$ {format(table_total, '.2f')}")
    print("--------------------------------------------------\n\n")

  def show_individual_orders(self, user_id: int):
    for user in self.table:
      if user.id == user_id:
        user.get_orders()


if __name__ == "__main__":
  waiter = Waiter()
  user = User(0, "Teste", "128.65.27.104:5000")
  user2 = User(1, "Outro Teste", "128.65.27.104:5500")

  waiter.add_user_to_table(user)
  waiter.add_user_to_table(user2)

  waiter.show_menu()

  user.add_order(1)
  user.add_order(2)
  user.add_order(11)
  user.add_order(1)
  user.add_order(3)

  user2.add_order(12)
  user2.add_order(5)
  user2.add_order(8)
  user2.add_order(7)

  waiter.show_table_orders()
  waiter.show_individual_orders(0)
