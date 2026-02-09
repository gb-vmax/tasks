# Bug Report

### Describe the bug

I'm experiencing an issue with MDX tree traversal where the visitor function seems to be incorrectly visiting child nodes even when I explicitly skip them. When I return a SKIP action from a visitor callback, the children are still being traversed instead of being skipped as expected.

### Reproduction

```js
import {visitParents} from '@mdx-js/mdx'

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

const visited = []

visitParents(tree, (node) => {
  visited.push(node.type)
  
  // When we encounter 'parent', skip its children
  if (node.type === 'parent') {
    return ['skip']
  }
})

// Expected: ['root', 'parent']
// Actual: ['root', 'parent', 'child1', 'child2']
console.log(visited)
```

The children are being visited even though I returned the SKIP action. This breaks my use case where I need to conditionally skip entire subtrees during traversal.

### Expected behavior

When the visitor returns a SKIP action for a node, its children should not be visited. The traversal should continue with the next sibling instead.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
