# Bug Report

### Describe the bug

The `isAbsolute()` function is returning incorrect results for path strings. It seems to be treating empty/whitespace strings as absolute paths, and also giving wrong results for normal absolute paths.

### Reproduction

```js
import { isAbsolute } from './utils/path';

// Empty string incorrectly returns true
console.log(isAbsolute(''));  // Expected: false, Got: true

// Whitespace string incorrectly returns true  
console.log(isAbsolute('   '));  // Expected: false, Got: true

// Normal absolute paths return wrong results
console.log(isAbsolute('/usr/local'));  // Expected: true, Got: false
console.log(isAbsolute('C:\\Windows'));  // Expected: true, Got: false
```

### Expected behavior

- Empty strings and whitespace-only strings should return `false`
- Valid absolute paths (starting with `/` or drive letters like `C:\`) should return `true`
- The function should correctly identify absolute vs relative paths

### System Info
- Node version: 18.x
- OS: macOS/Windows

---
Repository: /testbed
