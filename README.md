# A dynamic sales analytics and reporting application built with Python, pandas, and Streamlit.

The application allows businesses to upload a sales CSV, map their own column names to a standard sales structure, automatically validate and clean the data, calculate business KPIs, visualize sales performance, and download processed results.

## 🚀 Live Demo

Try the deployed application:

[**Open Automated Sales Analytics**](https://automated-sales-reporting-c67g8dsprdcygxsjqcpswh.streamlit.app/)

Upload a sales CSV, map your columns, run the analysis, explore the KPIs and charts, and download the processed results.

## Features

- Upload sales data in CSV format
- Dynamic column mapping
- Automatic recognition of common sales column names
- Data validation and cleaning
- Revenue calculation
- Total revenue, orders, units sold, and average order value
- Revenue trend analysis
- Top product analysis
- Revenue by category
- Top customer analysis
- Currency selection
- Download cleaned sales data
- Download calculated business metrics
- Browser-based Streamlit interface

## Dynamic Data Mapping

Different businesses often use different column names.

For example:

| Customer CSV | Internal Field |
|---|---|
| Order_ID | order_id |
| Order_Date | date |
| Product_Name | product |
| Product_Category | category |
| Quantity | quantity |
| Unit_Price | unit_price |
| Customer_Name | customer |

The application automatically detects common column names where possible and allows the user to manually map unfamiliar columns.

This means the analytics pipeline is not restricted to one fixed CSV structure.

## Analytics Pipeline

```text
CSV Upload
    ↓
Column Mapping
    ↓
Data Validation
    ↓
Data Cleaning
    ↓
Standardized Sales Data
    ↓
Business Metric Calculation
    ↓
Interactive Dashboard
    ↓
Downloadable Results
