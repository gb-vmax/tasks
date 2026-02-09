# Bug Report

### Describe the bug

I'm experiencing an issue with source map generation where the line and column numbers appear to be swapped in the output. When debugging bundled code, the source map points to incorrect locations - specifically, it seems like line numbers are being used as column numbers and vice versa.

### Reproduction

```js
// Given a source file with the following structure:
// Line 10, Column 5: some code

// After bundling and checking the source map:
// The mapping points to Line 5, Column 10 instead

// This makes debugging impossible as breakpoints and error traces
// point to completely wrong locations in the original source
```

### Expected behavior

Source maps should correctly map the bundled code positions back to the original source positions, with line and column numbers preserved accurately. Line numbers should map to lines, and column numbers should map to columns.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing major issues when trying to debug production builds. Any help would be appreciated!

---
Repository: /testbed
