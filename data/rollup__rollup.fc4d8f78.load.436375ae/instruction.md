# Bug Report

### Describe the bug

The CLI help text is not being processed correctly - newlines are missing after region markers are removed. When viewing the help output, region comment lines are being removed but the newline character that follows them is not, causing the next line to be concatenated with the previous line.

### Reproduction

1. Add region comments in the help.md file like:
```
Some help text
// #region example
Example content
// #endregion
More help text
```

2. Build the CLI and check the help output
3. The output will be missing newlines where region markers were removed

### Expected behavior

When region markers are stripped from the help file, the newlines should be preserved so that the help text formatting remains intact. Each line should appear on its own line in the final output.

### System Info
- Node version: Latest
- OS: Any

---
Repository: /testbed
