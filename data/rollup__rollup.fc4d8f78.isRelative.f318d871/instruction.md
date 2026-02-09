# Bug Report

### Describe the bug

The `isRelative()` function is returning incorrect results for certain path strings. It seems to be inverting the logic for paths that start with a dot (`.`).

### Reproduction

```js
import { isRelative } from './utils/path';

// These should return true but return false
console.log(isRelative('./file.txt'));  // Expected: true, Got: false
console.log(isRelative('../folder'));   // Expected: true, Got: false

// These should return false but return true  
console.log(isRelative('.hidden'));     // Expected: false, Got: true
console.log(isRelative('..invalid'));   // Expected: false, Got: true
```

### Expected behavior

Relative paths like `./file.txt` and `../folder` should be correctly identified as relative paths and return `true`. Files starting with a dot that aren't path separators (like `.hidden` files) should return `false`.

### System Info
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
