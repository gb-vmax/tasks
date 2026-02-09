# Bug Report

### Describe the bug

When specifying input files via both command line arguments and the `--input` flag, the CLI doesn't properly handle the case where `--input` is a string. The duplicate input detection logic seems to be broken and allows conflicting input specifications to pass through without error.

### Reproduction

```bash
# This should raise an error but doesn't
rollup src/main.js --input src/main.js -o dist/bundle.js
```

The command accepts both positional arguments (`src/main.js`) and the `--input` flag with a string value at the same time, which should be considered duplicate/conflicting input options.

### Expected behavior

The CLI should detect when input files are specified in multiple ways (positional args + `--input` flag) and throw an error about duplicate import options, regardless of whether `--input` is a string or an array.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
