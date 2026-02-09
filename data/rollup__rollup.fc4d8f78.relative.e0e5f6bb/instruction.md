# Bug Report

### Describe the bug

The `relative()` path function is producing incorrect results when computing relative paths between directories. When I try to get the relative path from one directory to another, the output is wrong - it's missing path segments that should be there.

### Reproduction

```js
import { relative } from './path'

// This returns an incorrect result
const result = relative('/a/b/c', '/a/b/d')
console.log(result) // Expected: '../d' but getting something else

// Another example that fails
const result2 = relative('/foo/bar', '/foo/baz')
console.log(result2) // Should be '../baz'
```

### Expected behavior

The function should correctly compute the relative path between two absolute paths. When going from `/a/b/c` to `/a/b/d`, the expected result is `../d` (go up one level, then into `d`).

### System Info
- Version: latest
- Environment: Browser

---
Repository: /testbed
