# Bug Report

### Describe the bug

Translation extraction warnings are being logged even when there are no warnings to display. The console is getting flooded with unnecessary warning messages for files that don't have any translation issues.

### Reproduction

When running the build or translation extraction process, you'll see warning messages like this appearing for every single file, even when there are no actual warnings:

```
Translation extraction warnings for file path=<some-file-path>: []
```

This happens for all source code files being processed, making it difficult to spot actual warnings in the output.

### Expected behavior

Warning messages should only be logged when there are actual warnings to report (i.e., when the warnings array contains at least one warning). Files with no warnings should not produce any log output.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
