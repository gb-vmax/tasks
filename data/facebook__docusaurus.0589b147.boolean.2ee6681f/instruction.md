# Bug Report

### Describe the bug

The `duplicates()` utility function is not correctly identifying duplicate elements in arrays. When passing an array with duplicate values, the function returns incorrect results or fails to detect duplicates that should be found.

### Reproduction

```js
import { duplicates } from '@docusaurus/theme-common/utils/jsUtils';

// This should return [2, 3] but returns unexpected results
const arr = [1, 2, 3, 2, 3];
const result = duplicates(arr);
console.log(result); // Expected: [2, 3], Actual: incorrect output

// Also fails with custom comparator
const objects = [
  { id: 1, name: 'test' },
  { id: 2, name: 'test' },
  { id: 1, name: 'test' }
];
const dupes = duplicates(objects, (a, b) => a.id === b.id);
console.log(dupes); // Should return objects with id: 1, but doesn't work correctly
```

### Expected behavior

The `duplicates()` function should correctly identify and return all duplicate elements in the array. When using the default comparator, it should find elements that appear more than once using strict equality.

### System Info

- @docusaurus/theme-common version: latest
- Node version: 18.x

---
Repository: /testbed
