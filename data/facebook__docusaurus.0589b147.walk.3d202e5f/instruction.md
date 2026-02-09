# Bug Report

### Describe the bug

I'm experiencing an issue with AST traversal where the `enter` and `leave` callbacks are being invoked in the wrong order during tree walking. When I provide an `enter` callback and a `leave` callback to the walker, they seem to be swapped - the `leave` callback is being called when entering nodes, and the `enter` callback is being called when leaving nodes.

### Reproduction

```js
const ast = {
  type: 'Program',
  body: [
    {
      type: 'ExpressionStatement',
      expression: { type: 'Literal', value: 42 }
    }
  ]
};

const visited = [];

walk(ast, {
  enter(node) {
    visited.push(`enter: ${node.type}`);
  },
  leave(node) {
    visited.push(`leave: ${node.type}`);
  }
});

console.log(visited);
// Expected: ['enter: Program', 'enter: ExpressionStatement', 'enter: Literal', 'leave: Literal', 'leave: ExpressionStatement', 'leave: Program']
// Actual: ['leave: Program', 'leave: ExpressionStatement', 'leave: Literal', 'enter: Literal', 'enter: ExpressionStatement', 'enter: Program']
```

The callbacks are being executed in reverse order - what should be `enter` is behaving like `leave` and vice versa.

### Expected behavior

The `enter` callback should be called when entering a node (pre-order), and the `leave` callback should be called when exiting a node (post-order). The traversal order should follow standard depth-first traversal semantics.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
