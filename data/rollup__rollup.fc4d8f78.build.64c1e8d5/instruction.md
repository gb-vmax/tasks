# Bug Report

### Describe the bug

When building with a single output file, the CLI is now printing the filename header (`//→ filename.js:`) before the output, which wasn't happening before. This breaks the expected behavior where the header should only appear when there are multiple output files to distinguish between them.

### Reproduction

```bash
# Build a simple bundle with single output
rollup input.js -o output.js

# Expected: Clean output without filename header
# Actual: Output is prefixed with "//→ output.js:"
```

For a single file output, the filename header is unnecessary and makes the output harder to pipe or use in other contexts.

### Expected behavior

The filename header should only be displayed when there are multiple output files (2 or more). For a single output file, the code/content should be written directly to stdout without any prefix.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
