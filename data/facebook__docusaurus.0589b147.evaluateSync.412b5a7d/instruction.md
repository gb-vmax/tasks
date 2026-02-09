# Bug Report

### Describe the bug

I'm encountering a syntax error when trying to use the MDX library. It seems like there's a malformed export in the main module file that's preventing the library from loading correctly.

### Reproduction

```js
import { evaluateSync } from '@mdx-js/mdx';

// This throws a syntax error before any code can execute
const result = evaluateSync('some content');
```

The error occurs immediately on import, before any actual code runs. It appears to be related to how `evaluateSync` is exported from the module.

### Expected behavior

The import should work without any syntax errors, and `evaluateSync` should be available as an exported function that can be called normally.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
