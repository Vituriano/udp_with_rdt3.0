# cardapio OK
# criar usuário OK
# adicionar à mesa
# realizar pedido OK
# conta do usuário OK
# conta da mesa OK
# pagar
# levantar da mesa OK

from User import User
from utils.menu import menu


class Waiter:
  name = "CInToFome"
  menu = menu
  list_of_clients = []

  def show_menu(self) -> None:
    print("Menu:\n")

    for item in menu:
      print(f"{item['id']} | {item['name']} - {item['price']}")
      print("--------------------------------------------------")

    print("\n")

  def add_user_to_list_of_clients(self, user: User) -> None:
    self.list_of_clients.append(user)

  def show_table_orders(self, user_id: int) -> None:
    table_total = 0

    user = self.__find_user(user_id)

    table_id = user.table_id

    for user in self.list_of_clients:
      if user.table_id == table_id:
        table_total += user.get_orders()

    print(f"\nTotal da mesa: R$ {format(table_total, '.2f')}")
    print("--------------------------------------------------\n\n")

  def show_individual_orders(self, user_id: int) -> None:
    user = self.__find_user(user_id)
    user.get_orders()

  def __find_user(self, user_id: int) -> User:
    for user in self.list_of_clients:
      if user.id == user_id:
        return user

  def remove_user_from_list(self, user_id: int) -> bool:
    updated_list_of_clients = [user for user in self.list_of_clients if not (user.id == user_id)]

    self.list_of_clients = updated_list_of_clients

    return True


if __name__ == "__main__":
  waiter = Waiter()
  user = User(0, "Teste", "128.65.27.104:5000", 5)
  user2 = User(1, "Outro Teste", "128.65.27.104:5500", 5)
  user3 = User(2, "Mais um Teste", "128.65.27.104:5550", 4)

  waiter.add_user_to_list_of_clients(user)
  waiter.add_user_to_list_of_clients(user2)
  waiter.add_user_to_list_of_clients(user3)

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

  user3.add_order(12)
  user3.add_order(12)
  user3.add_order(12)
  user3.add_order(5)
  user3.add_order(8)
  user3.add_order(7)

  waiter.show_table_orders(user.id)
  waiter.show_table_orders(user3.id)
  waiter.show_individual_orders(user.id)

  waiter.remove_user_from_list(0)
  waiter.remove_user_from_list(1)
  waiter.remove_user_from_list(2)
  waiter.remove_user_from_list(0)
