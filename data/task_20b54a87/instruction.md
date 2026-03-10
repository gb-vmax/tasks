Hey, I need your help updating some configuration files for my ML experiment tracking setup. I've been running a training job and the results are in — I need to update the experiment config and artifact registry files to reflect the completed run before I hand this off to the deployment team.

I have two config files that need to be updated:

**1. `/home/user/mlops/experiments/run_42.yaml`**

This file already exists and tracks the experiment metadata. I need you to make these changes:
- Change the `status` field (currently `"running"`) to `"completed"`
- Set the `metrics.val_accuracy` field (currently `null`) to `0.9173`
- Set the `metrics.val_loss` field (currently `null`) to `0.2041`
- Add a new field `artifact_path` at the top level (same level as `status`, `model`, `metrics`) with the value `"s3://mlops-bucket/run_42/model.pkl"`

**2. `/home/user/mlops/artifacts/registry.toml`**

This file already exists with a list of registered models. I need you to append a new entry to it. The file uses TOML array-of-tables format with `[[models]]` sections. Add a new `[[models]]` entry at the end of the file with these fields (in this order):
- `run_id` = `42` (integer)
- `name` = `"gradient_boost_v3"` (string)
- `status` = `"staged"` (string)
- `val_accuracy` = `0.9173` (float)
- `artifact_path` = `"s3://mlops-bucket/run_42/model.pkl"` (string)

After your changes, the final content of `/home/user/mlops/experiments/run_42.yaml` should be a valid YAML file, and `/home/user/mlops/artifacts/registry.toml` should be a valid TOML file. Please make the minimal edits necessary — don't reformat or reorder anything that doesn't need to change in either file.
