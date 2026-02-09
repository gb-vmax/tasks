# Bug Report

### Describe the bug

The build process is now showing warnings even when the `--silent` flag is passed. The silent mode should suppress all output including warnings, but warnings are still being printed to the console.

### Reproduction

```bash
# Run rollup with silent flag
rollup -c --silent

# Warnings still appear in the output despite --silent flag
```

When building with the `--silent` flag, I expect no output at all, but warnings are still being displayed. This breaks automated build scripts that rely on silent mode for clean output.

### Expected behavior

When using the `--silent` flag, all warnings and output should be suppressed. The build should run completely silently unless there's an actual error.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
