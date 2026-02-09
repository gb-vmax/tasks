# Bug Report

### Describe the bug

The `isRelative()` path utility function is returning incorrect results. When I pass certain path strings to it, I'm getting the opposite of what I expect - paths that should be identified as relative are being marked as absolute and vice versa.

### Reproduction

```js
import { isRelative } from './utils/path';

// These are giving unexpected results:
console.log(isRelative(''));           // Expected: false, Got: true
console.log(isRelative('./file.js'));  // Expected: true, Got: false
console.log(isRelative('../file.js')); // Expected: true, Got: false
console.log(isRelative('file.js'));    // Expected: true, Got: false
```

### Expected behavior

- Empty string `''` should return `false` (not a valid relative path)
- Paths starting with `./` or `../` should return `true`
- Simple file paths without leading slashes should return `true`

The function seems to be inverting the logic somehow. This is breaking path resolution in my build configuration.

### System Info
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
