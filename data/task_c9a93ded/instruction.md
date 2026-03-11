Hey, I need some help with one of our older mobile CI scripts. We have a legacy Android build pipeline script at `/home/user/pipeline/check_apk_sizes.py` that was written for Python 2 and I need to get it running under Python 3. The script scans a directory for `.apk` files and prints a size report to stdout.

Right now the script is broken — if you run it with `python3`, it fails immediately. Please fix the script so it runs correctly under Python 3, then run it against the `/home/user/pipeline/apks/` directory and redirect the output to `/home/user/pipeline/size_report.txt`.

The output written to `/home/user/pipeline/size_report.txt` must be exactly this format (one line per APK, sorted alphabetically by filename, followed by a total line):

```
app-debug.apk: 1024 KB
app-release.apk: 2048 KB
app-staging.apk: 512 KB
---
Total: 3584 KB
```

Where the KB values are calculated by dividing each file's byte size by 1024 and rounding down (integer division), and the Total is the sum of those KB values. The `---` separator and `Total:` line must appear exactly as shown.

Only fix what's necessary to make the Python 2 script run under Python 3 — don't rewrite the whole thing. Once fixed, run it and make sure `/home/user/pipeline/size_report.txt` contains the correct output.
