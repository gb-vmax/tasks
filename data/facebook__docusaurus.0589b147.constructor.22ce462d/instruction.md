# Bug Report

### Describe the bug

I'm encountering an issue with the AST walker where nodes are being skipped unexpectedly during traversal. It seems like the walker is not visiting all nodes in the tree as it should.

### Reproduction

```js
import { walk } from '@mdx-js/mdx';

const ast = {
  type: 'root',
  children: [
    { type: 'paragraph', children: [{ type: 'text', value: 'Hello' }] },
    { type: 'paragraph', children: [{ type: 'text', value: 'World' }] }
  ]
};

const visited = [];
walk(ast, {
  enter(node) {
    visited.push(node.type);
  }
});

console.log(visited);
// Expected: ['root', 'paragraph', 'text', 'paragraph', 'text']
// Actual: Only 'root' is visited, children are skipped
```

### Expected behavior

The walker should traverse all nodes in the AST tree by default. All child nodes should be visited unless explicitly skipped using the `skip()` context method.

### Additional context

This appears to have started recently. The walker seems to be skipping child nodes by default instead of traversing them, which breaks any code that relies on visiting all nodes in the tree.

---
Repository: /testbed
