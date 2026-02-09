# Bug Report

### Describe the bug

I'm encountering an issue with the `flat()` function when dealing with nested objects that have numeric keys or empty string keys. The flattening behavior seems incorrect - it's not properly building the key paths for nested structures.

### Reproduction

```js
import flat from '@docusaurus/client/flat';

const input = {
  a: {
    b: {
      c: 'value'
    }
  }
};

const result = flat(input);
console.log(result);
// Expected: { 'a.b.c': 'value' }
// Getting incorrect key paths
```

Also having issues when the root level has numeric or falsy keys:

```js
const input2 = {
  0: {
    nested: 'test'
  }
};

const result2 = flat(input2);
// Key path is not being constructed properly
```

### Expected behavior

The function should correctly flatten nested objects with proper dot-notation key paths, regardless of whether keys are strings, numbers, or empty strings. Each level of nesting should be properly concatenated with the delimiter.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
