# Bug Report

### Describe the bug

I'm experiencing an issue with node type checking in MDX processing. When validating nodes, the type checker is returning unexpected results - it seems to be passing nodes that shouldn't match the specified type.

### Reproduction

```js
// When checking if a node matches a specific type
const checker = typeFactory('paragraph')

// This returns true even when node is undefined or null
const result = checker(null)  // Expected: false, Actual: true
const result2 = checker(undefined)  // Expected: false, Actual: true

// Also returns true for nodes with incorrect types
const wrongNode = { type: 'heading' }
const result3 = checker(wrongNode)  // Expected: false, Actual: true
```

### Expected behavior

The type checker should only return `true` when:
1. The node exists (not null/undefined)
2. The node has a `type` property
3. The `type` property matches the expected value

Currently it's returning `true` for nodes that don't match these criteria, which causes downstream processing issues.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
