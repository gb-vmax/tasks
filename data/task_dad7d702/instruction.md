I'm a researcher and I need help organizing and archiving some of my datasets. I have a directory at `/home/user/datasets/experiment_42` that contains various files from a recent experiment. I need to back up only the CSV data files from this directory into a compressed tar archive, and then generate a manifest listing what's inside.

Here's exactly what I need you to do:

1. Create a compressed tar archive (using gzip compression) at `/home/user/backups/experiment_42_data.tar.gz` that contains **only the `.csv` files** from `/home/user/datasets/experiment_42`. The files should be stored in the archive with their paths relative to `/home/user/datasets/experiment_42` (i.e., just the filenames, no leading directory path components like `home/user/datasets/experiment_42/` in the archive).

2. Generate a manifest file at `/home/user/backups/experiment_42_manifest.txt` that lists the contents of the archive. The manifest should be produced by running `tar -tzf` on the archive you just created, and the output written directly to that file. The manifest should list one filename per line, exactly as `tar -tzf` reports them.

The `/home/user/backups/` directory does not exist yet — you'll need to create it.

To be clear on what "relative paths" means here: if the archive contains `results_day1.csv`, the manifest should show `results_day1.csv`, not `/home/user/datasets/experiment_42/results_day1.csv` or `./results_day1.csv` or `experiment_42/results_day1.csv`.

Please make sure only `.csv` files end up in the archive — the experiment directory also contains some other files (notes, logs, etc.) that should NOT be included.
