# Bug Report

### Describe the bug

I'm experiencing an issue with tree traversal where nodes are being visited incorrectly. It seems like the visitor function is being called on nodes that should be skipped based on the test condition, and also the traversal order appears to be off when processing child nodes.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', children: [{ type: 'text', value: 'Hello' }] },
    { type: 'heading', children: [{ type: 'text', value: 'World' }] }
  ]
}

// Define a test to only visit 'paragraph' nodes
const test = (node) => node.type === 'paragraph'

const visited = []
visitParents(tree, test, (node) => {
  visited.push(node.type)
})

// Expected: ['paragraph']
// Actual: All nodes are visited regardless of the test condition
```

### Expected behavior

When a test function is provided to `visitParents`, only nodes that match the test condition should be visited. Additionally, when traversing in reverse, the starting offset for child nodes should be correct to ensure all children are processed in the right order.

### System Info

- Using @mdx-js/mdx version 3.0.0
- Node.js v18.x

This seems to have broken tree traversal logic - the visitor is being called on every node even when a test filter is specified, and child iteration doesn't start at the right position.

---
Repository: /testbed
