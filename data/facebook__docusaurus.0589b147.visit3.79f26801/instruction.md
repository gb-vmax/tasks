# Bug Report

### Describe the bug

I'm experiencing an issue with tree traversal when using the `SKIP` action in visitor callbacks. When a visitor returns `SKIP` for a node, the traversal seems to be incorrectly processing the node's children instead of skipping them as expected.

### Reproduction

```js
import { visit } from 'unist-util-visit-parents'

const tree = {
  type: 'root',
  children: [
    {
      type: 'parent',
      children: [
        { type: 'child1' },
        { type: 'child2' }
      ]
    }
  ]
}

const visited = []

visit(tree, (node) => {
  visited.push(node.type)
  
  // Skip processing children of 'parent' node
  if (node.type === 'parent') {
    return SKIP
  }
})

console.log(visited)
// Expected: ['root', 'parent']
// Actual: ['root', 'parent', 'child1', 'child2']
```

### Expected behavior

When a visitor function returns `SKIP`, the traversal should skip visiting the children of that node and continue with the next sibling. The children should not be processed at all.

### Additional context

This appears to have started happening recently. The `SKIP` action used to work correctly and would prevent descending into child nodes. Now it seems like the logic is inverted - children are being visited when `SKIP` is returned instead of being skipped.

---
Repository: /testbed
