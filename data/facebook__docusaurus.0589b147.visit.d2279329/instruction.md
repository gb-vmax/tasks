# Bug Report

### Describe the bug

The `visit` function from `unist-util-visit` is not working properly. When trying to use it, I get an error that it's not a function or it doesn't behave as expected.

### Reproduction

```js
const { visit } = require('unist-util-visit');

const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', children: [] }
  ]
};

// This doesn't work anymore
visit(tree, 'paragraph', (node) => {
  console.log(node);
});
```

### Expected behavior

The `visit` function should traverse the tree and execute the visitor callback for matching nodes. It should work as documented in the unist-util-visit API.

### Additional context

This seems to have broken recently. The function is exported but calling it directly throws an error or requires an extra invocation which doesn't make sense based on the API.

---
Repository: /testbed
