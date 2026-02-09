# Bug Report

### Describe the bug

I'm experiencing an issue with the `EXIT` constant exported from `unist-util-visit`. When trying to use it to control tree traversal, it's not working as expected. The visitor continues traversing the tree even after returning `EXIT`.

### Reproduction

```js
import { visit, EXIT } from 'unist-util-visit';

const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', value: 'first' },
    { type: 'paragraph', value: 'second' }
  ]
};

visit(tree, 'paragraph', (node) => {
  console.log(node.value);
  return EXIT; // Should stop traversal here
});

// Expected: Only logs 'first'
// Actual: Logs both 'first' and 'second'
```

### Expected behavior

When returning `EXIT` from a visitor function, the traversal should immediately stop and no further nodes should be visited. The constant should be directly comparable with the return value to control flow.

### Additional context

This seems to have broken recently. Previously `EXIT` was a simple constant that could be returned to halt traversal, but now it doesn't seem to be recognized properly by the visit function's control flow logic.

---
Repository: /testbed
