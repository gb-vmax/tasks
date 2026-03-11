I'm an automation specialist and I've been handed a legacy workflow script that was flagged in a security audit. The script is at `/home/user/workflows/process_orders.sh` and it processes daily order data. The security team flagged it for using predictable temporary file paths — a classic TOCTOU (Time-of-Check Time-of-Use) vulnerability where an attacker could create a symlink at the predictable path before the script runs, potentially overwriting arbitrary files or reading sensitive data.

I need you to fix the security vulnerability in the script so it uses secure temporary file creation instead, and also make sure the temporary file is always cleaned up when the script exits (including on errors or signals).

Here are the specific requirements:

1. **Identify the insecure line**: The script currently creates a temporary file using a hardcoded predictable path under `/tmp` (e.g., `/tmp/orders_temp.csv`). This is the vulnerability.

2. **Fix the temporary file creation**: Replace the hardcoded temp file path with a call to `mktemp` that creates a secure, unpredictably-named temporary file. The `mktemp` call must use the template `XXXXXX` suffix convention to generate random characters, specifically use the template `/tmp/orders_tmp.XXXXXX`. Assign the result to a variable called `TMPFILE`.

3. **Add a cleanup trap**: Immediately after the `TMPFILE` variable is assigned, add a `trap` statement that removes `$TMPFILE` on exit. The trap must handle the signals `EXIT`, `INT`, and `TERM`. The trap command should be written on a single line in this exact format:
   ```
   trap "rm -f $TMPFILE" EXIT INT TERM
   ```

4. **Update all references**: Every place in the script that previously referenced the old hardcoded temp path (e.g., `/tmp/orders_temp.csv`) must be updated to use `$TMPFILE` instead.

5. **The fixed script must remain executable** (preserve the execute permission).

The final script at `/home/user/workflows/process_orders.sh` should have the vulnerability fixed with no remaining references to the old hardcoded path `/tmp/orders_temp.csv`. The script should still be logically complete and functional — only the temporary file handling should change.
