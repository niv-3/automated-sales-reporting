# End-to-End E-Commerce Sales Reporting Pipeline & Power BI Dashboard

![E-Commerce Sales Performance Dashboard](screenshots/dashboard.png)

An automated sales reporting workflow that transforms raw CSV sales data into cleaned, validated business data and an interactive Power BI dashboard.

The project demonstrates how repetitive sales reporting can be streamlined using Python and Power BI.

## Business Problem

E-commerce businesses often rely on recurring Excel or CSV exports to monitor sales performance. Preparing these reports manually requires repetitive data cleaning, validation, KPI calculations, and dashboard updates.

This project demonstrates how that reporting workflow can be standardized and automated using Python and Power BI.

## Business Value

The workflow replaces repetitive manual data preparation with a reusable reporting pipeline that:

- Validates incoming sales data before processing
- Detects missing fields and invalid numeric values
- Removes duplicate records
- Standardizes dates, products, categories, and customer data
- Automatically calculates revenue and core sales KPIs
- Generates standardized reporting outputs
- Feeds an interactive Power BI dashboard
- Allows the same dashboard to be refreshed when new processed data becomes available

## Solution

```text
Raw CSV / Excel Export
        ↓
Python Data Ingestion
        ↓
Validation
        ↓
Cleaning & Standardization
        ↓
KPI & Revenue Calculation
        ↓
Processed Reporting Data
        ↓
Power BI Dashboard
```

## Dashboard

The Power BI dashboard provides visibility into:

- Total Revenue
- Total Orders
- Total Units Sold
- Average Order Value
- Revenue by Product
- Revenue by Category
- Sales Revenue Trends
- Interactive Date Filtering

## Technologies

- Python
- pandas
- Power BI
- DAX
- CSV / Excel data processing
- Git

## Project Structure

```text
automated-sales-reporting/
│
├── data/
│   └── sales.csv
│
├── output/
│   ├── cleaned_sales.csv
│   ├── sales_metrics.csv
│   └── revenue_by_product.csv
│
├── pipeline/
│   ├── ingest.py
│   ├── validate.py
│   ├── clean.py
│   ├── metrics.py
│   ├── output.py
│   └── main.py
│
├── screenshots/
│   └── dashboard.png
│
├── generate_demo_data.py
└── README.md
```

## How It Works

### 1. Ingestion
The pipeline loads raw sales transaction data from CSV.

### 2. Validation
Required columns and numeric fields are checked before processing. Invalid data can stop the pipeline before incorrect results reach the report.

### 3. Cleaning
The workflow removes duplicate rows, standardizes dates and text fields, and converts numeric fields into appropriate formats.

### 4. KPI Calculation
The pipeline calculates revenue and key business metrics including total revenue, order count, units sold, and average order value.

### 5. Output
Processed reporting files are automatically generated in the `output` directory.

### 6. Power BI
Power BI consumes the processed sales data and provides an interactive dashboard. When new data is processed, the existing dashboard can be refreshed instead of rebuilt manually.

## Running the Demo

Install the required Python packages:

```bash
pip install pandas openpyxl
```

Generate the synthetic demonstration dataset:

```bash
python generate_demo_data.py
```

Run the reporting pipeline:

```bash
python pipeline/main.py
```

The processed reporting files will be created in the `output` directory.

## Demo Data

The included dataset is **synthetic demonstration data generated specifically for this project**.

It does not represent a real company, customer, or actual business revenue.

The demo dataset contains 1,000 generated e-commerce orders across multiple products and categories.

## Potential Business Use

The workflow can be adapted for businesses that repeatedly work with sales exports from spreadsheets or other systems.

Future/custom implementations could include:

- Customer-specific Excel/CSV formats
- Database connections
- API integrations
- Scheduled data processing
- Automated dashboard refresh
- Additional business KPIs

## Author

**Victor Nwaigwe**

MSc Computational Sciences — Freie Universität Berlin

GitHub: https://github.com/niv-3