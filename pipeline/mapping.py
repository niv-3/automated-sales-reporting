def map_sales_columns(data, column_mapping):
    """
    Convert customer CSV column names into the standard
    column names used by the sales analytics pipeline.

    Example:
        "Order Number" -> "order_id"
        "Sale Date" -> "date"
        "Item Name" -> "product"
    """

    data = data.copy()

    # Reverse the mapping because pandas.rename expects:
    # existing_name -> new_name
    rename_mapping = {
        customer_column: standard_column
        for standard_column, customer_column in column_mapping.items()
    }

    data = data.rename(columns=rename_mapping)

    return data