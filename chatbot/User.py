from utils.menu import find_item

class User:
  def __init__(self, id: int, name: str, socket: str, orders: list[dict] = []) -> None:
      self.id = id
      self.name = name
      self.socket = socket
      self.orders = orders

  def add_order(self, order_id: int) -> None:
    order = find_item(order_id)

    if order:
      self.orders.append(order)

  def print_orders(self) -> None:
    print(f"| {self.name} |\n")

    for order in self.orders:
      print(f"{order['name']} -> {order['price']}")
      print("--------------------------------------------------")

if __name__ == "__main__":
  user = User(0, "Teste", "128.65.27.104:5000")

  user.add_order(1)
  user.add_order(2)
  user.add_order(11)
  user.add_order(1)
  user.add_order(3)
  user.print_orders()
