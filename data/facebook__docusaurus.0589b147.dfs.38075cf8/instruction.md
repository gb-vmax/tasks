# Bug Report

### Describe the bug

The `flat()` function is producing incorrect output when flattening nested objects. It seems like the flattening logic is inverted - leaf values are being treated as objects to recurse into, while actual nested objects are being added directly to the output.

### Reproduction

```js
import flat from '@docusaurus/client/flat';

const input = {
  a: {
    b: {
      c: 'value1'
    }
  },
  x: 'value2'
};

const result = flat(input);
console.log(result);
// Expected: { 'a.b.c': 'value1', 'x': 'value2' }
// Actual: Objects are not flattened correctly
```

When I try to flatten a nested object structure, the resulting object doesn't have the correct key paths. Instead of creating dot-notation keys for deeply nested values, it appears to be doing the opposite of what it should.

### Expected behavior

The function should recursively traverse nested objects and create flattened keys using dot notation. Leaf values (strings, numbers, etc.) should be assigned to their full dot-notated path, while nested objects should be recursed into further.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
