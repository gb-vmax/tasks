# Bug Report

### Describe the bug

I'm encountering an issue with node type checking in the MDX parser. It seems like the type validation is returning incorrect results, causing nodes to be incorrectly identified or filtered.

### Reproduction

When working with MDX content that contains specific node types, the parser appears to be accepting nodes that should be rejected or vice versa. This is causing unexpected behavior in content processing.

```js
// Example scenario where type checking fails
const node = {
  type: 'paragraph',
  children: [...]
}

// Type check returns unexpected result
// Expected: true when node.type matches
// Actual: incorrect boolean value
```

### Expected behavior

The type checking function should:
- Return `true` when a node exists AND its type matches the expected type
- Return `false` when the node doesn't exist OR its type doesn't match

Currently, the logic seems inverted or incorrect, leading to nodes being incorrectly validated.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node.js version: Latest

This is breaking content parsing for documents with nested structures. Any help would be appreciated!

---
Repository: /testbed
