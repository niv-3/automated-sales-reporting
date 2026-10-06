import streamlit as st
import pandas as pd

from pipeline.main import run_sales_pipeline


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Automated Sales Analytics",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("📊 Automated Sales Analytics")

st.write(
    "Upload your sales CSV, match your columns, "
    "and automatically generate business insights."
)


# --------------------------------------------------
# CURRENCY
# --------------------------------------------------

currency_options = {
    "Euro (€)": "€",
    "US Dollar ($)": "$",
    "British Pound (£)": "£",
    "Nigerian Naira (₦)": "₦"
}

selected_currency = st.selectbox(
    "Currency",
    list(currency_options.keys())
)

currency_symbol = currency_options[selected_currency]


# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Sales CSV",
    type=["csv"]
)


if uploaded_file is not None:

    try:

        data = pd.read_csv(uploaded_file)

        st.success("CSV uploaded successfully!")


        # --------------------------------------------------
        # FILE INFORMATION
        # --------------------------------------------------

        st.subheader("Data Preview")

        st.dataframe(
            data.head(10),
            use_container_width=True
        )

        st.write(
            f"**{len(data):,} rows** and "
            f"**{len(data.columns)} columns** detected."
        )


        # --------------------------------------------------
        # COLUMN MAPPING
        # --------------------------------------------------

        st.subheader("Match Your Columns")

        st.write(
            "Match the columns in your file to the fields "
            "required for sales analysis."
        )

        columns = list(data.columns)


        def guess_column(possible_names):

            for column in columns:

                normalized = (
                    column.lower()
                    .strip()
                    .replace(" ", "_")
                    .replace("-", "_")
                )

                if normalized in possible_names:
                    return column

            return None


        field_options = {

            "order_id": [
                "order_id",
                "order_number",
                "order_no",
                "order_number_id",
                "invoice",
                "invoice_id",
                "transaction_id",
                "transaction"
            ],

            "date": [
                "date",
                "sale_date",
                "sales_date",
                "order_date",
                "purchase_date",
                "transaction_date",
                "order_purchase_timestamp"
            ],

            "product": [
                "product",
                "product_name",
                "item",
                "item_name",
                "product_id",
                "sku"
            ],

            "category": [
                "category",
                "product_category",
                "product_category_name",
                "department"
            ],

            "quantity": [
                "quantity",
                "qty",
                "units",
                "units_sold",
                "quantity_sold"
            ],

            "unit_price": [
                "unit_price",
                "price",
                "selling_price",
                "sale_price",
                "item_price"
            ],

            "customer": [
                "customer",
                "customer_name",
                "customer_id",
                "buyer",
                "buyer_name",
                "client",
                "client_name"
            ]
        }


        labels = {
            "order_id": "Order ID",
            "date": "Date",
            "product": "Product",
            "category": "Category",
            "quantity": "Quantity",
            "unit_price": "Unit Price",
            "customer": "Customer"
        }


        column_mapping = {}


        for standard_field, possible_names in field_options.items():

            guessed_column = guess_column(possible_names)

            options = ["-- Select Column --"] + columns

            if guessed_column:
                default_index = options.index(guessed_column)
            else:
                default_index = 0

            selected_column = st.selectbox(
                labels[standard_field],
                options,
                index=default_index,
                key=f"mapping_{standard_field}"
            )

            if selected_column != "-- Select Column --":
                column_mapping[standard_field] = selected_column


        # --------------------------------------------------
        # ANALYZE
        # --------------------------------------------------

        st.divider()

        if st.button(
            "📊 Analyze Sales",
            type="primary",
            use_container_width=True
        ):

            required_fields = list(field_options.keys())

            missing_fields = [
                labels[field]
                for field in required_fields
                if field not in column_mapping
            ]


            if missing_fields:

                st.error(
                    "Please select columns for: "
                    + ", ".join(missing_fields)
                )


            else:

                try:

                    uploaded_file.seek(0)

                    cleaned_data, metrics, revenue_by_product = (
                        run_sales_pipeline(
                            uploaded_file,
                            column_mapping=column_mapping,
                            save_files=False
                        )
                    )


                    # --------------------------------------------------
                    # VALIDATE RESULTS
                    # --------------------------------------------------

                    if cleaned_data.empty:

                        st.warning(
                            "No usable sales records were found "
                            "after processing the file."
                        )

                        st.stop()


                    st.success(
                        "Sales analysis completed successfully!"
                    )


                    # --------------------------------------------------
                    # DATE INFORMATION
                    # --------------------------------------------------

                    valid_dates = cleaned_data["date"].dropna()

                    if not valid_dates.empty:

                        start_date = valid_dates.min()
                        end_date = valid_dates.max()

                        st.caption(
                            f"Analysis period: "
                            f"{start_date.strftime('%d %b %Y')} – "
                            f"{end_date.strftime('%d %b %Y')}"
                        )


                    # --------------------------------------------------
                    # KPI CARDS
                    # --------------------------------------------------

                    st.subheader("Business Overview")

                    col1, col2, col3, col4 = st.columns(4)


                    col1.metric(
                        "Total Revenue",
                        f"{currency_symbol}"
                        f"{metrics['total_revenue']:,.2f}"
                    )


                    col2.metric(
                        "Total Orders",
                        f"{metrics['total_orders']:,}"
                    )


                    col3.metric(
                        "Units Sold",
                        f"{metrics['total_units']:,.0f}"
                    )


                    col4.metric(
                        "Average Order Value",
                        f"{currency_symbol}"
                        f"{metrics['average_order_value']:,.2f}"
                    )


                    # --------------------------------------------------
                    # REVENUE TREND
                    # --------------------------------------------------

                    st.subheader("Revenue Over Time")

                    revenue_over_time = (
                        cleaned_data
                        .dropna(subset=["date"])
                        .groupby("date")["revenue"]
                        .sum()
                        .sort_index()
                    )

                    if not revenue_over_time.empty:

                        st.line_chart(
                            revenue_over_time
                        )

                    else:

                        st.info(
                            "Revenue trend could not be generated "
                            "because no valid dates were found."
                        )


                    # --------------------------------------------------
                    # PRODUCT + CATEGORY ANALYSIS
                    # --------------------------------------------------

                    chart_col1, chart_col2 = st.columns(2)


                    with chart_col1:

                        st.subheader("Top Products")

                        top_products = (
                            revenue_by_product
                            .head(10)
                        )

                        st.bar_chart(
                            top_products
                        )


                    with chart_col2:

                        st.subheader("Revenue by Category")

                        revenue_by_category = (
                            cleaned_data
                            .groupby("category")["revenue"]
                            .sum()
                            .sort_values(ascending=False)
                        )

                        st.bar_chart(
                            revenue_by_category
                        )


                    # --------------------------------------------------
                    # TOP CUSTOMERS
                    # --------------------------------------------------

                    st.subheader("Top Customers")

                    top_customers = (
                        cleaned_data
                        .groupby("customer")["revenue"]
                        .sum()
                        .sort_values(ascending=False)
                        .head(10)
                    )

                    st.bar_chart(
                        top_customers
                    )


                    # --------------------------------------------------
                    # CLEANED DATA
                    # --------------------------------------------------

                    st.subheader("Cleaned Sales Data")

                    st.dataframe(
                        cleaned_data,
                        use_container_width=True
                    )


                    # --------------------------------------------------
                    # DOWNLOADS
                    # --------------------------------------------------

                    st.subheader("Download Results")

                    cleaned_csv = cleaned_data.to_csv(
                        index=False
                    ).encode("utf-8")


                    metrics_download = pd.DataFrame(
                        {
                            "Metric": [
                                "Total Revenue",
                                "Total Orders",
                                "Units Sold",
                                "Average Order Value"
                            ],

                            "Value": [
                                metrics["total_revenue"],
                                metrics["total_orders"],
                                metrics["total_units"],
                                metrics["average_order_value"]
                            ]
                        }
                    )


                    metrics_csv = metrics_download.to_csv(
                        index=False
                    ).encode("utf-8")


                    download_col1, download_col2 = st.columns(2)


                    with download_col1:

                        st.download_button(
                            label="⬇️ Download Cleaned Sales Data",
                            data=cleaned_csv,
                            file_name="cleaned_sales.csv",
                            mime="text/csv",
                            use_container_width=True
                        )


                    with download_col2:

                        st.download_button(
                            label="⬇️ Download Business Metrics",
                            data=metrics_csv,
                            file_name="sales_metrics.csv",
                            mime="text/csv",
                            use_container_width=True
                        )


                except Exception as error:

                    st.error(
                        f"Analysis failed: {error}"
                    )


    except Exception as error:

        st.error(
            f"Could not process the CSV: {error}"
        )