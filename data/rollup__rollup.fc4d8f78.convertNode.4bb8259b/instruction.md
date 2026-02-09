# Bug Report

### Describe the bug

I'm encountering an issue with AST parsing where nodes are being incorrectly converted. When processing the buffer, the node type and position seem to be misaligned, causing the parser to fail or produce incorrect results.

### Reproduction

```js
// When converting AST nodes from buffer
const ast = parseModule(sourceCode);

// The node conversion appears to be reading from wrong buffer positions
// This leads to incorrect node types being detected or positions being off by one
```

### Expected behavior

The AST conversion should correctly read the node type from the buffer and pass the appropriate position to the converter function. Each node should be properly parsed with its type and position aligned.

### Additional context

This seems to affect all node conversions when reading from the AST buffer. The converter is either reading the node type from the wrong position or passing an incorrect position offset to the conversion function, which breaks the entire parsing process.

---
Repository: /testbed
