from utils.menu import find_item

class User:
  bill = 0

  def __init__(self, id: int, name: str, socket: str, table_id: int) -> None:
      self.id = id
      self.name = name
      self.socket = socket
      self.table_id = table_id
      self.orders = []

  def add_order(self, order_id: int) -> None:
    order = find_item(order_id)

    self.bill += order["price"]

    if order:
      self.orders.append(order)

  def get_orders(self) -> None:
    print(f"| {self.name} |\n")

    for order in self.orders:
      print(f"{order['name']} -> {order['price']}")
      print("--------------------------------------------------")

    print(f"\nTotal: R$ {format(self.bill, '.2f')}")
    print("--------------------------------------------------\n")

if __name__ == "__main__":
  user = User(0, "Teste", "128.65.27.104:5000", 5)

  user.add_order(1)
  user.add_order(2)
  user.add_order(11)
  user.add_order(1)
  user.add_order(3)
  user.get_orders()
