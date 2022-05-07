from User import User
from utils.menu import find_item

class Table:
  clients: list[User] = []
  table_total = 0

  def __init__(self, id: int) -> None:
      self.id = id

  def add_user(self, user: User) -> None:
    self.clients.append(user)

  def remove_user(self, user_id: int) -> bool:
    updated_list_of_clients = [user for user in self.clients if not (user.id == user_id)]

    self.clients = updated_list_of_clients

    return True

  def get_table_total(self) -> None:
    total = 0

    for user in self.clients:
      total += user.get_orders()

    print(f"\nTotal da mesa: R$ {format(total, '.2f')}")
    print("--------------------------------------------------\n\n")

  def __find_user(self, user_id: int) -> User:
    for user in self.clients:
      if user.id == user_id:
        return user

  def compute_user_order(self, user_id: int, order_id: int) -> None:
    user = self.__find_user(user_id)

    if user:
      item = find_item(order_id)

      if item:
        user.add_order(order_id)
        table_total += item['price']
