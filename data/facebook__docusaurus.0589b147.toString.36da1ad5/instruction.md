# Bug Report

### Describe the bug

The `toString` export from `mdast-util-to-string` appears to be broken. When trying to import and use the function, I'm getting errors that it's not available or not working as expected.

### Reproduction

```js
const { toString } = require('./jest/vendor/mdast-util-to-string@4.0.0.js');

// Trying to use toString fails
const result = toString(someNode);
```

### Expected behavior

The `toString` function should be properly exported and callable. It should convert mdast nodes to string representation as documented.

### Additional context

This seems to have broken recently. The export might be misconfigured or the function name is incorrect in the module exports.

---
Repository: /testbed
