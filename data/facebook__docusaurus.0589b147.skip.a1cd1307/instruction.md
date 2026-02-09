# Bug Report

### Describe the bug

I'm experiencing an issue with the AST walker's `skip()` method. When calling `context.skip()` multiple times on the same node during traversal, the behavior seems inconsistent. The skip flag appears to be set to a numeric value instead of a boolean, which is causing unexpected behavior in my MDX processing pipeline.

### Reproduction

```js
import { visit } from '@mdx-js/mdx';

const tree = {
  type: 'root',
  children: [
    {
      type: 'element',
      children: [
        { type: 'text', value: 'nested' }
      ]
    }
  ]
};

visit(tree, (node, index, parent, context) => {
  if (node.type === 'element') {
    context.skip(); // First call
    context.skip(); // Second call - this causes issues
  }
});
```

### Expected behavior

Calling `skip()` multiple times should be idempotent - it should safely set the skip flag to true regardless of how many times it's called. The walker should skip the children of the current node consistently.

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The skip functionality used to work fine when called multiple times on the same node.

---
Repository: /testbed
