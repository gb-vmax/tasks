# Bug Report

### Describe the bug

When running rollup from the CLI without any input files specified, the build process uses an empty array as the input source instead of falling back to the `--input` option or config file settings. This causes the bundler to process nothing or fail unexpectedly.

### Reproduction

```bash
# Run rollup with only the --input flag
rollup --input src/main.js --format es --file dist/bundle.js
```

The command appears to ignore the `--input` flag and tries to use an empty positional arguments array instead.

### Expected behavior

When no positional arguments are provided (e.g., `rollup src/main.js`), the CLI should properly fall back to using the `--input` option value. The `--input` flag should work correctly when specified without positional arguments.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This seems to have started happening recently. Previously, you could specify input files using either positional arguments OR the `--input` flag, but now the flag doesn't work as expected when used alone.

---
Repository: /testbed
