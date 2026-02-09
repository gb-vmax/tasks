# Bug Report

### Describe the bug

I'm experiencing an issue with the `visit` function where the parent node being passed to the visitor callback is incorrect. Instead of receiving the immediate parent of the current node, I'm getting the grandparent (parent's parent).

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

visit(tree, 'text', (node, index, parent) => {
  console.log('Node:', node.value);
  console.log('Parent type:', parent.type);
  // Expected: parent.type should be 'paragraph'
  // Actual: parent.type is 'root'
});
```

### Expected behavior

When visiting a text node that is a child of a paragraph, the `parent` parameter in the visitor callback should be the paragraph node (the immediate parent). However, it's returning the root node (the grandparent) instead.

This breaks any logic that depends on accessing the correct parent node during tree traversal.

### System Info
- unist-util-visit version: 5.0.0
- Node.js version: Latest

---
Repository: /testbed
