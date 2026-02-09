# Bug Report

### Describe the bug

I'm experiencing an issue where the tree visitor is not calling the visitor function on any nodes when a test/filter is provided. The visitor function only gets invoked when no test parameter is passed, but when I specify a test function to filter which nodes to visit, nothing happens at all.

### Reproduction

```js
import { visit } from 'unist-util-visit';

const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', children: [] },
    { type: 'heading', children: [] }
  ]
};

let visitedNodes = [];

// This doesn't visit any nodes
visit(tree, 'paragraph', (node) => {
  visitedNodes.push(node.type);
});

console.log(visitedNodes); // Expected: ['paragraph'], Actual: []

// Also doesn't work with a test function
visit(tree, (node) => node.type === 'heading', (node) => {
  visitedNodes.push(node.type);
});

console.log(visitedNodes); // Expected: ['heading'], Actual: []
```

### Expected behavior

When providing a test parameter (either a string type or a test function), the visitor should be called on matching nodes. Currently it seems like the visitor is never invoked when a test is specified.

### Additional context

This appears to have started happening recently. Without any test parameter, the visitor works fine and visits all nodes, but as soon as I try to filter nodes using the test parameter, nothing gets visited.

---
Repository: /testbed
