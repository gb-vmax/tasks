# Bug Report

### Describe the bug

I'm experiencing an issue with variable declarations where destructuring patterns are not being included correctly in the bundled output. When using destructured variable declarations, the generated code seems to be missing the necessary destructuring logic, causing runtime errors.

### Reproduction

```js
// Input code
const { a, b } = someObject;
console.log(a, b);

// Expected: Both 'a' and 'b' should be properly destructured and available
// Actual: The destructuring doesn't work as expected in the output
```

Another case:

```js
const { nested: { value } } = config;
// The nested destructuring pattern is not being handled properly
```

### Expected behavior

Variable declarations with destructuring patterns should be correctly included in the bundle, with all destructured identifiers properly extracted and available for use.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The bundled code either throws reference errors or doesn't include the proper destructuring logic. Regular variable declarations (non-destructured) work fine.

---
Repository: /testbed
