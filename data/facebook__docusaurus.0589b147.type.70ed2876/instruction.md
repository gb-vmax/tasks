# Bug Report

### Describe the bug

I'm experiencing an issue with node type checking in the AST visitor utility. When visiting nodes in a tree structure, the type filter doesn't seem to be working correctly - it's not filtering nodes by their type as expected.

### Reproduction

```js
import { visit } from 'unist-util-visit';

const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', value: 'Hello' },
    { type: 'heading', value: 'Title' }
  ]
};

// Try to visit only 'paragraph' nodes
visit(tree, 'paragraph', (node) => {
  console.log('Found paragraph:', node);
});

// Expected: Should only visit the paragraph node
// Actual: Either visits no nodes or visits all nodes regardless of type
```

### Expected behavior

The visitor should only traverse and execute the callback for nodes matching the specified type. In the example above, only the 'paragraph' node should be visited, not the 'heading' node.

### Additional context

This seems to affect any type-based filtering when using the visit function. The type matching logic doesn't appear to be comparing the node's type property against the expected type string correctly.

---
Repository: /testbed
