 Task 28
1. Project Overview-
- An end-to-end Customer Repeat Purchase & Retention Analysis built in Python using the Online Retail II dataset (online_retail_II.csv).
-  Prepared for senior leadership and data analytics assessment, this project evaluates core customer loyalty metrics, Average Order Value (AOV) progression, and multi-tier revenue distribution to inform data-driven retention strategies.

2. Key Features-
- Retention & Loyalty Metrics: Computes enterprise-level customer retention indicators, revealing a 65.58% Repeat Purchase Rate (2,845 repeat customers out of 4,338 total unique buyers).
- Order Progression & AOV Analysis: Evaluates spending growth across purchase sequences, demonstrating a 16.9% increase in Average Order Value (AOV) for repeat transactions (£497.74) compared to initial orders (£425.66).
- Multi-Tier Customer Segmentation: Groups buyers into four distinct behavioral tiers (One-Time Buyers, Returning, Frequent, and Loyal) to highlight revenue concentration, showing that Loyal Customers (6+ orders) account for 66.27% (£5.9M+) of total sales.
- Automated Data Processing Pipeline: Features clean Python scripts using pandas and numpy to automatically handle missing customer records, exclude cancelled transactions ('C' invoices), compute transaction totals, and dynamically rank chronological order sequences per buyer.

3. Repository Contents-
- customer_repeat_analysis.py: Main executable Python script containing the data cleaning pipeline, order sequence ranking logic, metric aggregations, and segment table generation.
- Customer_Repeat_Purchase_Report.pdf: Executive single-page summary report outlining core findings, customer tier distributions, strategic recommendations, and interview task answers.

4. How to View & Run
- Download customer_repeat_analysis.py and online_retail_II.csv into your local project directory.
- Open your terminal or Python environment (Jupyter Notebook / VS Code) and ensure pandas and numpy are installed (pip install pandas numpy).
- Run the script:Bashpython customer_repeat_analysis.py
-----------------------------------------------------------------------------------------------------------------
1. Project Overview TASK 26
- An interactive, single-page executive management dashboard built in Microsoft Power BI using the Sample - Superstore dataset. Designed for senior leadership, this report consolidates high-level revenue metrics, profitability analysis, product category distributions, and seasonal sales trends into a streamlined, clutter-free visualization canvas.

2. Key Features
- Executive Summary KPIs: Features high-visibility callout cards displaying core enterprise metrics including Total Sales (₹2.30M), Total Net Profit (₹286.40K), and Total Units Sold (37.87K).
- Product Mix & Margin Breakdown: Incorporates a central donut chart analyzing category revenue share (Technology, Furniture, Office Supplies) alongside a horizontal bar chart tracking profitability across detailed sub-categories.
- Temporal & Geographic Analytics: Utilizes a monthly time-series line chart to map sales momentum and seasonality (Jan–Dec), paired with a regional column chart comparing sales volume across Central, East, South, and West territories.
- Dynamic Slicing & Interactive Filtering: Integrates single-click interactive tile slicers for Region and Category, enabling leadership to perform real-time cross-filtering across all visual elements without navigating off the main canvas.

3. Repository Contents
- Sample_Superstore_Executive_Dashboard.pbix: Interactive Microsoft Power BI Desktop file containing the data model, DAX measures, visual layouts, and dynamic slicers.
- Executive_KPI_Dashboard_Report.pdf: Single-page exported PDF version of the final executive dashboard for quick viewing and distribution.
- KPI_Definitions_and_Documentation.md: Detailed documentation outlining measure formulas, business logic definitions, and data visualization best practices applied in the report.
- Sample - Superstore.xlsx: Raw underlying transactional dataset containing order records, customer segments, regional tags, and financial metrics.

4. How to View
- Download Sample_Superstore_Executive_Dashboard.pbix and Sample - Superstore.xlsx into your local directory.
- Open Sample_Superstore_Executive_Dashboard.pbix using Microsoft Power BI Desktop.
- Ensure the data source path links to Sample - Superstore.xlsx, then interact with the Region and Category slicers to explore dynamic cross-filtering across all visual cards and charts.
------------------------------------------------------------------------------------------------------------------------------------
Project Overview: Customer Cohort Retention Analysis
- An automated Python data analysis and visualization script designed to evaluate e-commerce customer transaction history, perform monthly cohort retention grouping, quantify repeat purchasing loyalty over time.

1. Project Overview
- An automated Python data analysis and visualization script designed to evaluate e-commerce customer transaction history, perform monthly cohort retention grouping, quantify repeat purchasing loyalty over time, and output an annotated heatmap.
  
2. Key Features
- Data Cleaning & Filtering: Cleans the raw transaction dataset by removing missing Customer IDs, filtering out non-positive unit prices and quantities, and excluding cancelled invoices.
- Monthly Cohort Grouping: Identifies each customer's first purchase month and calculates monthly elapsed time indexes relative to sign-up.
- Retention Rate Quantification: Builds a percentage-based matrix tracking customer retention behavior across 12-month transaction windows relative to initial sign-up size.
-  Visual Heatmap: Generates an annotated matrix heatmap using native Matplotlib (imshow and dynamic text contrast) and prints tabular retention matrices directly to the Spyder IPython console.
  
3. Repository Contents-
- cohort_analysis.py: Automated Python script containing data cleaning routines, cohort index math, retention matrix calculations, and Matplotlib visualization code.
- online_retail_II.csv: Raw input CSV dataset containing transactional records (Invoice, StockCode, Description, Quantity, InvoiceDate, Price, Customer ID, Country).
- retention_matrix.csv: Exported summary table displaying exact monthly customer retention percentages per cohort.cohort_heatmap.png: Rendered heatmap image displaying customer retention trends across time periods.

4. How to View
- Download the repository files (cohort_analysis.py and online_retail_II.csv) to your local project folder.
- Open cohort_analysis.py in your preferred Python IDE (Spyder, VS Code, or Jupyter).Execute the script via terminal or press F5 in Spyder to display the annotated retention heatmap and terminal matrix output.
-----------------------------------------------------------------------------------------------------------------------------------------
1. Project Overview TASK 24
- An automated Python data audit and quality validation script designed to evaluate multi-sheet relational databases, execute custom business validation rules, quantify data hygiene anomalies, and export cleaned dataset samples for downstream analytics.
  
2. Key Features
- Multi-Sheet Inspection: Loads and scans multiple relational entity tables (Customers, Products, Stores, and Transactions) using Pandas to perform global null checks and full-row duplicate detection.
- Relational & Temporal Validation: Enforces primary key uniqueness and cross-table date sequence logic (Transaction Date >= Customer Join Date) to detect temporal inconsistencies.
-  Domain & Range Verification: Validates product pricing logic and cost bounds (UnitPrice > 0, CostPrice > 0, and UnitPrice >= CostPrice) to ensure financial reporting accuracy.
-  Dynamic Reporting & Issue Logging: Calculates audit metrics live from the dataset to output an executive summary report, a structured issue log, and a clean 100-row sample directly to the IPython console.

3. Repository Contents- data_quality_audit.py: Automated Python audit script containing the multi-sheet validation engine, metric calculators, and terminal reporting logic.
- Retail_sales_dataset.xlsx: Raw input Excel workbook containing four relational sheets (Customers, Products, Stores, Transactions).
- issue_log.csv: Generated issue log detailing affected dataset tables, rule descriptions, error severity levels, record counts, and impacted sample IDs.       cleaned_sample.csv: Filtered 100-row transaction dataset free from temporal logic violations, ready for downstream modeling.
  
4. How to View
- Download the repository files (data_quality_audit.py and retail_sales_dataset.xlsx) to your local project folder.
- Open data_quality_audit.py in your preferred Python IDE (Spyder, VS Code, or Jupyter).
- Execute the script via terminal or press F5 in Spyder to display the dynamic Audit Report, Issue Log, and Cleaned Sample outputs.
--------------------------------------------------------------------------------------------------
1. Project Overview TASK 23-

- An advanced SQL Data Query Language (DQL) analysis script designed to execute window functions, perform row-level ranking, evaluate lead/lag trend metrics, and calculate rolling window aggregations on the Northwind dataset (mytable).
  
2. Key Features-Row-Level Ranking:
- Assigns deterministic sequence values and dense rank tiers across line items using ROW_NUMBER(), RANK(), and DENSE_RANK().
- Positional & Trend Navigation: Computes consecutive line-item price variations and order-over-order revenue metrics using LAG() and LEAD().
-  Cumulative & Moving Aggregations: Calculates running order totals and 3-item moving price averages using custom frame specifications (ROWS BETWEEN).
  
3. Repository Contents-task23_queries.pdf:
- SQL script containing the 12 executed window function query set for database analysis.
- data.csv: Raw input dataset (mytable) containing order details (order_id, product_id, unit_price, quantity, discount).
  
4. How to View-
- Download the repository files to your local system.
- Execute the script via terminal or command prompt
----------------------------------------------------------------------------------------------------
1. Project Overview TASK 21-
- A basic Data Query Language (DQL) analysis script designed to execute targeted SQL queries, apply conditional filtering, and sort transaction metrics on the Northwind dataset.
  
2. Key Features-
- Conditional Data Filtering: Restricts transaction rows using specific thresholds for pricing, quantities, and discount rates.
- Data Sorting & Limiting: Orders records systematically while limiting outputs to ensure concise, single-screen readable results.
- Query Flexibility: Performs targeted lookups by specific order IDs, price ranges, and promotional tiers.
  
3. Repository Contents-
- task21_queries.pdf: SQL script containing the executed query set for database analysis.
- data.csv: Raw input dataset containing order details (order_id, product_id, unit_price, quantity, discount).

4. How to View-
- Download the repository files to your local system.
- Execute the script via terminal or command prompt: "task21_queries.sql".
---------------------------------------------------------------------------------------------------------
1. Project Overview TASK 1-
- A basic data cleaning and preprocessing script designed to identify missing values, handle null entries, and prepare raw data for analysis.

3. Key Features-
- Missing Value Handling: Automated imputation of missing values in Age (mean) and Embarked (mode), and filling missing Cabin entries with 'Unknown'.
- Data Standardization: Replaces missing data across features without dropping rows indiscriminately.
- Data Export: Processed output saved automatically as a clean Excel file ready for downstream analysis.

3. Repository Contents-
- Task no. 1.py: Python script using Pandas to read, clean, and save the dataset.
- Titanic .xlsx: Raw input dataset used for cleaning.
  
4. How to View-
- Download the repository files to your local system.
- Execute the script via terminal or command prompt:"Task no. 1.py".
-----------------------------------------------------------------------------------------------------------------------------
1. Project Overview
- A basic missing-data inspection script designed to identify missing values across dataset features and summarize where incomplete data occurs.

2. Key Features
- Missing Value Summary: Comprehensive analysis displaying missing value counts and percentage proportions across all 12 columns.
- Inspection & Profiling: Automated detection of null patterns with Pandas display options configured to prevent column truncation (...).
- Impact Analysis: Evaluation of data completeness to prevent risky operations like ungrounded row deletion.

 3. Repository Contents
- Task no. 12.py:
  Python script utilizing Pandas to process local data files and display complete missing value metrics across all features.
- Titanic .xlsx.xlsx: Raw dataset used for analysis.

 4. How to view
- Download the repository files to your local system.
- Ensure required libraries are installed (pip install pandas openpyxl).
- Execute the script via terminal or command prompt: python "Task no. 12.py".
--------------------------------------------------------------------------------------------------------------------------------------
Basic Data Sorting & Filtering - TASK 11

​1. Project Overview
- A foundational data analysis task focused on sorting and filtering structured business datasets to answer key operational questions.
  
​2. Key Features
​- Data Preservation: Raw dataset kept unchanged in a dedicated sheet.  
​- Multi-Criteria Filtering: Applied combined logic rules across regions, discounts, and profitability metrics.  
​- Dynamic Sorting: Single and multi-column alphanumeric and numerical ordering.  

​3. Repository Contents
​-  Filtered workbook containing Raw Data and Analysis sheets.  
​- Documented answers to the 5 business queries and interview questions. 

​4. How to View
​- Download the workbook from this repository.  
​- Open in Excel or Google Sheets to inspect the active filters and worksheet structure.

----------------------------------------------------------------------------------------------
Simple KPI Tracking Sheet - TASK 10
1. Project Overview
- An automated, single-tab summary dashboard designed to translate raw transactional order data into real-time operational metrics.
2. Key Features
- Dynamic KPI Summary: Instant snapshot of Total Revenue, Total Units Sold, Average Order Value (AOV), and Total Orders.
- Auto-Updating Calculations: Formulas automatically recalculate as new transaction rows are added.
- Data Integrity: Standardized currency and numeric formatting with full-column range references.
3. Repository Contents
- TASK 10- Dynamic Excel KPI dashboard file.
- Sample-Superstore transactional dataset used for analysis.
- Dashboard preview.png: Visual layout preview.
4. How to View
- Download the file from this repository.
- Open in Microsoft Excel or Google Sheets to view or add data to the Raw Data tab.
 
 -------------------------------------------------------------------------------------------------------------------
 Data Analysis & Summary Statistics - TASK 9
1. Project Overview
- An end-to-end Python exploratory data analysis script utilizing Pandas to extract, compute, and format key descriptive statistical measures from the Titanic dataset.

2. Key Features
- Targeted Metric Selection: Focuses on core numerical variables (Age, Fare, SibSp) to analyze distinct distribution patterns across continuous, skewed, and discrete counts.
- Individual Parameter Extraction: Calculates measures of central tendency (mean, median, mode) and dispersion (standard deviation, interquartile ranges) independently.
- Structured Matrix Assembly: Combines distinct statistical series into a clean, unified DataFrame output for structured evaluation.
- Precision Formatting: Formats numeric outputs to two decimal places to ensure visual clarity and immediate table scannability.

3. CENTRAL TENDENCY ANALYSIS
- Averaging & Middle Values: Computes mean and median values across selected attributes to evaluate baseline distribution centerpoints.
- Skewness Detection: Contrasts mean against median values (notably in Fare) to identify right-skewed distributions caused by high-value outliers.

4. DISPERSION & SPREAD MODELING
- Variability Metrics: Calculates standard deviations to measure variance and distribution spread around average values.
- Quantile Segmentation: Derives 25th and 75th percentiles to define the Interquartile Range (IQR) for boundary analysis.

5. Repository Contents
- Primary Python script (task_9_analysis.py) containing data loading logic, metric computations, table aggregation, and output formatting.
- Reference dataset (Titanic-Dataset.csv).

6. How to View
- Download task_9_analysis.py and Titanic-Dataset.csv into the same execution directory.
- Run python task_9_analysis.py in your terminal or IDE environment.
- Review the formatted summary output matrix directly in the console output.
---------------------------------------------------------------------------------------------------
Dynamic Sales Tracker - TASK 8

1. Project Overview
- A multi-tab automated sales tracking system in Google Sheets created to process, validate, and summarize 5,000 raw transaction records into daily, weekly, and monthly performance totals.

2. Key Features

- Dynamic Summary Rollups: Automated tracking of Daily, Weekly, and Monthly revenue using SUMIF and SUMIFS formulas.

- Data Validation & Error Prevention: Restrictive cell rules for dates, dynamic product lookup dropdowns, and protected summary formulas.

- Dynamic Pricing & Revenue Calculation: Multi-condition nested formulas using VLOOKUP to auto-calculate gross revenue net of variable discounts.

- Modular Workbook Architecture: Clean relational tab structure separating core transactional data from master dimension entities.

3. Workbook Architecture & File Contents

- TASK 8- SALES TRACKER workbook with automated rollups.

- Summary Tab: High-level automated rollup cards and date-filtered revenue metrics.

- Transactions Tab: Core transactional dataset featuring input validation and dynamic price lookup.

- Reference Tabs: Products, Customers, and Stores lookup tables.

4. How to View

- Open the workbook in Google Sheets or Microsoft Excel.

- Navigate to the Transactions tab to interact with dropdown validation rules or view formula logic.

- Switch to the Summary tab to inspect calculated aggregate metrics and revenue breakdowns.

-----------------------------------------------------------------------------------------------
 Data Visualization & Storytelling - TASK 7
 
​ 1. Project Overview

​- An end-to-end data visualization and storytelling module utilizing Google Sheets to build interactive,
labeled visual chart models from the World Happiness Report dataset.

​2. Key Features

​- Visual Structure Selection: Strategic chart selection matching core analytical query types (Composition, Comparison, and Trend/Relationship).

​- Clean Composition Limits: Grouped low-frequency categories into an "Others" slice to respect the 5-slice visual rule.

​- Sorted Categorical Rankings: Descending horizontal bar charts to maintain clean text readability for long geographic labels.

​- Continuous Trend Modeling: Pre-sorted X-axis indexing to convert raw scatter points into clear continuous trendlines.

​3. COMPOSITION ANALYSIS (PIE CHART)

​- Regional Happiness Share: Aggregates global cumulative happiness scores into a top-4 regional breakdown plus consolidated remaining regions.

​- Slice Optimization: Restricts total slices to under 5 for visual clarity and percentage readability.

​4. CATEGORICAL COMPARISON (HORIZONTAL BAR CHART)

​- Regional Average Rankings: Compares average happiness scores across geographic regions in descending order.

​- Label Readability: Uses horizontal orientation and explicit data labels to eliminate text overlap on region titles.

​- TREND & RELATIONSHIP MODELING (SORTED LINE CHART)

​- GDP per Capita vs. Happiness: Plots nation happiness against economic output tiers to evaluate direct correlation.

​- Trendline Integration: Integrates a linear trendline on pre-sorted data to prove continuous upward scaling from lower to higher GDP brackets.

​5. Repository Contents

​- Primary Google Sheets workbook containing source dataset (2015.csv), functional calculation tabs (Pivot Tables), and visual dashboards.

​6. How to View

​- Open the provided Google Sheets link or download TASK 7.xlsx from this repository.

​- Navigate to the Pivot Tables sheet to view data aggregations.

​- Review the TASK 7 SUBMISSION tab for labeled charts, one-line takeaways, and the executive data narrative.

---------------------------------------------------------------------------------------------------------------
Excel Formulas and Functions - TASK 6
1. Project Overview
- An end-to-end Excel analysis module utilizing lookup, logical, mathematical, and text functions to clean, extract, and aggregate data from the Superstore dataset.

2. Key Features
- Advanced Lookups: Dynamic product retrieval and missing ID handling using lookup methods.
- Conditional Logic Rules: Order tiering and shipping priority assignment built using multi-level logic rules.
- Multi-Criteria Aggregation: Segmented revenue totals and conditional order counts based on dynamic criteria filters.
- Text Parsing & Cleaning: String extraction, location merging, extra space removal, and case standardization.

3. Functional Breakdown
- LOOKUPS
- VLOOKUP (Fetch Product Name using Product ID): Searches catalog columns to return exact matching product titles.
- XLOOKUP (Fetch Product Name / handling missing IDs): Performs bidirectional product lookups with built-in missing value handling.
- LOGICAL FUNCTIONS
- High/Medium/Low Sales Classifier: Groups transaction sales into custom value tiers based on revenue thresholds.
- Shipping Priority & Handling Fee Rules: Assigns fulfillment priority levels based on shipping class and item quantities.
- MATH & AGGREGATION
- Total Sales in Technology in the South Region: Aggregates technology category sales specifically within the South region.
- Overall Count of orders with Sales > $500 in the West Region: Filters and counts high-value transactions in the West region.
- TEXT FUNCTIONS
- Extracting Category Prefix: Extracts starting department characters from Product IDs.
- Isolating Sub-Category Code: Isolates sub-category identifiers from middle string positions.
- Extracting Product Sequence Number: Retrieves trailing unique sequence digits.
- Combining City and State into Full Location: Joins city and state attributes with proper delimiter formatting.
- Cleaning Unwanted Spaces in Customer Names: Strips leading, trailing, and irregular middle spaces from customer names.
- Standardizing Text to Uppercase: Converts product descriptions into standard uppercase text format.

4. Repository Contents
- Primary Excel workbook containing source datasets (Original data - Orders, Original Data - Returns), the functional calculations tab (TASK 6 SUBMISSION), and the conceptual guide (NOTES).

6. How to View
- Download TASK 6.xlsx from this repository.
- Open the workbook in Microsoft Excel or Google Sheets.
- Navigate to the TASK 6 SUBMISSION sheet to view calculated outputs.
- Review the NOTES sheet for function guidelines, best practices, and key advantages.

-------------------------------------------------------------------------------------------
Excel Data Analysis Report - TASK 5

- Project Overview
An in-depth Excel data analysis model designed to calculate key financial metrics, process returns, and structure pivot table summaries across products, regions, and sales trends.

- Key Features
Dynamic Metrics: Instant calculation of Total Revenue, Total Order Volume, and Average Consumer Order Value using Excel formulas.
Advanced Querying: Filtered logic for high-value regional orders and categorical average profits.

- Structured Summaries:
Pivot Table: Sales distribution by Product Category.
             Regional sales comparison and percentage contributions.
             Monthly sales trends and seasonal performance.
             Top sub-category profitability tracking.

- Repository Contents
TASK 5 .xlsx: Complete Excel workbook containing raw order data, calculated working sheets, returns tracking, and summary pivot tables.

- How to View
Open the file in Microsoft Excel or any standard spreadsheet application to inspect the formulas, working data, and summary tables.
---------------------------------------------------------------------------------------------------------


1. Data Visualisation and Story-Telling - TASK 4
- Project Overview
- An end-to-end data visualization project using Excel, Power BI, and PowerPoint to analyze trends and present insights.

2. Key Features

- Data Prep: Cleaned data, structured transformations, and lookup tables in Excel.
- Interactive Dashboard: Dynamic filtering, category breakdowns, and trend charts in Power BI.

3. Visual Breakdown:

- Bar Chart: Segment performance and categorical comparisons.
- Line Chart: Metric movements and performance trends over time.
- Slide Deck: Visual narrative translating data into actionable findings in PowerPoint.

4. Repository Contents

- TASK 4- VISUALIZATIONS.xlsx: Raw dataset and cleaned analysis file.
- Final presentation slide deck with visuals created in Power BI.

==================================================================================
- Simple Sales Dashboard - TASK 3
1. Project Overview
An interactive sales performance dashboard designed to analyze key metrics across products, regions, and monthly 
timeframes.

2. Key Features
- KPI Summary:Instant snapshot of Total Sales, Units Sold, and Profit Margins.
- Interactive Slicers: Dynamic filtering by Region and Month.

- Visual Breakdown:
  - Bar Chart: Sales performance by Product Category.
  - Line Chart: Monthly revenue trends over time.
  - Column Chart: Geographical sales comparison (by Region).

3. Repository Contents
- TASK 3- POWERBI DASHBOARD.pbix: Interactive Power BI dashboard file.
- Sample-Superstore.xlsx: Raw dataset used for analysis.
- Dashboard preview.png: Visual layout preview.

4. How to View
- Download the .pbix file from this repository.
- Open in Power BI Desktop to interact with the slicers and visuals.
