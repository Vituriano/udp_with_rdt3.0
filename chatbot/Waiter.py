# cardapio OK
# criar usuário OK
# adicionar à mesa
# realizar pedido OK
# conta do usuário OK
# conta da mesa OK
# pagar OK
# levantar da mesa OK

from User import User
from Table import Table
from utils.menu import menu


class Waiter:
  name = "CInToFome"
  menu = menu
  list_of_clients = []
  list_of_tables: list[Table] = []

  def show_menu(self) -> None:
    print("Menu:\n")

    for item in menu:
      print(f"{item['id']} | {item['name']} - {item['price']}")
      print("--------------------------------------------------")

    print("\n")

  def add_user_to_list_of_clients(self, user: User) -> None:
    table = self.__find_table(user)

    if not table:
      new_table = Table(user.table_id)
      new_table.clients = []
      new_table.clients.append(user)
      self.list_of_tables.append(new_table)
    else:
      table.clients.append(user)

    self.list_of_clients.append(user)

  def show_table_orders(self, user_id: int) -> None:
    user = self.__find_user(user_id)

    table_id = user.table_id

    for table in self.list_of_tables:
      if table.id == table_id:
        table.get_table_total()

  def show_individual_orders(self, user_id: int) -> None:
    user = self.__find_user(user_id)
    user.get_orders()

  def user_order(self, user_id: int, order_id: int) -> None:
    user = self.__find_user(user_id)

    table = self.__find_table(user)

    table.compute_user_order(user_id, order_id)

  def __find_user(self, user_id: int) -> User:
    for user in self.list_of_clients:
      if user.id == user_id:
        return user

  def __find_table(self, user: User) -> Table:
    for table in self.list_of_tables:
      if table.id == user.table_id:
        return table

  def remove_user_from_list(self, user_id: int) -> bool:
    user = self.__find_user(user_id)

    if user:
      table = self.__find_table(user)

      if table:
        updated_list_of_clients = [user for user in self.list_of_clients if not (user.id == user_id)]
        self.list_of_clients = updated_list_of_clients

        table_updated_list_of_clients = [user for user in table.clients if not (user.id == user_id)]
        table.clients = table_updated_list_of_clients

        return True

    return False


if __name__ == "__main__":
  waiter = Waiter()
  user = User(0, "Teste", "128.65.27.104:5000", 5)
  user2 = User(1, "Outro Teste", "128.65.27.104:5500", 5)
  user3 = User(2, "Mais um Teste", "128.65.27.104:5550", 4)

  waiter.add_user_to_list_of_clients(user)
  waiter.add_user_to_list_of_clients(user2)
  waiter.add_user_to_list_of_clients(user3)

  waiter.show_menu()

  waiter.user_order(user.id, 1)
  waiter.user_order(user.id, 2)
  waiter.user_order(user.id, 11)
  waiter.user_order(user.id, 1)
  waiter.user_order(user.id, 13)

  waiter.user_order(user2.id, 12)
  waiter.user_order(user2.id, 5)
  waiter.user_order(user2.id, 8)
  waiter.user_order(user2.id, 7)

  waiter.user_order(user3.id, 12)
  waiter.user_order(user3.id, 12)
  waiter.user_order(user3.id, 12)
  waiter.user_order(user3.id, 5)
  waiter.user_order(user3.id, 8)
  waiter.user_order(user3.id, 7)

  waiter.show_table_orders(user.id)
  waiter.show_table_orders(user3.id)
  waiter.show_individual_orders(user.id)

  waiter.remove_user_from_list(0)
  waiter.remove_user_from_list(1)
  waiter.remove_user_from_list(2)
  waiter.remove_user_from_list(0)
