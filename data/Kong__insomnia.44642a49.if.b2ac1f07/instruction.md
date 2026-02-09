# Bug Report

### Describe the bug

The `isNotNullOrUndefined` utility function is returning incorrect results. It's supposed to filter out null and undefined values, but it's doing the opposite - it returns `true` for null/undefined values and still returns `true` for valid values.

### Reproduction

```js
import { isNotNullOrUndefined } from './common/misc';

// These should return false but return true
console.log(isNotNullOrUndefined(null));      // Expected: false, Actual: true
console.log(isNotNullOrUndefined(undefined)); // Expected: false, Actual: true

// These correctly return true
console.log(isNotNullOrUndefined('test'));    // Expected: true, Actual: true
console.log(isNotNullOrUndefined(0));         // Expected: true, Actual: true
console.log(isNotNullOrUndefined(false));     // Expected: true, Actual: true
```

When using this function to filter arrays, all elements are kept including null/undefined:

```js
const items = ['a', null, 'b', undefined, 'c'];
const filtered = items.filter(isNotNullOrUndefined);
console.log(filtered); // Expected: ['a', 'b', 'c'], Actual: ['a', null, 'b', undefined, 'c']
```

### Expected behavior

The function should return `false` for null or undefined values and `true` for all other values, allowing it to be used as a type guard to filter out nullish values.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
