# Bug Report

### Describe the bug

When using the CLI with the `--no-stdin` flag, the stdin plugin is still being added and enabled. The flag appears to be ignored and stdin input is always processed regardless of the command line option.

### Reproduction

```bash
# This should disable stdin but it's still active
rollup --no-stdin -c

# Or programmatically:
rollup({
  stdin: false
})
```

The stdin plugin gets added even when explicitly setting `stdin: false` in the configuration or using `--no-stdin` on the command line.

### Expected behavior

When `stdin: false` is specified or `--no-stdin` flag is used, the stdin plugin should not be added to the input options and stdin input should be disabled.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
