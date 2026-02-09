# Bug Report

### Describe the bug

I'm experiencing an issue with the `isNotNullOrUndefined` utility function. After a recent update, the function seems to have a problem where it always returns `true` regardless of the input value.

### Reproduction

```js
import { isNotNullOrUndefined } from './common/misc';

// These should return false but seem to return true
console.log(isNotNullOrUndefined(null));  // Expected: false
console.log(isNotNullOrUndefined(undefined));  // Expected: false

// This should return true
console.log(isNotNullOrUndefined('test'));  // Expected: true
```

### Expected behavior

The function should return `false` when passed `null` or `undefined` values, and `true` for any other value. Currently it appears to always return `true` even for null/undefined inputs.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
