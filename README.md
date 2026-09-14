 Data Visualization & Storytelling - TASK 7
​1. Project Overview
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
