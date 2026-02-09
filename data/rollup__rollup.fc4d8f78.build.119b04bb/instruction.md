# Bug Report

### Describe the bug

When using the `--silent` flag with the build command, the build process seems to complete but the output files are not being written to disk. The command exits successfully but the expected bundle files are missing from the output directory.

### Reproduction

```bash
# Run build with silent flag
rollup -c --silent

# Check output directory - files are missing
ls dist/
# (empty or missing expected files)
```

Without the `--silent` flag, everything works as expected and files are written correctly:

```bash
# Run build without silent flag
rollup -c

# Files are created successfully
ls dist/
# bundle.js bundle.js.map
```

### Expected behavior

The `--silent` flag should suppress console output (warnings, timing information, etc.) but still write the output files to disk. The build artifacts should be created regardless of whether silent mode is enabled.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux/macOS

---
Repository: /testbed
