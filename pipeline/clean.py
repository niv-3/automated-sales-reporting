import pandas as pd 


def clean_sales_data(data):
    """ clean and standardise sales data """

    data = data.copy()

    # Remove duplicate rows
    data = data.drop_duplicates()

    #convert date column to datetime
    data["date"] = pd.to_datetime(data["date"], errors = "coerce")

    #clean text columns
    data["product"] = data["product"].str.strip().str.title()
    data["category"] = data["category"].str.strip().str.title()
    data["customer"] = data["customer"].str.strip().str.title()

    #covert numeric columns
    data["quantity"] = pd.to_numeric(data["quantity"], errors = "coerce")
    data["unit_price"] = pd.to_numeric(data["unit_price"], errors = "coerce")

    return data

