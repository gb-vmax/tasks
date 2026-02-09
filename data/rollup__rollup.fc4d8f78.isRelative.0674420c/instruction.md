# Bug Report

### Describe the bug

The `isRelative()` function is returning incorrect results. It seems to be inverted - paths that should be identified as relative are being reported as absolute, and vice versa.

### Reproduction

```js
import { isRelative } from './utils/path'

// These should return true but return false
console.log(isRelative('./file.js'))  // Expected: true, Got: false
console.log(isRelative('../parent/file.js'))  // Expected: true, Got: false

// These should return false but return true  
console.log(isRelative('/absolute/path'))  // Expected: false, Got: true
console.log(isRelative('C:\\Windows\\path'))  // Expected: false, Got: true
```

### Expected behavior

The function should correctly identify relative paths (starting with `./` or `../`) as relative and return `true`, while absolute paths should return `false`.

### System Info
- Version: latest main branch
- Node: v18.x

---
Repository: /testbed
