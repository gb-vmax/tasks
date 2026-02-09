# Bug Report

### Describe the bug

The `flat()` function is not correctly flattening nested objects with multiple levels. When flattening deeply nested structures, the key paths are being truncated and don't include all parent keys in the path.

### Reproduction

```js
import flat from '@docusaurus/client/flat';

const chunkNames = {
  component: {
    nested: {
      deep: 'value1'
    }
  }
};

const result = flat(chunkNames);
console.log(result);
// Current output: { 'nested.deep': 'value1' }
// Expected output: { 'component.nested.deep': 'value1' }
```

The function is dropping the top-level key `component` from the flattened path. This breaks when you have multiple top-level keys with the same nested structure, as they would collide.

### Expected behavior

The flattened object should preserve the full key path from root to leaf, with all intermediate keys separated by the delimiter (`.`). For example:
- Input: `{ a: { b: { c: 'value' } } }`
- Expected: `{ 'a.b.c': 'value' }`
- Actual: `{ 'b.c': 'value' }`

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
