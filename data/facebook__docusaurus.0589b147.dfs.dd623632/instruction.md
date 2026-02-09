# Bug Report

### Describe the bug

The `flat()` function is producing incorrect output when flattening nested objects. The flattened keys are not being constructed properly, and the logic for determining when to recurse versus when to add values to the output seems to be inverted.

### Reproduction

```js
import flat from '@docusaurus/core/lib/client/flat';

const chunkNames = {
  component: {
    nested: {
      deep: 'value1'
    },
    shallow: 'value2'
  },
  simple: 'value3'
};

const result = flat(chunkNames);
console.log(result);

// Expected output:
// {
//   'component.nested.deep': 'value1',
//   'component.shallow': 'value2',
//   'simple': 'value3'
// }

// Actual output is incorrect - the keys are malformed and values are in wrong places
```

### Expected behavior

The function should recursively flatten nested objects and create dot-delimited keys that represent the full path to each leaf value. Non-object values should be added to the output with their complete path as the key.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
