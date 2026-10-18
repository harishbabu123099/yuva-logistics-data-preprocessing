"""
Week 2 - Logistics Data Collection, Cleaning, and Preprocessing
Run: pip install pandas numpy
     python logistics_preprocessing.py
Note: This is a demonstration using a small synthetic sample dataset.
"""
import pandas as pd
import numpy as np

INPUT_FILE = "logistics_shipments_sample.csv"
OUTPUT_FILE = "logistics_shipments_cleaned.csv"

# 1. Data collection: load the reference dataset from a local CSV file.
df = pd.read_csv(INPUT_FILE)
print("Rows and columns before cleaning:", df.shape)
print(df.head())

# 2. Standardise column names and text fields.
df.columns = df.columns.str.strip().str.lower()
for col in ["origin", "destination"]:
    df[col] = df[col].astype("string").str.strip().str.title()

# 3. Convert columns to appropriate data types.
numeric_cols = ["distance_km", "transit_days", "shipping_cost_inr"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df["dispatch_date"] = pd.to_datetime(df["dispatch_date"], errors="coerce")

# 4. Remove duplicate shipment records.
df = df.drop_duplicates(subset=["shipment_id"], keep="first")

# 5. Handle missing numeric values using the median.
# Median is less affected by extreme values than the mean.
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# 6. Detect extreme values using the IQR rule and cap them at the bounds.
# This keeps rows for a small teaching dataset; real projects should investigate first.
for col in numeric_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    df[col] = df[col].clip(lower=lower, upper=upper)

# 7. Add a derived metric useful for logistics analysis.
df["cost_per_km_inr"] = (df["shipping_cost_inr"] / df["distance_km"]).round(2)
df["dispatch_month"] = df["dispatch_date"].dt.to_period("M").astype("string")

# 8. Normalise distance and cost to a 0-1 scale (min-max normalisation).
for col in ["distance_km", "shipping_cost_inr"]:
    minimum, maximum = df[col].min(), df[col].max()
    output_col = col + "_normalised"
    if maximum != minimum:
        df[output_col] = ((df[col] - minimum) / (maximum - minimum)).round(4)
    else:
        df[output_col] = 0.0

# 9. Save cleaned data and basic quality summary.
df.to_csv(OUTPUT_FILE, index=False)
print("Rows and columns after cleaning:", df.shape)
print("Missing values after cleaning:\\n", df.isna().sum())
print("Cleaned data saved to:", OUTPUT_FILE)
