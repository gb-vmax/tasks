I'm a machine learning engineer preparing a dataset for model training and I need to quickly profile my training data before feeding it into the pipeline. I have a CSV file at `/home/user/ml_project/training_data.csv` that contains labeled samples with numeric features.

The CSV has no header row. Each line has exactly 4 comma-separated values in this order:
- Column 1: `sample_id` (integer)
- Column 2: `feature1` (float)
- Column 3: `feature2` (float)
- Column 4: `label` (string, one of: "cat", "dog", "bird")

I need you to compute a per-class summary and write it to `/home/user/ml_project/class_stats.txt`.

**The output file must have exactly this format:**

```
=== CLASS DISTRIBUTION REPORT ===

bird: 4 samples (26.67%), feature1 range [0.50, 3.20], feature2 range [1.10, 4.80]
cat: 6 samples (40.00%), feature1 range [1.20, 5.60], feature2 range [0.30, 3.90]
dog: 5 samples (33.33%), feature1 range [0.80, 4.40], feature2 range [1.50, 6.20]

Total samples: 15
```

(The numbers above are just illustrative — use the actual values from the file.)

Formatting rules:
- Classes must appear in **alphabetical order**, one per line.
- The percentage is `(class_count / total_count) * 100`, formatted to **2 decimal places**.
- The `feature1 range` and `feature2 range` values are the **min** and **max** of that feature for that class, formatted to **2 decimal places**.
- There is a blank line between the header and the first class line, and a blank line between the last class line and the "Total samples" line.
- The header is exactly `=== CLASS DISTRIBUTION REPORT ===`.
- The total samples line is exactly `Total samples: <N>` where `<N>` is the integer count.

Please compute this from `/home/user/ml_project/training_data.csv` and write the result to `/home/user/ml_project/class_stats.txt`.
</think>
