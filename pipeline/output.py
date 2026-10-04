import os
import pandas as pd


def save_outputs(data, metrics, revenue_by_product, output_folder="output"):
    """Save processed sales data and business metrics."""

    os.makedirs(output_folder, exist_ok=True)

    data.to_csv(
        f"{output_folder}/cleaned_sales.csv",
        index=False
    )

    metrics_data = {
        "metric": list(metrics.keys()),
        "value": list(metrics.values())
    }

    metrics_df = pd.DataFrame(metrics_data)

    metrics_df.to_csv(
        f"{output_folder}/sales_metrics.csv",
        index=False
    )

    revenue_by_product_df = revenue_by_product.reset_index()

    revenue_by_product_df.to_csv(
        f"{output_folder}/revenue_by_product.csv",
        index=False
    )

    print("Output files saved successfully!")