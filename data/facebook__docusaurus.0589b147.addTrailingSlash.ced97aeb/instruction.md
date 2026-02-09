# Bug Report

### Describe the bug

The `applyTrailingSlash` function is not adding trailing slashes correctly. When I pass a path that doesn't have a trailing slash, it returns the path unchanged instead of adding one.

### Reproduction

```js
import applyTrailingSlash from '@docusaurus/utils-common';

const path = '/docs/intro';
const result = applyTrailingSlash(path, true);

console.log(result); // Expected: '/docs/intro/', Actual: '/docs/intro'
```

When `trailingSlash` is set to `true`, paths without trailing slashes should get one added, but they're being returned as-is.

### Expected behavior

When calling `applyTrailingSlash(path, true)` on a path like `/docs/intro`, it should return `/docs/intro/` with the trailing slash added.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
