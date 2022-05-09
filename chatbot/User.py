from chatbot.utils.menu import find_item

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

  def get_orders(self) -> str:
    output = f"| {self.name.decode()} |\n"

    for order in self.orders:
      output += f"{order['name']} -> {order['price']}\n"
      output += "--------------------------------------------------\n"

    output += f"\nTotal: R$ {format(self.bill, '.2f')}\n"
    output += "--------------------------------------------------\n"
    return output

if __name__ == "__main__":
  user = User(0, "Teste", "128.65.27.104:5000", 5)

  user.add_order(1)
  user.add_order(2)
  user.add_order(11)
  user.add_order(1)
  user.add_order(3)
  user.get_orders()
