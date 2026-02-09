# Bug Report

### Describe the bug

I'm encountering an issue with HTML nodes in the markdown AST. When creating HTML nodes, the `value` property is now `undefined` instead of an empty string, which breaks compatibility with code that expects `value` to always be a string.

### Reproduction

```js
const processor = remark();
const tree = processor.parse('some markdown');

// Traverse the tree to find HTML nodes
visit(tree, 'html', (node) => {
  console.log(typeof node.value); // Expected: 'string', Actual: 'undefined'
  console.log(node.value.length); // TypeError: Cannot read property 'length' of undefined
});
```

### Expected behavior

The `value` property of HTML nodes should be an empty string `""` when there's no content, not `undefined`. This maintains backwards compatibility and follows the expected node structure where `value` is always a string type.

### Additional context

This appears to have changed recently. My code that processes markdown AST nodes is now throwing errors when trying to access string methods on the `value` property of HTML nodes.

---
Repository: /testbed
