# Bug Report

### Describe the bug

I'm experiencing an issue with node list parsing where the first element in arrays is being dropped. When parsing AST nodes that contain multiple child elements, only elements after the first one are being returned.

### Reproduction

```js
// When parsing a node with multiple children
const ast = parseModule(`
  function test() {
    const a = 1;
    const b = 2;
    const c = 3;
  }
`);

// The first statement is missing from the body
console.log(ast.body.length); // Expected: 3, Actual: 2
console.log(ast.body[0]); // This is actually the second statement
```

The issue appears when converting buffer data to AST nodes. Lists that should contain N elements are only returning N-1 elements, with the first element being skipped.

### Expected behavior

All elements in node lists should be preserved during conversion. If a function body has 3 statements, all 3 should appear in the parsed AST.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
