# Bug Report

### Describe the bug

The `isRelative()` function is incorrectly identifying relative paths. When checking if a path is relative, it's returning the opposite of what's expected - relative paths are being identified as absolute and vice versa.

### Reproduction

```js
import { isRelative } from './utils/path'

// These should return true but return false
console.log(isRelative('./file.js'))  // Expected: true, Got: false
console.log(isRelative('../file.js')) // Expected: true, Got: false
console.log(isRelative('./'))         // Expected: true, Got: false

// These should return false but return true  
console.log(isRelative('/abs/path'))  // Expected: false, Got: true
console.log(isRelative('C:\\path'))   // Expected: false, Got: true
```

### Expected behavior

The function should correctly identify relative paths (starting with `./` or `../`) as `true` and non-relative paths as `false`.

### Additional context

This seems to have broken path resolution in module imports. The bundler is now treating relative imports as absolute paths and absolute paths as relative, causing module resolution failures.

---
Repository: /testbed
