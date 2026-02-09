# Bug Report

### Describe the bug

I'm encountering an issue where AST node conversion is failing with an error about unknown node types. The error appears to be triggered when processing certain AST buffers, and it's causing the parser to crash unexpectedly.

### Reproduction

```js
// When converting AST nodes from buffer
const buffer = [/* some AST buffer data */];
const node = convertNode(0, buffer);
// Throws: "Unknown node type: <type>"
```

The error occurs during AST conversion and seems to be related to how node converters are being looked up. The position being passed to the converter appears to be off by one, which might be causing the wrong node type to be read from the buffer.

### Expected behavior

The AST node should be converted successfully without throwing errors about unknown node types. The converter should properly read the node type from the buffer and apply the correct conversion.

### Additional context

This seems to have started happening recently. The error message includes a stack trace but the actual node type value doesn't match any expected types. It's possible that the buffer position offset is incorrect when calling the converter function.

---
Repository: /testbed
