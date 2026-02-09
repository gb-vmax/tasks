# Bug Report

### Describe the bug

I'm experiencing an issue with tree traversal when using `visitParents()` with a test condition. The visitor function is not being called on nodes that should match the test criteria.

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

const visited = []
visitParents(tree, 'text', (node) => {
  visited.push(node.value)
})

// Expected: ['Hello', 'world']
// Actual: nothing gets visited
```

When I provide a test condition (like a node type string), the visitor function never gets called even though matching nodes exist in the tree. If I remove the test condition entirely, the visitor works but visits all nodes regardless of type.

### Expected behavior

The visitor should be called for all nodes matching the test condition. In the example above, it should visit both text nodes and collect their values.

### Additional context

This seems to affect both forward and reverse traversal modes. The issue appears when any test parameter is provided to `visitParents()`.

---
Repository: /testbed
