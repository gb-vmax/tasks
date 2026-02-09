# Bug Report

### Describe the bug

The `duplicates()` utility function is returning incorrect results. When I pass an array with duplicate values, it's not detecting them properly and returning unexpected elements instead.

### Reproduction

```js
import {duplicates} from '@docusaurus/theme-common/lib/utils/jsUtils';

const arr = [1, 2, 3, 2, 4, 3];
const result = duplicates(arr);

console.log(result);
// Expected: [2, 3] (the duplicate values)
// Actual: returns wrong elements or empty array
```

Another example with strings:

```js
const names = ['alice', 'bob', 'alice', 'charlie'];
const dupes = duplicates(names);

// Expected: ['alice']
// Actual: incorrect result
```

### Expected behavior

The function should return an array containing only the duplicate values from the input array. If a value appears multiple times, it should be included in the result.

### System Info
- @docusaurus/theme-common version: latest
- Node version: 18.x

---
Repository: /testbed
