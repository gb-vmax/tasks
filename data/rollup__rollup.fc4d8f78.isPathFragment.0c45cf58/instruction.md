# Bug Report

### Describe the bug

The path fragment detection is not working correctly for relative paths starting with `./`. When I try to use a path like `./myModule`, it's not being recognized as a path fragment even though it should be.

### Reproduction

```js
import { isPathFragment } from './utils/relativeId';

// This should return true but returns false
console.log(isPathFragment('./myModule')); // Expected: true, Actual: false

// This still works correctly
console.log(isPathFragment('../myModule')); // Returns: true
console.log(isPathFragment('/absolute/path')); // Returns: true
```

### Expected behavior

Paths starting with `./` should be recognized as path fragments, just like paths starting with `../` or `/`.

### System Info
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
