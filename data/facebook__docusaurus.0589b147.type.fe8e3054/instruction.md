# Bug Report

### Describe the bug

I'm experiencing an issue with the `unist-util-visit` library where nodes are not being visited correctly when filtering by type. It seems like the type checking logic is inverted - nodes that should match a specific type are being skipped, while nodes that don't match are being visited instead.

### Reproduction

```js
import { visit } from 'unist-util-visit';

const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', value: 'Hello' },
    { type: 'heading', value: 'Title' },
    { type: 'paragraph', value: 'World' }
  ]
};

const visited = [];

// Try to visit only 'paragraph' nodes
visit(tree, 'paragraph', (node) => {
  visited.push(node);
});

console.log(visited);
// Expected: 2 paragraph nodes
// Actual: All non-paragraph nodes are visited instead
```

### Expected behavior

When calling `visit(tree, 'paragraph', callback)`, only nodes with `type: 'paragraph'` should be passed to the callback function. Currently, it appears to be doing the opposite - visiting everything except paragraph nodes.

### System Info

- unist-util-visit version: 5.0.0
- Node.js version: 18.x

---
Repository: /testbed
