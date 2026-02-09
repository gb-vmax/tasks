# Bug Report

### Describe the bug

I'm experiencing an issue with type checking in MDX nodes. It seems like the type comparison is not working as strictly as it should, which could lead to unexpected behavior when processing MDX AST nodes.

### Reproduction

```js
const node = {
  type: 'paragraph',
  // ... other properties
}

// Type checking seems to accept values that shouldn't match
// For example, if node.type is a number or gets coerced
const nodeWithNumericType = {
  type: 123,
  // ... other properties  
}

// This might incorrectly pass type validation
```

The issue appears to be related to how node types are being compared internally. When checking if a node matches a specific type, the comparison doesn't seem to be using strict equality, which could cause type coercion issues.

### Expected behavior

Type checking should use strict equality (`===`) to ensure that only nodes with exactly matching string types are accepted. This would prevent potential bugs from type coercion (e.g., `'123' == 123` evaluating to true).

### System Info
- @mdx-js/mdx version: 3.0.0
- Node.js version: Latest

---
Repository: /testbed
