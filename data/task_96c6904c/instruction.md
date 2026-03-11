I'm preparing a dataset for a binary classification model and need help cleaning and transforming a raw CSV file into a format my training pipeline expects.

The raw data file is at `/home/user/data/raw_samples.csv`. It has the following columns (with a header row):

```
sample_id,feature_a,feature_b,feature_c,label,split
```

I need you to produce a cleaned file at `/home/user/data/train_ready.csv` by doing the following transformations using `awk` and/or `sed`:

**Step 1 — Filter to training rows only:**
Keep only rows where the `split` column equals `train`. Drop the header row and all non-train rows entirely.

**Step 2 — Reformat and select columns:**
From the filtered rows, output only these columns in this exact order:
```
sample_id,feature_a,feature_b,feature_c,label
```
(Drop the `split` column.)

**Step 3 — Normalize the label column:**
The raw `label` column contains the strings `positive` and `negative`. Replace them with `1` and `0` respectively.

**Step 4 — Add a new header:**
The output file must begin with this exact header line:
```
id,feat_a,feat_b,feat_c,target
```
Note the column names are different from the original — `sample_id` becomes `id`, `feature_a` becomes `feat_a`, etc., and `label` becomes `target`.

The final file `/home/user/data/train_ready.csv` should contain the header line followed by the transformed training rows, one per line, with no trailing whitespace and no blank lines.

**Example:** if the raw file had a row `S003,0.55,1.20,0.88,positive,train`, the corresponding output row would be `S003,0.55,1.20,0.88,1`.
