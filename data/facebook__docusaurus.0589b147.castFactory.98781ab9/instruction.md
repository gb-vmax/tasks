# Bug Report

### Describe the bug

I'm experiencing an issue with tree traversal where non-node values are being incorrectly processed. When visiting a tree structure, the visitor function seems to be called on values that shouldn't be treated as nodes, and the parent parameter passed to the test function appears to be inverted.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [
        { type: 'text', value: 'Hello' }
      ]
    }
  ]
}

visit(tree, (node, index, parent) => {
  // Visitor is being called with non-node values
  // Parent parameter seems to have wrong value
  console.log('Node:', node)
  console.log('Parent:', parent)
})
```

### Expected behavior

The visitor function should only be invoked for actual tree nodes (objects with a `type` property), and the parent parameter should correctly reference the parent node when it exists, or be undefined when there is no parent.

Currently it seems like:
1. Non-node values are being passed to the test function when they shouldn't be
2. The parent parameter logic is reversed - it's undefined when a parent exists and has the parent value when it should be undefined

### System Info
- unist-util-visit version: 5.0.0
- Node.js version: 18.x

---
Repository: /testbed
