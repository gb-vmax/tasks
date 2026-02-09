# Bug Report

### Describe the bug

I'm encountering an issue where the tree visitor is attempting to access child nodes beyond the valid array bounds. When iterating through children of a node, the visitor tries to access an index that equals the array length, which results in accessing `undefined` instead of properly terminating the loop.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'child1' },
    { type: 'child2' },
    { type: 'child3' }
  ]
};

visit(tree, (node) => {
  // Visitor function
  console.log(node.type);
});

// The visitor attempts to access children[3] when the array only has indices 0-2
```

### Expected behavior

The visitor should only iterate through valid child indices (0 to `children.length - 1`). It should not attempt to access an index equal to the array length, as this will always be `undefined` in JavaScript arrays.

### System Info

- unist-util-visit version: 5.0.0
- Node version: Latest

The loop condition should prevent accessing indices outside the valid range of the children array. Currently it's allowing iteration to an out-of-bounds index.

---
Repository: /testbed
