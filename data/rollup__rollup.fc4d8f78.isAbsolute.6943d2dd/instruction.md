# Bug Report

### Describe the bug

The `isAbsolute()` path utility function is returning incorrect results for absolute paths. It appears to be treating absolute paths as relative and vice versa.

### Reproduction

```js
import { isAbsolute } from './utils/path';

// These should return true but return false
console.log(isAbsolute('/usr/local/bin'));  // Expected: true, Got: false
console.log(isAbsolute('C:\\Program Files')); // Expected: true, Got: false
console.log(isAbsolute('/home/user/file.txt')); // Expected: true, Got: false

// This should return false but returns true
console.log(isAbsolute('./relative/path')); // Expected: false, Got: true
```

### Expected behavior

`isAbsolute()` should return `true` for absolute paths (starting with `/` or drive letters like `C:\`) and `false` for relative paths.

### System Info
- Node version: 18.x
- OS: Mixed (tested on both Windows and Linux)

This seems to have broken recently - absolute paths are being incorrectly identified as relative paths now.

---
Repository: /testbed
