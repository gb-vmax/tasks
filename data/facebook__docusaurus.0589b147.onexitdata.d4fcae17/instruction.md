# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the position information for data nodes appears to be incorrect. After processing text content, the `position.start` of data nodes is being set to the end position of the token instead of remaining at the original start position.

### Reproduction

```js
// Parse MDX content with text data
const result = compile('Some text content here');

// Check the position information of the data node
console.log(result.data.position.start);
console.log(result.data.position.end);

// Expected: start and end positions should be different
// Actual: start position is set to the same value as end position
```

### Expected behavior

The `position.start` should remain at the beginning of the data node and `position.end` should be at the end. Both should not point to the same location after the token is processed.

### Additional context

This seems to affect any MDX content that contains text data. The position tracking gets messed up because the start position is being overwritten with the end position value, which breaks any tooling that relies on accurate source position information for things like:
- Syntax highlighting
- Error reporting
- Source maps
- AST navigation

The stack is also not being properly managed - looks like the tail element is being referenced but not removed from the stack after processing.

---
Repository: /testbed
