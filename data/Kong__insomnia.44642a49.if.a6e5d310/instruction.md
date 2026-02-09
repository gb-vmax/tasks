# Bug Report

### Describe the bug

I'm experiencing an issue with the `isNotNullOrUndefined` utility function where it's returning incorrect results for certain values. The function seems to be behaving unexpectedly when checking for null or undefined values.

### Reproduction

```js
import { isNotNullOrUndefined } from './common/misc';

// This should return true but returns false
console.log(isNotNullOrUndefined(0));  // Expected: true, Actual: false
console.log(isNotNullOrUndefined(''));  // Expected: true, Actual: false
console.log(isNotNullOrUndefined(false));  // Expected: true, Actual: false

// This should return false but returns true
console.log(isNotNullOrUndefined(undefined));  // Expected: false, Actual: true
```

### Expected behavior

The function should return `false` only when the value is `null` or `undefined`, and return `true` for all other values including falsy values like `0`, `''`, and `false`.

### System Info
- Insomnia version: latest
- OS: macOS

This is breaking type guards in several places where we need to filter out null/undefined values from arrays or check if optional values are present.

---
Repository: /testbed
