# Bug Report

### Describe the bug

When using the tree visitor utility, the traversal stops prematurely when the visitor callback returns `EXIT`. The visitor is supposed to stop traversal and return when `EXIT` is encountered, but instead it appears to continue visiting nodes or return early in unexpected cases.

### Reproduction

```js
import { visit } from 'unist-util-visit';

const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [
        { type: 'text', value: 'first' },
        { type: 'text', value: 'second' }
      ]
    },
    {
      type: 'paragraph',
      children: [
        { type: 'text', value: 'third' }
      ]
    }
  ]
};

let visitedNodes = [];

visit(tree, 'text', (node) => {
  visitedNodes.push(node.value);
  if (node.value === 'first') {
    return [EXIT]; // Should stop traversal here
  }
});

console.log(visitedNodes);
// Expected: ['first']
// Actual: All nodes are visited or traversal behaves incorrectly
```

### Expected behavior

When a visitor returns `EXIT`, the traversal should immediately stop and no further nodes should be visited. The function should return the EXIT result.

### System Info

- unist-util-visit version: 5.0.0
- Node.js version: 18.x

---
Repository: /testbed
