# Bug Report

### Describe the bug

When using the tree visitor with SKIP action, child nodes are unexpectedly being visited instead of being skipped. The SKIP action should prevent traversal into the children of the current node, but it appears to be doing the opposite - it only visits children when SKIP is returned.

### Reproduction

```js
import {visit, SKIP} from 'unist-util-visit'

const tree = {
  type: 'root',
  children: [
    {
      type: 'parent',
      children: [
        {type: 'child', value: 'should be skipped'}
      ]
    }
  ]
}

const visited = []

visit(tree, 'parent', (node) => {
  visited.push(node.type)
  return SKIP  // Should skip children
})

visit(tree, 'child', (node) => {
  visited.push(node.type)
})

// Expected: visited = ['parent']
// Actual: visited = ['parent', 'child']
```

The child nodes are being visited even though SKIP was returned for the parent node. This is the opposite of the expected behavior - when SKIP is returned, the visitor should not descend into that node's children.

### Expected behavior

When a visitor function returns SKIP for a node, the traversal should not visit any of that node's children. The children should only be visited when SKIP is NOT returned.

### System Info
- unist-util-visit version: 5.0.0
- Node version: Latest

---
Repository: /testbed
