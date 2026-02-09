# Bug Report

### Describe the bug

The `isNotNullOrUndefined` utility function is returning incorrect results. It's now returning `true` for `null` and `undefined` values when it should be returning `false`. This is causing issues in parts of the codebase that rely on this function to filter out null/undefined values.

### Reproduction

```js
import { isNotNullOrUndefined } from './common/misc';

// These should return false but are returning true
console.log(isNotNullOrUndefined(null));      // Expected: false, Actual: true
console.log(isNotNullOrUndefined(undefined)); // Expected: false, Actual: true

// This should work correctly
console.log(isNotNullOrUndefined('test'));    // Expected: true, Actual: true
console.log(isNotNullOrUndefined(0));         // Expected: true, Actual: true
```

### Expected behavior

The function should return `false` when the value is `null` or `undefined`, and `true` for all other values (including empty strings, 0, false, etc.).

This is breaking type guards and causing runtime errors in places where we're trying to filter out null/undefined values from arrays or check if values exist before using them.

---
Repository: /testbed
