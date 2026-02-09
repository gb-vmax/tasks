# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error when trying to use the MDX package. It looks like there's a malformed export statement in the vendor file that's breaking the module loading.

### Reproduction

```js
import { runSync } from '@mdx-js/mdx'

// Trying to use runSync throws an error about unexpected token
const result = runSync(tree, file)
```

The error appears to be coming from the module exports definition. When I inspect the compiled output, the `runSync` export seems to have invalid syntax - it looks like there's a mix of export definition and actual implementation code that got merged incorrectly.

### Expected behavior

The module should export `runSync` properly and allow it to be imported and used without syntax errors.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is blocking our build process. Any help would be appreciated!

---
Repository: /testbed
