# Bug Report

### Describe the bug

The `isAbsolute()` function is returning incorrect results for absolute paths. When I pass in a valid absolute path, it's being treated as relative instead.

### Reproduction

```js
import { isAbsolute } from './utils/path';

// These should all return true but they don't
console.log(isAbsolute('/usr/local/bin'));  // Expected: true, Got: false
console.log(isAbsolute('C:\\Program Files'));  // Expected: true, Got: false
console.log(isAbsolute('/home/user/project'));  // Expected: true, Got: false
```

### Expected behavior

The function should correctly identify absolute paths and return `true` for them. Right now it seems to be doing the opposite - returning `false` for absolute paths and probably `true` for relative ones.

### Additional context

This is breaking path resolution in my build scripts. Not sure when this started happening but it's causing issues with file imports that use absolute paths.

---
Repository: /testbed
