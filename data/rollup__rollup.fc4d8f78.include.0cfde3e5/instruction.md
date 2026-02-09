# Bug Report

### Describe the bug

I'm experiencing an issue with variable declarations in destructuring patterns. When using object or array destructuring in variable declarations, the identifiers are not being included in the output bundle correctly.

### Reproduction

```js
// Input code
const { a, b } = obj;
const [x, y] = arr;

// These declarations seem to be handled incorrectly
// The identifiers (a, b, x, y) are missing from the output
```

### Expected behavior

When destructuring is used in variable declarations, all identifiers should be properly included in the bundled output. The destructuring patterns should be preserved or transformed correctly so that the variables are accessible.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The variable declarations with destructuring patterns are not being processed as expected during the bundling process.

---
Repository: /testbed
