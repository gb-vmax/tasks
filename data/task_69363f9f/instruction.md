I'm an integration developer working on a data pipeline that consumes outputs from three different internal APIs. Each API dumps its response data as a tab-separated file, but the columns are in different orders across the three files. I need to normalize, recombine, and validate the data before it goes into our unified data store.

Here's the situation: I have three source files in `/home/user/api_data/`:

- `users.tsv` — user records from the User API
- `scores.tsv` — engagement scores from the Analytics API
- `regions.tsv` — geographic region data from the Location API

My goal is to produce two output files in `/home/user/api_data/output/`:

1. **`normalized_users.tsv`** — a cleaned and reordered extract from `users.tsv`
2. **`combined_report.tsv`** — a merged file combining columns from all three source files

Here are the exact requirements:

---

### Step 1: Produce `normalized_users.tsv`

The `users.tsv` file has columns in this order:
```
created_at  user_id  email  full_name  status  department
```
(columns 1–6, tab-separated)

I need `normalized_users.tsv` to contain ONLY the following columns, in this exact new order:
```
user_id  full_name  email  department  status
```
That is: column 2, then column 4, then column 3, then column 6, then column 5 from the original file.

The output file must include the header line first, then all data rows in the same row order as the original. No trailing whitespace on any line. The delimiter must remain a tab character.

---

### Step 2: Produce `combined_report.tsv`

The three source files all have the same number of rows (including a header row), and the rows correspond to the same users in the same order across all files.

- `users.tsv` columns: `created_at  user_id  email  full_name  status  department`
- `scores.tsv` columns: `user_id  login_count  engagement_score  last_active`
- `regions.tsv` columns: `user_id  country  city  timezone`

I need `combined_report.tsv` to contain the following columns in this exact order:
```
user_id  full_name  email  engagement_score  login_count  country  city  status
```

That means:
- `user_id` → column 2 of `users.tsv`
- `full_name` → column 4 of `users.tsv`
- `email` → column 3 of `users.tsv`
- `engagement_score` → column 3 of `scores.tsv`
- `login_count` → column 2 of `scores.tsv`
- `country` → column 2 of `regions.tsv`
- `city` → column 3 of `regions.tsv`
- `status` → column 5 of `users.tsv`

The output must include the header row as the first line, then all data rows in the original row order. All fields are tab-separated. No trailing whitespace.

---

Please create the `/home/user/api_data/output/` directory if it doesn't exist, then produce both output files. I need the exact column order and tab separation to match precisely, because an automated system will be parsing these files downstream.
