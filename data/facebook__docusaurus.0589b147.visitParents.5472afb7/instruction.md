# Bug Report

### Describe the bug

I'm experiencing an issue with tree traversal when using `visitParents` in reverse mode. The visitor function seems to be skipping the first child node when traversing in reverse order, and also appears to be passing an incorrect parent reference (undefined) to the test function.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', children: [{ type: 'text', value: 'first' }] },
    { type: 'paragraph', children: [{ type: 'text', value: 'second' }] },
    { type: 'paragraph', children: [{ type: 'text', value: 'third' }] }
  ]
}

const visited = []
visitParents(tree, 'text', (node, parents) => {
  visited.push(node.value)
}, true) // reverse = true

// Expected: ['third', 'second', 'first']
// Actual: ['third', 'second'] - 'first' is missing
```

Additionally, when using a test function that checks the parent, it receives `undefined` instead of the actual parent node:

```js
visitParents(tree, (node, index, parent) => {
  console.log(parent) // logs undefined for root-level nodes
  return node.type === 'text'
}, (node) => {
  // visitor logic
})
```

### Expected behavior

- When traversing in reverse, all child nodes should be visited including the first one
- The parent parameter passed to the test function should be the actual parent node, not undefined

This seems to have started happening recently and is breaking my tree traversal logic that relies on visiting all nodes in reverse order.

---
Repository: /testbed
