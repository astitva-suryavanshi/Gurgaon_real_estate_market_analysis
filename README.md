# Gurgaon_real_estate_market_analysis
This project focuses on performing end-to-end data analysis on a real estate dataset to uncover key insights about property pricing, locality trends, and housing characteristics. The dataset was cleaned and transformed using Pandas, followed by exploratory analysis and visualization using Matplotlib and Seaborn. 

📌 Overview

This project performs end-to-end data analysis on a real estate dataset to extract meaningful insights about property prices, localities, and housing trends. The goal is to understand factors influencing property pricing and support data-driven decision-making.

🛠️ Tech Stack

Python
Pandas → Data cleaning & manipulation
Matplotlib & Seaborn → Data visualization

🧹 Data Cleaning
Standardized column names (lowercase, removed spaces)
Removed duplicate records
Converted numeric columns (price, area, rate_per_sqft) into proper formats
Cleaned categorical columns (status, flat_type, rera_approval)
Converted RERA approval into boolean values (True/False)

🔍 Key Analysis Performed
1. Costliest Property
Identified the most expensive flat in the dataset
2. Locality Insights
Found locality with highest average price
Found locality with highest rate per square foot
3. Property Status Comparison
Compared ready-to-move vs under-construction properties
4. RERA Approval Impact
Analyzed whether RERA-approved properties have a price advantage
5. Area vs Price Relationship
Visualized how property area affects overall price
6. BHK Analysis
Identified most expensive BHK configuration
7. Property Type Comparison
Compared Apartment, Floor, Plot pricing trends
8. Builder Analysis
Identified top builders with highest pricing
9. Area vs Rate per Sqft
Checked whether larger homes cost more per square foot

📊 Visualizations
Scatter plot: Area vs Price
Scatter plot: Area vs Rate per Sqft

📈 Key Insights
Premium localities significantly influence property pricing
Ready-to-move properties often have higher prices due to immediate availability
Larger homes do not always have higher price per square foot
Certain builders consistently price their properties higher
Property type plays a major role in pricing differences
