# Data Integrity Audit for Property Records

## Overview
Data integrity audit using Python and Pandas. 
It checks a mock dataset (propety_data.csv) for integrity issues (missing values, inconsistent values and duplicates)

## Dataset
File: `property_data.csv`
Format: tab separated values (tsv)

## Column
Property ID - unique ID
Address - Property address
Postcode - Suburb postcode 
Land_Area - How much land in square meters (some negative)
Sale Date - Date sold
Sale price - Sale price in AUD

## Script checks

### Missing values:
- Detects any blank (`NULL`) entries in each column
- Printed summary of missing values

### Negative values
- Detects any negative values in land column
- Prints number of negative land areas

### Duplicates
- Detects any duplicate records in data set
- prints number of duplicates

## Example
![screenshot of terminal showing Data Summary Report(missing values, negatives and duplicates)](/assets/example.png)

## How to use
```bash
pip3 install python3 pandas
cd Data-Integrity-Audit
```