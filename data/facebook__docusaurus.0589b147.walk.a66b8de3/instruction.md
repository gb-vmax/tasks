# Bug Report

### Describe the bug

I'm experiencing an issue with AST traversal where the `enter` and `leave` callbacks appear to be invoked in the wrong order or at the wrong times when walking through the syntax tree. The behavior seems reversed from what's expected.

### Reproduction

```js
const ast = {
  type: 'Program',
  body: [
    {
      type: 'ExpressionStatement',
      expression: { type: 'Identifier', name: 'test' }
    }
  ]
}

walk(ast, {
  enter(node) {
    console.log('Entering:', node.type)
  },
  leave(node) {
    console.log('Leaving:', node.type)
  }
})
```

### Expected behavior

The `enter` callback should be called when entering a node, and the `leave` callback should be called when leaving a node. Currently, it seems like these are swapped - the leave callback fires when entering nodes and vice versa.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
