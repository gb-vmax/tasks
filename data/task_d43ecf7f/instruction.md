I'm a build engineer trying to decide which compression format to use for distributing our application artifacts. I have a build output directory at `/home/user/artifacts/build/` that contains several compiled files. I need you to compress this directory using two different formats and then write a comparison report so I can decide which to use in our CI pipeline.

Here's what I need done:

1. Create a **gzip-compressed tarball** of the entire `/home/user/artifacts/build/` directory. Save it as `/home/user/artifacts/build.tar.gz`.

2. Create a **bzip2-compressed tarball** of the entire `/home/user/artifacts/build/` directory. Save it as `/home/user/artifacts/build.tar.bz2`.

3. Write a plain-text report to `/home/user/artifacts/compression_report.txt` that compares the two archives. The report must follow this **exact format** (replace the angle-bracket placeholders with actual byte counts from `ls -l` or `wc -c`, no commas, no units, just raw integers):

```
compression comparison
build.tar.gz <N>
build.tar.bz2 <N>
winner <filename>
```

- Line 1 is literally `compression comparison` (all lowercase, no colon).
- Lines 2 and 3 each have the filename, a single space, then the file size in bytes as a plain integer.
- Line 4 is `winner ` followed by the filename (e.g., `build.tar.bz2`) of whichever archive is **smaller**.
- If they are the same size, write `winner tie` on line 4.
- There must be no trailing spaces, no blank lines, and no extra lines in the file.

Please make sure both archive files actually exist at the specified paths before writing the report, and that the byte sizes in the report match the actual sizes of the files on disk.
