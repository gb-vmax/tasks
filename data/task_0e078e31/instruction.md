I'm a build engineer and I need your help verifying the integrity of some build artifacts before they get published to our artifact repository. We had a storage hiccup earlier and I want to confirm which files are intact and which are corrupted.

The build artifacts are in `/home/user/artifacts/`. There are several `.jar` files in that directory. Alongside each `.jar`, there is a corresponding `.sha256` file that contains the expected checksum (just the hex digest, nothing else).

Here's what I need you to do:

1. For each `.jar` file in `/home/user/artifacts/`, compute its actual SHA256 checksum and compare it against the expected checksum stored in the matching `.sha256` file.

2. Write a verification report to `/home/user/artifacts/verification_report.txt` with the following **exact** format:

```
Build Artifact Verification Report
===================================
app-core-1.0.jar: OK
app-ui-2.1.jar: CORRUPTED
app-utils-1.4.jar: OK
===================================
Total: 3 | Passed: 2 | Failed: 1
```

The rules for the report:
- The header must be exactly `Build Artifact Verification Report` followed by a line of exactly 35 `=` signs.
- Each artifact line must be `<filename>: OK` or `<filename>: CORRUPTED`, with the jar filename only (no directory path).
- The artifact lines must be sorted **alphabetically** by filename.
- The footer is a line of exactly 35 `=` signs, followed by a summary line in the format `Total: <N> | Passed: <P> | Failed: <F>` where N is the total number of jars checked, P is how many had matching checksums, and F is how many did not.
- A file is `OK` if its computed SHA256 hex digest matches the content of the `.sha256` file exactly. It is `CORRUPTED` if they differ.

The `.sha256` files each contain just the raw 64-character hex digest with no filename suffix, no spaces, no trailing newline — just the hex string.

Please write the report to `/home/user/artifacts/verification_report.txt`. Do not include the `.sha256` files themselves in the report, only the `.jar` files.
