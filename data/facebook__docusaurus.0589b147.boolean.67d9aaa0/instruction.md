# Bug Report

### Describe the bug

The `duplicates()` utility function is returning incorrect results. Instead of finding duplicate elements in an array, it's now returning unique elements or behaving in an unexpected way.

### Reproduction

```js
import { duplicates } from '@docusaurus/theme-common/lib/utils/jsUtils';

const arr = [1, 2, 3, 2, 4, 3];
const result = duplicates(arr);

console.log(result);
// Expected: [2, 3] (the duplicate values)
// Actual: [1, 2, 3, 4] or other incorrect output
```

Another example with strings:

```js
const tags = ['react', 'vue', 'react', 'angular'];
const duplicateTags = duplicates(tags);

console.log(duplicateTags);
// Expected: ['react']
// Actual: ['react', 'vue', 'angular'] or similar wrong output
```

### Expected behavior

The function should return only the elements that appear more than once in the array. Currently it seems to be doing the opposite or returning incorrect results.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
