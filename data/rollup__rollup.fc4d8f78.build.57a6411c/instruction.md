# Bug Report

### Describe the bug

When building with a single output file, the CLI now prints the file name header (`//→ filename:`) before the output, which wasn't happening before. This creates unexpected output formatting when piping or redirecting the build output.

### Reproduction

```bash
# Build with single output configuration
rollup -c rollup.config.js

# Expected: clean output without header
# Actual: output includes "//→ bundle.js:" header
```

The issue occurs when there's only one output file. Previously, the header was only shown when there were multiple outputs to help distinguish between them.

### Expected behavior

When building with a single output file, the output should be printed directly without the `//→ filename:` header, just like in previous versions. The header should only appear when there are multiple output files to differentiate between them.

### Additional context

This affects scripts that rely on clean output from the build process, especially when using stdout redirection or piping the output to other tools.

---
Repository: /testbed
