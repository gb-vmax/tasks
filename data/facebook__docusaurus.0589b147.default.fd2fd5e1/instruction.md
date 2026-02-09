# Bug Report

### Describe the bug

I'm encountering an issue with `rehype-stringify` where the module export is not working as expected. When trying to use the default export from `rehype-stringify@10.0.0`, I'm getting unexpected behavior - it seems like the export is being wrapped in an extra function call or returning a function instead of the actual `rehypeStringify` implementation.

### Reproduction

```js
const rehypeStringify = require('rehype-stringify');

// Expected: rehypeStringify should be the actual plugin function
// Actual: Getting something else (possibly a wrapper function)

const unified = require('unified');
const processor = unified().use(rehypeStringify);
// This fails or behaves unexpectedly
```

### Expected behavior

The default export should directly provide the `rehypeStringify` plugin function that can be used with unified processors, not a wrapper or modified version of it.

### System Info
- Package: rehype-stringify@10.0.0
- Node version: (any)

---
Repository: /testbed
