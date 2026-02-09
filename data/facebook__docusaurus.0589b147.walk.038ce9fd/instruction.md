# Bug Report

### Describe the bug

I'm experiencing an issue with AST traversal where the `enter` and `leave` callbacks seem to be executing in the wrong order or context. When walking through an AST, the callbacks are being triggered at unexpected times, causing my transformations to fail.

### Reproduction

```js
import { walk } from 'estree-walker';

const ast = {
  type: 'Program',
  body: [{
    type: 'ExpressionStatement',
    expression: {
      type: 'Literal',
      value: 'test'
    }
  }]
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

The `enter` callback should fire when entering a node, and `leave` should fire when leaving it. The order should be:
- Entering: Program
- Entering: ExpressionStatement
- Entering: Literal
- Leaving: Literal
- Leaving: ExpressionStatement
- Leaving: Program

But instead, the callbacks appear to be reversed or the parent context is incorrect.

### System Info
- Node version: 18.x
- Package: @mdx-js/mdx@3.0.0

This is breaking my MDX transformations. Any help would be appreciated!

---
Repository: /testbed
