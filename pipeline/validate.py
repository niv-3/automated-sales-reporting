import pandas as pd

def validate_sales_data(data):
    """validate that the sales data contains the required columns."""

    required_columns = [
        "order_id",
        "date",
        "product",
        "category",
        "quantity",
        "unit_price",
        "customer"
    ]

    missing_columns =[
        column for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"missing required columns: {missing_columns}"
        )

    #check for completely empty required values

    missing_values = data[required_columns].isnull().sum()

    missing_values = missing_values[missing_values > 0]

    if not missing_values.empty:
        print("\nWarning: Missing values detected:")
        print(missing_values)


    #check that quantity and unit_ptice contain numeric values
    numeric_columns = ["quantity", "unit_price"]

    for column in numeric_columns:
        converted = pd.to_numeric(data[column], errors = "coerce")

        invalid_count = converted.isnull().sum() - data[column].isnull().sum()

        if invalid_count > 0:
            raise ValueError(
                f"{column} contains {invalid_count} invalid numeric value(s)"
            )


    return True

