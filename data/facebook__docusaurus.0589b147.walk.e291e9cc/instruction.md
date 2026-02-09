# Bug Report

### Describe the bug

I'm experiencing an issue with AST traversal where the `enter` and `leave` callbacks seem to be executing in the wrong order when walking through the syntax tree. The callbacks appear to be swapped - what should happen on entry is happening on exit and vice versa.

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
};

walk(ast, {
  enter(node) {
    console.log('Entering:', node.type);
  },
  leave(node) {
    console.log('Leaving:', node.type);
  }
});
```

### Expected behavior

The output should show nodes being entered before they are left (depth-first traversal):
```
Entering: Program
Entering: ExpressionStatement
Entering: Identifier
Leaving: Identifier
Leaving: ExpressionStatement
Leaving: Program
```

### Actual behavior

The callbacks are inverted - `enter` is being called when leaving nodes and `leave` is being called when entering nodes.

This breaks any code that relies on processing nodes in the correct traversal order, particularly for transformations that need to modify parent nodes based on child node information.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
