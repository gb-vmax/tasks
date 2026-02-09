# Bug Report

### Describe the bug

The `visit` function from `unist-util-visit` is not working as expected. When trying to use it to traverse AST nodes, the function appears to be broken and doesn't actually perform any traversal operations.

### Reproduction

```js
const { visit } = require('unist-util-visit');

const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [{ type: 'text', value: 'hello' }]
    }
  ]
};

visit(tree, 'text', (node) => {
  console.log(node.value); // Expected to print 'hello', but nothing happens
});
```

### Expected behavior

The visitor function should be called for each matching node in the tree. In this example, it should log `'hello'` to the console when visiting the text node.

### Additional context

This seems to have broken recently. The `visit` function doesn't traverse the tree at all anymore. Not sure if this is related to recent changes in the vendored dependencies.

---
Repository: /testbed
