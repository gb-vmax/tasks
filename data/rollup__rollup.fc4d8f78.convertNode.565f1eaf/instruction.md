# Bug Report

### Describe the bug

I'm experiencing an issue with AST node position tracking. When parsing code, the start and end positions of nodes appear to be swapped - the start position contains what should be the end position and vice versa.

### Reproduction

```js
// Parse some code and check node positions
const ast = parse('const x = 1;');
const declaration = ast.body[0];

console.log('Start:', declaration.start); // Expected: 0, Actual: 11
console.log('End:', declaration.end);     // Expected: 11, Actual: 0
```

The node's `start` property returns the ending position and the `end` property returns the starting position. This makes it impossible to correctly extract source code ranges or perform accurate source mapping.

### Expected behavior

Node positions should be set correctly with `start` containing the beginning position and `end` containing the ending position of the node in the source code.

### Additional context

This seems to affect all node types during parsing. The positions are completely reversed which breaks any tooling that relies on accurate source locations.

---
Repository: /testbed
