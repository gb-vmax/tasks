# Bug Report

### Describe the bug

I'm encountering a syntax error when trying to use the library. It looks like there's an issue with the exported module structure - the code is throwing an error about an unexpected token.

### Reproduction

```js
import { overloadedBoolean } from '@mdx-js/mdx';

// Attempting to use the exported function
const result = overloadedBoolean('true');
```

When I try to run this, I get a parsing error. It seems like the export statement is malformed or the module structure got corrupted somehow.

### Expected behavior

The `overloadedBoolean` function should be properly exported and usable without any syntax errors. The module should load correctly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
