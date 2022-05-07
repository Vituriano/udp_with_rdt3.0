from utils.menu import find_item

class User:
  def __init__(self, id: int, name: str, socket: str) -> None:
      self.id = id
      self.name = name
      self.socket = socket
      self.orders = []

  def add_order(self, order_id: int) -> None:
    order = find_item(order_id)

    if order:
      self.orders.append(order)

  def get_orders(self) -> int:
    total = 0

    print(f"| {self.name} |\n")

    for order in self.orders:
      total += order['price']

      print(f"{order['name']} -> {order['price']}")
      print("--------------------------------------------------")

    print(f"\nTotal: R$ {format(total, '.2f')}")
    print("--------------------------------------------------\n")

    return total

if __name__ == "__main__":
  user = User(0, "Teste", "128.65.27.104:5000")

  user.add_order(1)
  user.add_order(2)
  user.add_order(11)
  user.add_order(1)
  user.add_order(3)
  user.get_orders()
