import random
from datetime import datetime, timedelta

import pandas as pd


random.seed(42)

products = {
    "Laptop": ("Electronics", 899.99),
    "Wireless Mouse": ("Electronics", 29.99),
    "Mechanical Keyboard": ("Electronics", 89.99),
    "Monitor": ("Electronics", 249.99),
    "Headphones": ("Electronics", 79.99),
    "Office Chair": ("Furniture", 229.99),
    "Standing Desk": ("Furniture", 449.99),
    "Desk Lamp": ("Furniture", 49.99),
    "Backpack": ("Accessories", 69.99),
    "Laptop Stand": ("Accessories", 39.99),
}

start_date = datetime(2026, 4, 1)

rows = []

for order_id in range(10001, 11001):

    product = random.choice(list(products.keys()))
    category, unit_price = products[product]

    date = start_date + timedelta(days=random.randint(0, 182))
    quantity = random.choices(
        [1, 2, 3, 4],
        weights=[70, 20, 7, 3]
    )[0]

    customer = f"Customer {random.randint(1, 250)}"

    rows.append({
        "order_id": order_id,
        "date": date.strftime("%Y-%m-%d"),
        "product": product,
        "category": category,
        "quantity": quantity,
        "unit_price": unit_price,
        "customer": customer
    })


data = pd.DataFrame(rows)

data = data.sort_values("date")

data.to_csv("data/sales.csv", index=False)

print(f"Demo dataset created: {len(data)} orders")