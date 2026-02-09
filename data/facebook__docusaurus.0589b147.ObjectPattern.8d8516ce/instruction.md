# Bug Report

### Describe the bug

I'm experiencing an issue with object destructuring patterns in MDX code generation. When using object destructuring with multiple properties, the generated output is malformed - it seems like the first property is being skipped entirely.

### Reproduction

```js
// Input MDX with object destructuring
const { a, b, c } = props;

// Expected generated output:
// const {a, b, c} = props;

// Actual generated output appears to be missing the first property
// const {, b, c} = props;
```

This results in invalid JavaScript syntax being generated. The issue appears when destructuring objects with 2 or more properties.

### Expected behavior

Object destructuring patterns should generate valid JavaScript code with all properties included in the correct order, starting from the first property.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
