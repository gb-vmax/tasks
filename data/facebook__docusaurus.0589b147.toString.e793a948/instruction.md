# Bug Report

### Describe the bug

I'm getting an error when trying to use the `toString` function from `mdast-util-to-string`. It seems like the export is broken and I'm getting `undefined` when trying to import it.

### Reproduction

```js
const { toString } = require('mdast-util-to-string');

const tree = {
  type: 'paragraph',
  children: [
    { type: 'text', value: 'Hello world' }
  ]
};

console.log(toString(tree));
// TypeError: toString is not a function
```

### Expected behavior

The `toString` function should be properly exported and callable. It should convert the mdast tree to a string representation.

### Additional context

This might be related to a recent change in the export statement. The function appears to be exported incorrectly.

---
Repository: /testbed
