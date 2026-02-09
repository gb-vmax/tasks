# Bug Report

### Describe the bug

The `isRelative()` function is incorrectly identifying paths as relative when they should be absolute. This is causing issues with path resolution in my project.

### Reproduction

```js
import { isRelative } from './utils/path';

// These should return false but are returning true
console.log(isRelative('/absolute/path'));  // Expected: false, Actual: true
console.log(isRelative('C:\\Windows\\System32'));  // Expected: false, Actual: true

// Empty string edge case
console.log(isRelative(''));  // Expected: false, Actual: true
```

### Expected behavior

The function should correctly identify absolute paths (starting with `/` on Unix or drive letters on Windows) as NOT relative, and return `false` for them. Only paths like `./relative` or `../parent` should be considered relative.

### System Info
- Node version: 18.x
- OS: macOS

This seems to have broken after a recent update. The logic for determining relative vs absolute paths appears to be inverted.

---
Repository: /testbed
