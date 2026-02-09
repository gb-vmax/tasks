# Bug Report

### Describe the bug

I'm getting unexpected redeclaration errors when declaring variables in modules. The error is being thrown for variables that should be allowed, while variables that actually conflict with imports are not being caught.

### Reproduction

```js
// module.js
import { foo } from './other.js';

// This should error but doesn't - foo is already imported
const foo = 'bar';

// This errors incorrectly - bar is not imported
const bar = 'baz';
```

The behavior seems inverted - variables that don't conflict with imports are throwing redeclaration errors, while variables that actually redeclare imported names are being allowed through.

### Expected behavior

The module should:
1. Allow declaring variables that don't conflict with any imports
2. Throw a redeclaration error when a variable name conflicts with an existing import

Currently it's doing the opposite of what it should be doing.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
