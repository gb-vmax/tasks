# Bug Report

### Describe the bug

When generating code snippets for objects with fields, the formatting appears to be incorrect. Objects that should have line breaks and proper indentation are being rendered without them, while empty objects are getting unnecessary whitespace.

### Reproduction

```js
// Generate a code snippet for an object with properties
const snippet = getObject([
  ['name', 'value'],
  ['age', '25']
], { 
  lineBreakIndent: { base: '', t: '  ' } 
});

// Expected output (with proper formatting):
// {
//   name: value,
//   age: 25
// }

// Actual output:
// {name: value,age: 25}
```

The issue also affects empty objects - they're getting formatted with line breaks when they shouldn't be.

### Expected behavior

Objects with fields should respect the `lineBreakIndent` configuration and include proper line breaks and indentation. Empty objects should remain compact without extra whitespace.

### System Info
- Node version: 18.x
- Using latest version from main branch

---
Repository: /testbed
