# Bug Report

### Describe the bug

I'm experiencing an issue where parsing certain AST structures results in incorrect node lists. When processing node lists from the buffer, the output contains an extra element that shouldn't be there, and the last element appears to be duplicated or incorrectly positioned.

### Reproduction

```js
// Parse a module with multiple statements
const ast = parseModule(`
  const a = 1;
  const b = 2;
  const c = 3;
`);

// The body array has an extra element
console.log(ast.body.length); // Expected: 3, Actual: 4
```

The issue seems to affect any code that generates node lists internally. The resulting AST has one more element than expected, with the last element appearing twice or being incorrectly parsed.

### Expected behavior

Node lists should contain exactly the number of elements specified in the buffer, without any duplicates or extra entries.

### System Info
- Rollup version: latest
- Node: v18.x

---
Repository: /testbed
