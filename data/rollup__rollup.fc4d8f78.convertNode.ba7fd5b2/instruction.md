# Bug Report

### Describe the bug

I'm experiencing incorrect AST node parsing when working with buffer-based parsing. The node positions seem to be off, causing properties to be read from the wrong buffer offsets. This leads to corrupted or incorrect AST node data.

### Reproduction

```js
// When parsing nodes from buffer
const buffer = createBuffer(sourceCode);
const node = parseNode(buffer);

// Node properties are incorrect
// For example, if the node should have certain child nodes or properties,
// they appear to be missing or contain wrong values
console.log(node); // Shows unexpected structure
```

The issue appears to be related to how buffer positions are being calculated during node conversion. After the node type, start, and end positions are set, subsequent parsing operations seem to read from incorrect buffer offsets.

### Expected behavior

Nodes should be parsed correctly with all properties and child nodes properly initialized from the correct buffer positions. The AST structure should accurately represent the source code.

### Additional context

This seems to have broken recently. The node initialization and buffer parsing order might be related to the problem, as the data being read doesn't match what's expected for the node type.

---
Repository: /testbed
