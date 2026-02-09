# Bug Report

### Describe the bug

I'm encountering an issue where AST nodes are being created with incorrect position information. The `end` position of nodes appears to be set to the same value as the `start` position, which results in zero-length spans for all nodes in the parse tree.

### Reproduction

```js
// Parse any source code
const ast = parse(`
  const x = 42;
  console.log(x);
`);

// Check node positions
const firstNode = ast.body[0];
console.log(`Start: ${firstNode.start}, End: ${firstNode.end}`);
// Output: Start: 3, End: 3
// Expected: Start: 3, End: 16
```

When inspecting the generated AST, all nodes have `start === end`, making it impossible to:
- Extract source code snippets for nodes
- Generate accurate source maps
- Determine the actual span of declarations/expressions

### Expected behavior

Each AST node should have correct `start` and `end` positions that reflect the actual character positions in the source code. The `end` position should be greater than the `start` position for non-empty nodes.

### Additional context

This seems to have started recently. The parser is reading from the buffer correctly but the position offsets appear to be wrong when constructing the nodes.

---
Repository: /testbed
