# Bug Report

### Describe the bug

The `visit` function from `unist-util-visit` is not accessible or throws an error when trying to use it. It seems like the export is broken and the function cannot be called properly.

### Reproduction

```js
const { visit } = require('unist-util-visit');

const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', children: [] }
  ]
};

// This fails - visit is not a function or is undefined
visit(tree, 'paragraph', (node) => {
  console.log(node);
});
```

### Expected behavior

The `visit` function should be exported correctly and work as documented. It should traverse the tree and call the visitor function for matching nodes.

### System Info
- Version: 5.0.0
- Environment: Node.js

---
Repository: /testbed
