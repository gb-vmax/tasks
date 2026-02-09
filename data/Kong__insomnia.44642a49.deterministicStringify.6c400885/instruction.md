# Bug Report

### Describe the bug

The `deterministicStringify` function is producing incorrect output for both objects and arrays. When stringifying objects, the key order appears to be reversed from what's expected, and for arrays, the first element is being skipped entirely.

### Reproduction

```js
import { deterministicStringify } from './deterministicStringify';

// Object stringification issue
const obj = { a: 1, b: 2, c: 3 };
const result = deterministicStringify(obj);
console.log(result);
// Expected: {"a":1,"b":2,"c":3}
// Actual: {"c":3,"b":2,"a":1}

// Array stringification issue
const arr = [1, 2, 3, 4];
const arrResult = deterministicStringify(arr);
console.log(arrResult);
// Expected: [1,2,3,4]
// Actual: [2,3,4] (first element missing!)
```

### Expected behavior

- Objects should be stringified with keys in alphabetical order (a, b, c)
- Arrays should include ALL elements, not skip the first one

This is breaking sync functionality as the deterministic stringify is supposed to produce consistent, predictable output for comparison purposes.

### System Info
- Package: @insomnia/sync
- Node version: 18.x

---
Repository: /testbed
