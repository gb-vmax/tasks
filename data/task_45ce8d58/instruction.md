Hey, I need some help organizing my data pipeline workspace. I have several CSV data files scattered across subdirectories under `/home/user/data/`, and I want to set up a clean working directory at `/home/user/workspace/` where I can access all the relevant files through symbolic links — without copying any data.

Here's what I need you to do:

**1. Create the workspace directory**

Create the directory `/home/user/workspace/` if it doesn't exist already.

**2. Create symbolic links for the data files**

Inside `/home/user/workspace/`, create symbolic links pointing to the following source CSV files. Use the exact link names specified:

- Link name `sales_q1.csv` → points to `/home/user/data/quarterly/q1_sales_data.csv`
- Link name `sales_q2.csv` → points to `/home/user/data/quarterly/q2_sales_data.csv`
- Link name `customers.csv` → points to `/home/user/data/customers/master_customers.csv`

All symlinks should use **absolute paths** as their targets (not relative paths).

**3. Create a manifest file**

Create a plain text file at `/home/user/workspace/manifest.txt` that documents each symlink. Each line should follow this exact format:

```
<link_name> -> <target_path>
```

The file should contain exactly 3 lines, one per symlink, listed in this order:
1. `sales_q1.csv`
2. `sales_q2.csv`
3. `customers.csv`

For example, the first line should look exactly like:
```
sales_q1.csv -> /home/user/data/quarterly/q1_sales_data.csv
```

No blank lines, no extra spaces, no header — just the 3 lines.

The symlinks themselves must be functional (i.e., readable, pointing to real files that exist), and the manifest must reflect the correct absolute target paths. Please make sure the link names in the workspace directory are exactly as specified above.
