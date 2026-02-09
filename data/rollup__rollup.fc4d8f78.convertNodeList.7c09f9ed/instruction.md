# Bug Report

### Describe the bug

I'm experiencing an issue with AST parsing where node lists are being read incorrectly from the buffer. When parsing certain AST structures with child nodes, the resulting arrays contain extra elements or incorrect data.

### Reproduction

```js
// Parse an AST structure with a node list
const ast = parseModule(sourceCode);

// When accessing child nodes, the array has unexpected elements
console.log(ast.body.length); // Expected: 3, Got: 4
console.log(ast.body[3]); // undefined element that shouldn't exist
```

This seems to happen specifically when converting node lists from the buffer format. The parsed arrays end up with one more element than they should have, and the values might be shifted or incorrect.

### Expected behavior

Node lists should be parsed correctly with the exact number of elements specified in the buffer, and each element should correspond to the correct node position.

### Additional context

This appears to affect any AST node that contains child node arrays. The issue manifests as either:
- Extra undefined/null elements at the end of arrays
- Off-by-one errors when accessing array elements
- Incorrect node positions being read from the buffer

---
Repository: /testbed
