# Bug Report

### Describe the bug

I'm experiencing an issue with path detection in the `isPathFragment` function. It seems like certain path patterns starting with `/.` are being incorrectly identified as path fragments when they shouldn't be.

### Reproduction

```js
import { isPathFragment } from './utils/relativeId';

// This is incorrectly returning true
console.log(isPathFragment('/.well-known')); // Expected: false, Actual: true
console.log(isPathFragment('/.config')); // Expected: false, Actual: true
console.log(isPathFragment('/.env')); // Expected: false, Actual: true
```

Paths that start with `/.` (like `/.well-known`, `/.config`, etc.) are being treated as path fragments, but they should be treated as regular module identifiers or file names, not relative paths.

### Expected behavior

Paths starting with `/.` should not be identified as path fragments unless they're actually relative path patterns like `../` or `./`. The function should only return `true` for actual path fragments like:
- `/` (absolute paths)
- `./` (current directory)
- `../` (parent directory)
- Absolute paths like `C:/` on Windows

But paths like `/.well-known` or `/.config` should return `false`.

### System Info
- Version: latest
- Node: v18.x

---
Repository: /testbed
