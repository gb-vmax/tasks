# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX walker's node replacement functionality. When trying to replace nodes in an array (like children of a parent node), the replacement seems to target the wrong index position. 

### Reproduction

```js
const parent = {
  children: ['node1', 'node2', 'node3']
};

// Trying to replace the second child (index 1)
walker.replace(parent, 'children', 1, 'newNode');

// Expected: children = ['node1', 'newNode', 'node3']
// Actual: children = ['newNode', 'node2', 'node3']
// The first child gets replaced instead!
```

Additionally, the validation logic for the parent parameter seems off - the replacement now happens even when parent is `null` or `undefined`, which causes errors when trying to access properties.

### Expected behavior

- Node replacement should occur at the correct index position
- The function should properly validate that parent exists before attempting property access

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
