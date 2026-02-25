You are a data analyst working with three CSV files containing sales data from different regions. Your goal is to process these files, extract insights, and present the results in both CSV and JSON formats for further analysis.

Here's the detailed task:

1. In the directory <code>/home/user/sales_data/</code>, there are three CSV files: <code>north.csv</code>, <code>south.csv</code>, and <code>west.csv</code>.
   - Each CSV file has the same columns, in this order: <code>OrderID</code>, <code>Product</code>, <code>Region</code>, <code>Salesperson</code>, <code>Quantity</code>, <code>SaleAmount</code>.
   - The values in the columns are comma-delimited, the first row is the header. All values are properly quoted if necessary.

2. You need to perform the following multi-step data processing:
   a. For each CSV file, calculate:
      i. The total number of orders (count the number of rows excluding the header).
      ii. The total <code>SaleAmount</code> (sum).
      iii. The average <code>SaleAmount</code> (mean, rounded to 2 decimal places).
   b. The results for all regions must be collected in a summary CSV file named <code>/home/user/sales_data/summary.csv</code> with the following columns in order:
      <blockquote>
      Region,TotalOrders,TotalSaleAmount,AverageSaleAmount
      </blockquote>
      Each row should correspond to a region (North, South, West), using the proper region name capitalization as found in the "Region" field in the originals.
   c. At the same time, create a JSON file <code>/home/user/sales_data/summary.json</code> containing an array of objects, one for each region, with keys matching the header fields from <code>summary.csv</code> (<code>Region</code>, <code>TotalOrders</code>, <code>TotalSaleAmount</code>, <code>AverageSaleAmount</code>). All numeric values should be numbers, not strings, and <code>AverageSaleAmount</code> should be a floating point value rounded to exactly two decimal places.

3. Save both files in <code>/home/user/sales_data/</code>.

4. Output a summary log at <code>/home/user/sales_data/process.log</code> listing, for each file processed, the filename, region, total orders, total sale amount, and average sale amount, formatted as follows (one entry per line):
   <blockquote>
   [FILENAME] | Region: [Region] | TotalOrders: [TotalOrders] | TotalSaleAmount: [TotalSaleAmount] | AverageSaleAmount: [AverageSaleAmount]
   </blockquote>
   Replace placeholders with actual values.

Please ensure the output files are in the exact format described above, as automated checks will verify column names, value formatting, and file paths.
