# Bug Report

### Describe the bug

I'm experiencing an issue with node type checking in MDX processing. It seems like nodes are being incorrectly identified or filtered based on their type. When processing MDX content, nodes that should match a specific type are being excluded, and nodes that shouldn't match are being included instead.

### Reproduction

```js
// When checking for a specific node type
const checker = typeFactory('paragraph')

// This returns true for non-paragraph nodes
checker({ type: 'heading' }) // returns true (unexpected)

// And returns false for actual paragraph nodes  
checker({ type: 'paragraph' }) // returns false (unexpected)
```

The behavior is inverted - nodes are passing the type check when they shouldn't, and failing when they should pass.

### Expected behavior

Type checking should correctly identify nodes:
- `checker({ type: 'paragraph' })` should return `true` for matching types
- `checker({ type: 'heading' })` should return `false` for non-matching types

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
