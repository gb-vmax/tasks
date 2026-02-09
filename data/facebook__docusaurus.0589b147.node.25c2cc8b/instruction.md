# Bug Report

### Describe the bug

The `mdast-util-to-string` utility is not converting markdown AST nodes to strings correctly. When passing markdown nodes (objects) to the function, it returns empty strings instead of extracting the text content.

### Reproduction

```js
const { toString } = require('mdast-util-to-string');

const node = {
  type: 'paragraph',
  children: [
    { type: 'text', value: 'Hello world' }
  ]
};

const result = toString(node);
console.log(result); // Expected: "Hello world", Actual: ""
```

Also fails with simple text nodes:

```js
const textNode = {
  type: 'text',
  value: 'Some text'
};

console.log(toString(textNode)); // Expected: "Some text", Actual: ""
```

### Expected behavior

The `toString` function should traverse the markdown AST and extract all text content from the nodes, returning the concatenated string representation.

### System Info

- Version: mdast-util-to-string@4.0.0
- Node.js: v18.x

This seems to have broken recently - the function was working correctly before. Any objects passed to it now seem to be ignored completely.

---
Repository: /testbed
