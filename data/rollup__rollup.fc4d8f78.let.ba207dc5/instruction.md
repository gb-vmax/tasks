# Bug Report

### Describe the bug

When running rollup with command line arguments, I'm getting an unexpected error about duplicate import options even when I'm only providing input files through positional arguments and not using the `--input` flag at all.

### Reproduction

```bash
# This command throws an error when it shouldn't
rollup src/main.js --format esm --file dist/bundle.js
```

The error message says there are duplicate import options, but I'm only specifying the input file as a positional argument. This used to work fine in previous versions.

### Expected behavior

The command should accept positional arguments for input files without throwing a duplicate import options error. The error should only occur when both positional arguments AND the `--input` flag are used together, like:

```bash
rollup src/main.js --input src/other.js --format esm
```

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
