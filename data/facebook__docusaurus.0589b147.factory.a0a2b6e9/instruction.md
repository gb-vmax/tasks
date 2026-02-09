# Bug Report

### Describe the bug

I'm experiencing an issue where the AST visitor seems to stop traversing the tree prematurely. When processing markdown/HTML documents with nested structures, only the top-level nodes are being visited and child nodes are being skipped entirely.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [
        { type: 'text', value: 'Hello' },
        { type: 'emphasis', children: [{ type: 'text', value: 'world' }] }
      ]
    }
  ]
}

visit(tree, 'text', (node) => {
  console.log(node.value)
})

// Expected: logs "Hello" and "world"
// Actual: only logs "Hello" (or nothing at all)
```

The visitor function is called for the first text node but doesn't descend into nested children. It seems like the tree traversal is incomplete.

### Expected behavior

All nodes matching the test condition should be visited, regardless of nesting depth. The visitor should traverse the entire tree structure and call the visitor function for every matching node.

### System Info
- Node version: 18.x
- Browser: N/A (server-side)

This seems to have started happening recently. The tree structure is valid and worked fine before.

---
Repository: /testbed
