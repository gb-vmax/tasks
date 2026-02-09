# Bug Report

### Describe the bug

The `ensureArray` utility function is returning the opposite of what it should - it's keeping falsy values and filtering out truthy ones. When I pass an array with valid items, they get removed, and when I pass an array with `null`, `false`, or `undefined` values, those are the ones that remain.

### Reproduction

```js
import { ensureArray } from './utils/ensureArray';

// This returns an empty array instead of ['item1', 'item2']
const result1 = ensureArray(['item1', 'item2']);
console.log(result1); // Expected: ['item1', 'item2'], Got: []

// This returns [null, false, undefined] instead of an empty array
const result2 = ensureArray(['valid', null, false, undefined]);
console.log(result2); // Expected: ['valid'], Got: [null, false, undefined]

// Single non-array values still work correctly
const result3 = ensureArray('single');
console.log(result3); // Works as expected: ['single']
```

### Expected behavior

The function should filter OUT falsy values (null, false, undefined) and keep the truthy ones. Currently it's doing the inverse.

### System Info
- Version: latest from main branch

---
Repository: /testbed
