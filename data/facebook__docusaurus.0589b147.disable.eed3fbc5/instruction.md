# Bug Report

### Describe the bug

After a recent update, I'm getting a runtime error when trying to use MDX. It seems like there's an issue with the `disable` export in the constructs module - it's being called as a function when it should just be a reference.

### Reproduction

```js
import { disable } from '@mdx-js/mdx'

// Attempting to use disable throws an error
console.log(disable)
```

When I try to import or access the `disable` export, I get an error because it's trying to execute `disable()` immediately instead of just exporting the value/function itself.

### Expected behavior

The `disable` export should be accessible as a normal value/function reference, not automatically invoked during the export process.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
