# Bug Report

### Describe the bug

The CLI watch mode is not properly waiting for the first input specifier. When multiple input files are specified, the first one is being skipped during the resolution check, which means if the first input file doesn't exist, the build starts anyway without waiting for it.

### Reproduction

1. Start a watch build with multiple input files where the first file doesn't exist yet:
```bash
rollup -w -i missing-file.js -i existing-file.js
```

2. The build proceeds without waiting for `missing-file.js` to be created

3. Only the second and subsequent input files are actually checked

### Expected behavior

The CLI should wait for ALL input specifiers to be available before proceeding with the build, including the first one in the list. It should display the "waiting for input..." message for any missing file regardless of its position.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
