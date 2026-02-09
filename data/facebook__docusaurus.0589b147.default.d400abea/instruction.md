# Bug Report

### Describe the bug

I'm encountering an issue with the rehype-stringify module where it seems to be exported incorrectly. When I try to use the default export from `rehype-stringify@10.0.0`, I'm getting a function that returns another function instead of the expected plugin function directly.

### Reproduction

```js
import rehypeStringify from 'rehype-stringify';

// Trying to use rehypeStringify in a unified pipeline
unified()
  .use(rehypeStringify)
  .process(/* ... */);
```

When I run this, the plugin doesn't work as expected. It seems like the export is wrapped in an extra function layer.

### Expected behavior

The default export should be the `rehypeStringify` function itself, not a function that returns it. The plugin should work directly when passed to `.use()` without needing to call it first.

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

---
Repository: /testbed
