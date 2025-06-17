items = [
    {"name": "Rice (1kg)", "price": 60, "quantity": 2},
    {"name": "Sugar (1kg)", "price": 45, "quantity": 1},
    {"name": "Milk (1L)", "price": 52, "quantity": 4},
    {"name": "Cooking Oil (1L)", "price": 130, "quantity": 1}
]
total_cost = 0
for item in items:
    item_cost = item["price"] * item["quantity"]
    print(f"{item['name']} - ₹{item['price']} x {item['quantity']} = ₹{item_cost}")
    total_cost += item_cost
print("\nTotal Bill: ₹", total_cost)
