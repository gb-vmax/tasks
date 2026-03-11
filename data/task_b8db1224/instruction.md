Hey, I need your help processing some experiment tracking logs from our ML training runs. I have a tab-separated log file at `/home/user/mlops/experiments.tsv` that records metadata about training experiments. Each line has these fields (tab-separated):

```
experiment_id   model_name   status   accuracy   checkpoint_path
```

Example rows look like:
```
exp_001   resnet50   COMPLETED   0.9234   /mnt/storage/runs/exp_001/ckpt_final.pt
exp_002   bert_base   FAILED   0.0000   /mnt/storage/runs/exp_002/ckpt_epoch3.pt
```

I need you to produce a summary report at `/home/user/mlops/artifact_report.txt` that contains only the **COMPLETED** experiments, with the following transformations applied:

1. Filter to rows where the `status` field is exactly `COMPLETED`.
2. Convert the `accuracy` field from a decimal (e.g., `0.9234`) to a percentage string rounded to one decimal place (e.g., `92.3%`).
3. Extract just the **filename** from the `checkpoint_path` (everything after the last `/`), and strip the `.pt` extension from it.
4. Output each qualifying row in this exact format, one per line:
   ```
   <experiment_id> | <model_name> | <accuracy_percent> | <checkpoint_name>
   ```

For example, if `exp_001` with model `resnet50`, accuracy `0.9234`, and checkpoint `/mnt/storage/runs/exp_001/ckpt_final.pt` is COMPLETED, the output line should be:
```
exp_001 | resnet50 | 92.3% | ckpt_final
```

The output file should contain only the matching lines — no header, no blank lines, no trailing spaces. Lines should appear in the same order they appear in the input file.

Please process `/home/user/mlops/experiments.tsv` and write the result to `/home/user/mlops/artifact_report.txt`.
