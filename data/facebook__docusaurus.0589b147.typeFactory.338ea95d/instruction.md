# Bug Report

### Describe the bug

I'm experiencing an issue with the type checking logic in the remark vendor code. It seems like the type validation is behaving inversely - nodes that should match a specific type are being rejected, and nodes that shouldn't match are being accepted.

### Reproduction

```js
// When checking for a specific node type, the validation fails unexpectedly
const checker = typeFactory('paragraph');

// This should return true but returns false
const paragraphNode = { type: 'paragraph', children: [] };
console.log(checker(paragraphNode)); // Expected: true, Actual: false

// This should return false but returns true  
const headingNode = { type: 'heading', depth: 1 };
console.log(checker(headingNode)); // Expected: false, Actual: true
```

### Expected behavior

The type factory should correctly identify nodes that match the specified type. When I create a checker for 'paragraph' nodes, it should return `true` for paragraph nodes and `false` for other node types.

### Additional context

This appears to be affecting markdown parsing functionality. The type matching logic seems to be inverted from what it should be.

---
Repository: /testbed
