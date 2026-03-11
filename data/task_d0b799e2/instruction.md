I'm a researcher trying to get a handle on my datasets directory before running some expensive preprocessing jobs. I want to audit what's taking up the most space, identify large files that should be compressed or archived, and produce a clean summary report I can share with my team. Can you help me analyze `/home/user/datasets` and generate a report?

Here's exactly what I need:

---

**Step 1: Scan the dataset structure**

The `/home/user/datasets` directory contains several subdirectories, each representing a separate dataset. Each subdirectory may contain files of various types (`.csv`, `.json`, `.bin`, `.log`, `.txt`). Scan all subdirectories (non-recursively — only one level deep inside each dataset directory).

---

**Step 2: Compute per-dataset statistics**

For each subdirectory inside `/home/user/datasets`, compute:
- Total size in bytes (sum of all file sizes in that directory)
- File count (number of files in that directory)
- The name of the largest single file in that directory

---

**Step 3: Identify large files**

Across the entire `/home/user/datasets` tree, find all individual files whose size is **strictly greater than 2000 bytes**. Collect their paths relative to `/home/user/datasets` (e.g., `genomics/reference.bin`), sizes in bytes, and sort them by size descending.

---

**Step 4: Generate the report**

Write the final report to `/home/user/datasets/audit_report.txt`. The report must follow this **exact format** (no extra blank lines, no trailing spaces, header and section titles exactly as shown):

```
=== DATASET AUDIT REPORT ===

DATASET SUMMARY (sorted by total size, descending):
  <dataset_name>: <total_bytes> bytes, <file_count> files, largest: <filename>
  <dataset_name>: <total_bytes> bytes, <file_count> files, largest: <filename>
  ...

TOTAL STORAGE USED: <grand_total_bytes> bytes across <total_file_count> files

LARGE FILES (>2000 bytes, sorted by size descending):
  <relative_path>: <size> bytes
  <relative_path>: <size> bytes
  ...

TOP DATASET: <name_of_dataset_with_most_bytes>
```

Rules:
- In the DATASET SUMMARY section, each dataset is listed on its own line with exactly two leading spaces.
- `<filename>` in "largest:" is just the bare filename, not the full path.
- The `TOTAL STORAGE USED` line counts all files across all datasets (do NOT include `audit_report.txt` itself in any counts or sizes).
- In the LARGE FILES section, each entry has exactly two leading spaces. `<relative_path>` uses forward slashes and is relative to `/home/user/datasets`.
- If no files exceed 2000 bytes, the LARGE FILES section should contain exactly one line: `  (none)`.
- `TOP DATASET` is the dataset directory with the single highest total byte count.
- The report file itself must be located at `/home/user/datasets/audit_report.txt` and must NOT appear in any statistics.

---

**Notes:**
- Do not recurse deeper than one level into each dataset directory.
- All size values are in bytes as reported by `stat` or equivalent (actual file size, not disk blocks).
- Datasets should be sorted strictly by total bytes descending in the summary. If two datasets have the same total size, sort them alphabetically by name.
- Large files should be sorted strictly by size descending. If two files have the same size, sort them by relative path alphabetically.
