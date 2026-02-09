# Bug Report

### Describe the bug

I'm experiencing an issue with AST node positions being swapped. When parsing code, the start and end positions of nodes appear to be reversed - the start position contains what should be the end position and vice versa.

### Reproduction

```js
// Parse any code with the AST parser
const ast = parse(`
  function example() {
    return 42;
  }
`);

// Check node positions
console.log(ast.body[0].start); // Shows end position
console.log(ast.body[0].end);   // Shows start position
```

The start position is greater than the end position, which doesn't make sense. This breaks any tooling that relies on correct source location information.

### Expected behavior

Node start positions should be less than or equal to end positions. The `start` property should indicate where the node begins in the source code, and `end` should indicate where it finishes.

### System Info
- Version: Latest from main branch
- Node: v18.x

---
Repository: /testbed
