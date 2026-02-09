# Bug Report

### Describe the bug

I'm experiencing an issue with path resolution where absolute paths are being incorrectly identified as relative paths. This is causing problems when trying to import modules using absolute paths.

### Reproduction

```js
import { isAbsolute } from './utils/path';

// This should return true but returns false
console.log(isAbsolute('/usr/local/bin'));  // Expected: true, Got: false

// Same issue with Windows-style paths
console.log(isAbsolute('C:/Program Files'));  // Expected: true, Got: false

// Even simple root paths fail
console.log(isAbsolute('/'));  // Works correctly (returns true)
console.log(isAbsolute('/home'));  // Expected: true, Got: false
```

### Expected behavior

The `isAbsolute()` function should return `true` for all absolute paths, including:
- Unix-style absolute paths like `/usr/local/bin`, `/home/user`, etc.
- Windows-style absolute paths like `C:/Users` or `C:\Users`
- Root path `/`

Currently it only seems to work correctly for the root path `/` but fails for any path longer than that.

### System Info
- Node version: 18.x
- OS: macOS / Linux

---
Repository: /testbed
