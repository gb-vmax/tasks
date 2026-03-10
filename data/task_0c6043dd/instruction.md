Hey, I have a CSV file at `/home/user/data/sales.csv` that contains daily sales records. I need to quickly benchmark which product categories are performing best by computing the total revenue per category. Can you help me process this file and write a summary?

The CSV file has the following columns (with a header row):
```
date,category,product,units_sold,unit_price
```

I need you to calculate the **total revenue** for each category, where revenue for each row is `units_sold * unit_price`. Then write the results to `/home/user/data/category_revenue.txt`.

The output file must have exactly this format — one line per category, sorted alphabetically by category name:

```
<category>: <total_revenue>
```

Where `<total_revenue>` is an integer (no decimal point, no dollar sign). For example:
```
Electronics: 45200
Furniture: 12800
```

The file should contain only the category lines — no header, no blank lines, no trailing whitespace.
