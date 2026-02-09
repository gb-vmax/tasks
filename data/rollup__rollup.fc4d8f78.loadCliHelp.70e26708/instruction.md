# Bug Report

### Describe the bug

The CLI help text is displaying with extra newlines that shouldn't be there. When running commands like `--help`, the output has additional blank lines appearing throughout the help documentation that make it look messy and harder to read.

### Reproduction

Run any CLI command with the `--help` flag and observe the output formatting. The help text contains unexpected blank lines where region comments were removed.

Example:
```bash
rollup --help
```

The output shows extra newlines scattered throughout the help documentation where there should be continuous text.

### Expected behavior

The help text should display cleanly without extra blank lines. Region comment lines should be removed completely including their newline characters, not leaving behind empty lines in the output.

### System Info
- Node version: Latest
- OS: Any

---
Repository: /testbed
