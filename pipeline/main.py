from pipeline.ingest import load_sales_data
from pipeline.validate import validate_sales_data
from pipeline.clean import clean_sales_data
from pipeline.metrics import calculate_metrics
from pipeline.output import save_outputs
from pipeline.mapping import map_sales_columns


def run_sales_pipeline(file_source, column_mapping=None, save_files=False):
    """
    Run the complete sales analytics pipeline.

    file_source can be:
    - a local CSV path
    - a Streamlit uploaded CSV file

    column_mapping allows customer column names
    to be converted to our standard schema.
    """

    # Load CSV
    sales_data = load_sales_data(file_source)

    # Convert customer columns to our standard format
    if column_mapping:
        sales_data = map_sales_columns(
            sales_data,
            column_mapping
        )

    # Validate standardized data
    validate_sales_data(sales_data)

    # Clean data
    sales_data = clean_sales_data(sales_data)

    # Calculate business metrics
    sales_data, metrics, revenue_by_product = calculate_metrics(
        sales_data
    )

    # Saving is optional because Streamlit doesn't need
    # to write files to disk every time somebody uploads a CSV.
    if save_files:
        save_outputs(
            sales_data,
            metrics,
            revenue_by_product
        )

    return sales_data, metrics, revenue_by_product


def main():
    """
    Keep our original local test working.
    """

    file_path = "data/sales.csv"

    sales_data, metrics, revenue_by_product = run_sales_pipeline(
        file_path,
        save_files=True
    )

    print(sales_data)

    print("\nBusiness Metrics:")
    print(metrics)


if __name__ == "__main__":
    main()