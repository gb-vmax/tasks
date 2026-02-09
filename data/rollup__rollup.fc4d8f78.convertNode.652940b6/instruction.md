# Bug Report

### Describe the bug

I'm encountering an issue where AST node conversion is failing with "Unknown node type" errors even though the node type appears to be valid. The error seems to be thrown incorrectly in some cases.

### Reproduction

When processing certain AST buffers, the converter throws an error about an unknown node type, but the stack trace suggests the node type should actually be recognized. The error appears to be a false positive.

```js
// Processing an AST buffer with a valid node type
const result = convertNode(position, buffer);
// Error: Unknown node type: <valid_type>
```

The issue seems intermittent and depends on the specific buffer contents, but when it occurs, valid node types are being rejected.

### Expected behavior

The converter should successfully process valid node types without throwing errors. The validation check should only throw when the node type is genuinely unsupported.

### Additional context

This appears to have started happening recently. The error message and stack trace don't align - the node type in the error message is actually a recognized type that should be handled by one of the converters.

---
Repository: /testbed
