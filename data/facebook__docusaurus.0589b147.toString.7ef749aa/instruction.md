# Bug Report

### Describe the bug

After a recent update, the `toString` export from `mdast-util-to-string` is not working as expected. When I try to import and use `toString`, I'm getting `undefined` instead of the actual function.

### Reproduction

```js
const { toString } = require('mdast-util-to-string');

const node = {
  type: 'text',
  value: 'Hello world'
};

// This returns undefined instead of the string
const result = toString(node);
console.log(result); // undefined
```

### Expected behavior

The `toString` function should be properly exported and callable. It should return the string representation of the mdast node, not `undefined`.

### Additional context

This seems to have started happening in the latest version. The function used to work fine when called directly. Now it appears the export itself is broken somehow.

---
Repository: /testbed
