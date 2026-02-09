# Bug Report

### Describe the bug

When passing an array of entry modules, the first entry point is being skipped during module normalization. Only entries from index 1 onwards are being processed, which causes the first entry module to be completely ignored during the build process.

### Reproduction

```js
const rollup = require('rollup');

// Configure with multiple entry points as an array
const inputOptions = {
  input: ['src/main.js', 'src/secondary.js', 'src/third.js']
};

// Build the bundle
const bundle = await rollup.rollup(inputOptions);

// Expected: All three modules should be processed
// Actual: Only 'src/secondary.js' and 'src/third.js' are included
// 'src/main.js' is missing from the output
```

### Expected behavior

All entry modules provided in the array should be included in the build. The first entry point should not be skipped.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
