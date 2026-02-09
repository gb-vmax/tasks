# Bug Report

### Describe the bug
When using the tree visitor with the `SKIP` action on a parent node, the visitor is still traversing into the children of that node instead of skipping them. This is the opposite of the expected behavior - when I return `SKIP`, I want to skip visiting the children, but currently it seems like children are only visited when `SKIP` is returned.

### Reproduction
```js
import {visit, SKIP} from 'unist-util-visit'

const tree = {
  type: 'root',
  children: [
    {
      type: 'parent',
      children: [
        {type: 'child1'},
        {type: 'child2'}
      ]
    }
  ]
}

visit(tree, 'parent', (node) => {
  console.log('Visiting parent, should skip children')
  return SKIP
})

// Expected: Only the parent node is visited
// Actual: Both parent and its children are visited
```

### Expected behavior
When returning `SKIP` from the visitor function, the visitor should skip traversing into the children of the current node. The children should not be visited at all.

Currently it appears that the logic is inverted - children are being visited when `SKIP` is returned, and not visited otherwise.

### System Info
- Node version: 18.x
- Package: unist-util-visit@5.0.0

---
Repository: /testbed
