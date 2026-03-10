I'm a data engineer and I need your help generating documentation for one of my ETL pipeline stages. I have a schema definition file at `/home/user/etl/schemas/orders_pipeline.csv` that describes each field in the pipeline's output table. I need you to transform this into a Markdown documentation file and then validate it.

Here's what I need done:

**Step 1: Inspect the schema CSV**

The file at `/home/user/etl/schemas/orders_pipeline.csv` contains information about each field in the `orders` ETL pipeline. Take a look at it to understand the structure before generating the docs.

**Step 2: Generate the Markdown documentation file**

Create a file at `/home/user/etl/docs/orders_pipeline.md` with the following exact content and structure:

```
# orders Pipeline Documentation

## Overview

Pipeline: orders  
Source: PostgreSQL  
Destination: BigQuery  
Owner: data-eng-team  

## Schema

| Field Name | Data Type | Nullable | Description |
|---|---|---|---|
```

After that header row and separator row, add one table row per field from the CSV, in the same order they appear in the CSV file. Each row must follow this exact format:

```
| <field_name> | <data_type> | <nullable> | <description> |
```

After the table, add a blank line followed by this exact footer section:

```
## Notes

- Schema version: 1.0
- Last updated: 2024-01-15
- Do not modify this file manually; it is generated from the schema CSV.
```

**Step 3: Count and verify the table rows**

Run a command to count the number of data rows in the Markdown table (excluding the header row and the separator row) and write the result as a single integer to `/home/user/etl/docs/row_count.txt`. For example, if there are 6 data rows in the table, the file should contain just:

```
6
```

**Step 4: Lint the Markdown file**

Check that every table row in the Markdown file is properly formatted — specifically, that every line that starts with `|` also ends with `|`. Write the result of this check to `/home/user/etl/docs/lint_result.txt`. If all pipe-delimited lines are correctly closed, the file should contain exactly:

```
LINT PASSED: all 8 table lines are properly closed
```

(where `8` is the total number of lines starting with `|`, i.e., the 2 header lines plus all data rows — adjust the number to match the actual count of `|`-starting lines in the file)

If any line starting with `|` does NOT end with `|`, write:

```
LINT FAILED: malformed table lines found
```

Please make sure the docs directory exists before writing any files.
</think>

The schema CSV at `/home/user/etl/schemas/orders_pipeline.csv` has the following columns: `field_name`, `data_type`, `nullable`, `description`. Make sure the Markdown table columns match those headers exactly as shown above.
