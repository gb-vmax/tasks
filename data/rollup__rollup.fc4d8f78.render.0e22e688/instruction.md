# Bug Report

### Describe the bug

I'm experiencing an issue with binary expression rendering where an extra character appears in the output after constant folding optimization. When a binary expression gets evaluated to a literal value at compile time, the replacement seems to be including one character too many from the original source.

### Reproduction

```js
// Input code
const result = 1 + 2;

// Expected output after optimization
const result = 3;

// Actual output
const result = 3;  // (includes an extra character from the source)
```

This happens when binary expressions are optimized and replaced with their computed literal values. The rendered output appears to be overwriting one position beyond where it should stop.

### Expected behavior

When a binary expression is replaced with its literal value during rendering, it should only replace the exact range of the expression without affecting any adjacent characters in the source code.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
