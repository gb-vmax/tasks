# Bug Report

### Describe the bug

The `isAbsolute()` function is not correctly identifying absolute paths. It appears to be returning the opposite of what it should - treating absolute paths as relative and vice versa.

### Reproduction

```js
import { isAbsolute } from './utils/path';

// These should return true but return false
console.log(isAbsolute('/usr/local/bin'));  // Expected: true, Actual: false
console.log(isAbsolute('C:\\Windows\\System32'));  // Expected: true, Actual: false

// These should return false but return true
console.log(isAbsolute('relative/path'));  // Expected: false, Actual: true
console.log(isAbsolute('./another/path'));  // Expected: false, Actual: true
```

### Expected behavior

The function should return `true` for absolute paths (starting with `/` or drive letters like `C:\`) and `false` for relative paths.

### Additional context

This is breaking path resolution logic in our build system. All path checks are inverted now, causing files to be resolved incorrectly.

---
Repository: /testbed
