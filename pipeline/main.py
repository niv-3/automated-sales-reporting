from ingest import load_sales_data
from validate import validate_sales_data
from clean import clean_sales_data
from metrics import calculate_metrics
from output import save_outputs


def main():

    file_path = "data/sales.csv"
    sales_data = load_sales_data(file_path)

    print("Sales data loaded successfully!")

    validate_sales_data(sales_data)

    sales_data = clean_sales_data(sales_data)

    sales_data, metrics, revenue_by_product = calculate_metrics(sales_data)

    save_outputs(sales_data, metrics, revenue_by_product)





    print(sales_data)

    print("\nBusiness Metrics:")
    print(metrics)


if __name__ == "__main__":
    main()