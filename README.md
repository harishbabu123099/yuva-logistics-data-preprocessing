# Logistics Data Collection, Cleaning, and Preprocessing

YUVA Internship – Week 2 task.

## Files
- `logistics_shipments_sample.csv`: synthetic sample shipment data with intentional quality issues.
- `logistics_preprocessing.py`: pandas-based cleaning and preprocessing pipeline.
- `logistics_shipments_cleaned.csv`: sample output produced by the pipeline.
- `YUVA_Week2_Logistics_Preprocessing_Report.docx`: task report.

## Run
Install dependencies:
```bash
pip install pandas numpy
```
Run in the folder containing the files:
```bash
python logistics_preprocessing.py
```

## Methods
- Standardise text and column names
- Convert data types
- Remove duplicate shipment IDs
- Fill missing numeric values with medians
- Cap IQR-based outliers for demonstration
- Calculate shipping cost per kilometre
- Normalise distance and cost using min-max scaling
- Export and validate the cleaned dataset

**Important:** The data is synthetic and intended for learning only. In a real logistics project, investigate unusual records and document any business decisions before changing them.
