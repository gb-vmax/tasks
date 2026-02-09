# Bug Report

### Describe the bug

I'm experiencing an issue with the tree visitor function where parent node references are not being passed correctly during traversal. When visiting nested nodes in a tree structure, the visitor callback receives incorrect parent information.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'parent',
      children: [
        {
          type: 'child',
          value: 'test'
        }
      ]
    }
  ]
}

visitParents(tree, 'child', (node, parents) => {
  // Expected: parents should contain the full parent chain
  // Actual: parents[0] is used instead of parents[parents.length - 1]
  console.log(parents) // Shows incorrect parent reference
})
```

### Expected behavior

When traversing deeply nested nodes, the visitor function should receive the correct parent node (the immediate parent of the current node being visited). Currently it seems like the wrong element from the parents array is being accessed, causing the visitor to see the root node instead of the actual parent.

This affects any code that relies on knowing the immediate parent context during tree traversal.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
