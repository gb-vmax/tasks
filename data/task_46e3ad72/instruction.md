You are an MLOps engineer who needs to back up a set of machine learning experiment artifacts for auditing and reproducibility. You have a working directory at <b>/home/user/ml_experiments/exp_42</b>, which contains the following (pre-existing) structure:

<ul>
<li><b>model/</b> (directory):</li>
  <ul>
    <li><b>model.h5</b> (binary model weights, 9112 bytes)</li>
    <li><b>params.json</b> (JSON file of hyperparameters)</li>
  </ul>
<li><b>logs/</b> (directory):</li>
  <ul>
    <li><b>train.log</b> (text log of training)</li>
  </ul>
<li><b>metrics.csv</b> (CSV file of recorded metrics)</li>
</ul>

<b>Task:</b>
<ol>
<li>Create a compressed archive (<b>.tar.gz</b>) of the entire <b>exp_42</b> directory named <b>exp_42_backup_YYYYMMDD.tar.gz</b>, where <b>YYYYMMDD</b> is today's date (e.g., 20240624 if today is June 24, 2024). The archive must preserve the internal directory structure.</li>
<li>After archiving, generate a SHA256 checksum file named <b>exp_42_backup_YYYYMMDD.sha256</b> in <b>/home/user/ml_experiments/</b>, containing the checksum of the created archive in the standard format: <i>SHA256_HASH  exp_42_backup_YYYYMMDD.tar.gz</i> (two spaces between hash and filename).</li>
<li>To enable quick reference, create a log file at <b>/home/user/ml_experiments/exp_42/backup.log</b>, containing the following information (in the exact order and format specified):</li>
</ol>

<pre>
Backup Date: YYYY-MM-DD
Archive Name: exp_42_backup_YYYYMMDD.tar.gz
Archive Size: X bytes
SHA256: SHA256_HASH
Backup Files:
- model/model.h5
- model/params.json
- logs/train.log
- metrics.csv
</pre>

<ul>
<li>The <b>Archive Size</b> is the size in bytes of the .tar.gz archive file you created, as displayed by stat -c%s (or similar).</li>
<li>The <b>SHA256</b> line must match the hash produced for the archive.</li>
</ul>

All file paths, sizes, hashes, and archive names must match exactly and reflect today's date. All operations must be completed from the terminal, and no files may be left in an inconsistent state. If any step fails, clean up any partial files before retrying.
