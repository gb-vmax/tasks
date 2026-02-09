# Bug Report

### Describe the bug

I'm experiencing an issue with node filtering when using multiple test conditions. When I provide an array of test functions, nodes that should be visited are being skipped, and nodes that shouldn't match are being visited instead.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', value: 'test' },
    { type: 'heading', value: 'title' },
    { type: 'code', value: 'example' }
  ]
}

// Try to visit only 'paragraph' OR 'heading' nodes
visit(tree, ['paragraph', 'heading'], (node) => {
  console.log(node.type)
})

// Expected: logs 'paragraph' and 'heading'
// Actual: logs 'code' instead (the node that doesn't match)
```

The behavior seems completely inverted - nodes that match the criteria are being filtered out while non-matching nodes are being processed.

### Expected behavior

When passing multiple test conditions (like an array of node types), the visitor should process nodes that match ANY of the conditions, not the ones that fail all conditions.

### System Info
- unist-util-visit version: 5.0.0
- Node.js version: 18.x

---
Repository: /testbed
