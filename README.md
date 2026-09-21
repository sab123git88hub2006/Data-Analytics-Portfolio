​1. Project Overview
​- A basic sales summary report designed to calculate core performance metrics and synthesize total sales revenue, average transaction size, and overall order volume using Microsoft Excel.

​2. Key Features
​- KPI Dashboarding: Built a dedicated SUMMARY SHEET tab displaying primary metrics: Total Sales (14,301,903.15), Average Sales per Transaction (2,860.38), and Total Transactions Count (5,000).  
​- Relational Sheet Formulas: Extracted unit pricing from the Products catalog into the Transactions log using VLOOKUP to accurately calculate net revenue after applying quantity and discounts.  
​- Manual Data Verification: Conducted status bar auditing and formula validation across 5,000 transaction rows to ensure 100% computational accuracy.  

​3. Repository Contents
​- Summary_Sheet.png: Screenshot showing the completed Excel KPI summary table and formatted numbers.  
​- Retail_sales_dataset.xlsx: Raw workbook containing Customers, Products, Stores, and Transactions sheets alongside the newly created Summary Sheet. 

​4. How to view
​- Download the retail_sales_dataset.xlsx file to your local computer.  
​- Open the file in Microsoft Excel.  
​- Navigate to the SUMMARY SHEET tab at the bottom to view the calculated KPIs and formulas

---------------------------------------------------------------------------------------------------------------------------------
TASK 13
1. Duplicate Record Check - Data Analytics Track

2. Description-
Find duplicate records across all tables in the dataset and document them.

3. Objective-
Understand duplicate detection across full rows and key columns.

4. Tools Used- MS Excel

5. Deliverables Summary-
- `Retail Sales Dataset Sample duplicate_report.csv`: A summary report documenting duplicate detection results across all 4 dataset sheets.
- `Retail_Sales_Data_Cleaned_Copy.xlsx`: Verified copy of the dataset containing no duplicate records.

6. Duplicate Detection Method & Results-
- Check Full Rows: Evaluated all 4 sheets (`Customers`, `Products`, `Stores`, `Transactions`) using Excel's Data -> Remove Duplicates feature.
- Identified 0 exact duplicate rows across all tables.
- Check Key Columns: Evaluated primary key columns (`CustomerID`, `ProductID`, `StoreID`, `TransactionID`) using Excel's Conditional Formatting -> Highlight Cells Rules -> Duplicate Values.
-  Identified 0 duplicate key values across all tables.
----------------------------------------------------------------------------------------------
TASK 12
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
