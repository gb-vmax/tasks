# Bug Report

### Describe the bug
I'm encountering an issue with the `mdast-util-to-string` vendor module where calling the exported `toString` function results in an error. It seems like the export is not pointing to the actual function anymore.

### Reproduction
```js
const { toString } = require('./jest/vendor/mdast-util-to-string@4.0.0.js');

const node = {
  type: 'text',
  value: 'Hello world'
};

// This throws an error
const result = toString(node);
```

### Expected behavior
The `toString` function should be callable and convert the mdast node to a string representation. Instead, I'm getting a `TypeError` indicating that the function is not defined or not callable.

### System Info
- Node version: Latest
- Module: mdast-util-to-string@4.0.0 (vendored)

This seems to have broken recently. The function used to work fine before.

---
Repository: /testbed
