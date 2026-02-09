# Bug Report

### Describe the bug

The `indent` function is not properly indenting multi-line strings. When a string contains multiple newline characters, only the first newline is being processed, leaving subsequent lines unindented.

### Reproduction

```js
const multiLineString = `line1
line2
line3`;

const indented = indent(multiLineString);
console.log(indented);

// Current output:
//  line1
//   line2
// line3

// Expected output:
//  line1
//  line2
//  line3
```

### Expected behavior

All lines in a multi-line string should be indented consistently. The function should replace ALL newline characters with newline + indentation, not just the first one.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
