# Bug Report

### Describe the bug

After a recent update, the MDX module appears to be broken. When trying to use the library, I'm getting syntax errors and the code doesn't execute properly. It seems like the vendor file for `@mdx-js/mdx@3.0.0` got corrupted or incompletely modified.

### Reproduction

```js
import { evaluateSync } from '@mdx-js/mdx';

// Trying to use any exported function fails
const result = evaluateSync(/* ... */);
```

The code fails to parse and throws errors about unexpected tokens or incomplete statements.

### Expected behavior

The MDX library should load and work correctly. All exported functions should be properly defined and functional.

### Additional context

Looking at the vendor file `jest/vendor/@mdx-js__mdx@3.0.0.js`, it appears that the code is malformed. The `evaluateSync` export definition seems to have been replaced with incomplete code that cuts off mid-statement (ends with `if (current` which is clearly incomplete).

This is preventing the entire module from loading correctly. The file needs to be restored to a valid state.

### System Info
- Affected file: `jest/vendor/@mdx-js__mdx@3.0.0.js`
- Issue: Syntax error due to incomplete code replacement

---
Repository: /testbed
