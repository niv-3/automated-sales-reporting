def calculate_metrics(data):
    """ calculate key sales metrics"""

    data = data.copy()

    data["revenue"] = data["quantity"] * data["unit_price"]

    revenue_by_product = (
        data.groupby("product")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    total_revenue = data["revenue"].sum()
    total_orders = data["order_id"].nunique()
    total_units = data["quantity"].sum()
    average_order_value = total_revenue/ total_orders

    metrics = {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "total_units": total_units,
        "average_order_value": average_order_value
    }

    return data, metrics, revenue_by_product
