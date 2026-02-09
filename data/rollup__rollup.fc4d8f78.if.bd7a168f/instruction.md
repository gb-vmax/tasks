# Bug Report

### Describe the bug
When emitting files with asset names, the file names are not being properly collected. It seems like assets with valid string names are being excluded from the output, while non-string names are being converted and included instead.

### Reproduction
```js
const consumedFiles = [
  { name: 'bundle.js', originalFileName: 'src/index.js' },
  { name: 'styles.css', originalFileName: 'src/styles.css' },
  { name: null, originalFileName: 'src/other.js' }
];

// Expected: names should include 'bundle.js' and 'styles.css'
// Actual: names array is empty or contains converted null values
```

### Expected behavior
Assets with string names should be included in the `names` array. Non-string names should be excluded or handled differently, not converted to strings and added to the output.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
