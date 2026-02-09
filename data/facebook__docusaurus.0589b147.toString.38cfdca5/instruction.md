# Bug Report

### Describe the bug

After a recent update, the `toString` function from `mdast-util-to-string` is no longer working correctly. When trying to use it to convert markdown AST nodes to strings, I'm getting a function reference instead of the actual string output.

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
console.log(result); // Expected: "Hello world", but getting something else
```

### Expected behavior

The `toString` function should convert the markdown AST node to its string representation. In the example above, it should return `"Hello world"`.

### System Info
- Node version: 18.x
- Package: mdast-util-to-string@4.0.0

---
Repository: /testbed
