# Bug Report

### Describe the bug

I'm experiencing an issue with the `EXIT` constant exported from `unist-util-visit`. When I try to use it to control tree traversal, the comparison doesn't work as expected and the visitor continues traversing instead of stopping.

### Reproduction

```js
import { visit, EXIT } from 'unist-util-visit'

const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', children: [] },
    { type: 'heading', children: [] }
  ]
}

visit(tree, (node) => {
  if (node.type === 'paragraph') {
    return EXIT
  }
  console.log('visited:', node.type)
})
```

### Expected behavior

The visitor should stop traversing the tree after encountering the first paragraph node. The heading node should not be visited.

### Actual behavior

The tree traversal continues even after returning `EXIT`, and all nodes are still being visited. It seems like the `EXIT` constant is not being recognized properly when used as a return value.

This was working fine before, so I suspect something changed with how the constant is being exported or handled.

---
Repository: /testbed
