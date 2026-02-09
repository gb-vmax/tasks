# Bug Report

### Describe the bug

The `visit()` function is not correctly handling the visitor callback arguments when called with a test function, visitor function, and reverse parameter. The parent node being passed to the visitor callback appears to be incorrect.

### Reproduction

```js
import { visit } from 'unist-util-visit';

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
};

visit(
  tree,
  'text',
  (node, index, parent) => {
    console.log('Parent type:', parent?.type);
    // Expected: 'paragraph'
    // Actual: undefined or wrong parent
  },
  false
);
```

When visiting nodes with a test parameter, the parent argument passed to the visitor callback doesn't match the actual parent of the current node. It seems like the wrong element from the parents array is being selected.

### Expected behavior

The visitor callback should receive the correct parent node as its third argument. For a text node inside a paragraph, the parent should be the paragraph node, not undefined or some other ancestor.

### System Info
- Node version: 18.x
- unist-util-visit version: 5.0.0

---
Repository: /testbed
