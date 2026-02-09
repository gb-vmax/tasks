# Bug Report

### Describe the bug

The `applyTrailingSlash` function is not removing trailing slashes correctly. When I pass a path with a trailing slash and the `trailingSlash` option is set to `false`, the function removes the leading slash instead of the trailing one.

### Reproduction

```js
import applyTrailingSlash from '@docusaurus/utils-common';

const path = '/docs/intro/';
const result = applyTrailingSlash(path, false);

console.log(result); // Expected: '/docs/intro', Actual: 'docs/intro/'
```

The function is supposed to remove the trailing slash when `trailingSlash` is `false`, but instead it's removing the leading slash from the path.

### Expected behavior

When `trailingSlash` is set to `false`, the function should remove the trailing slash from the end of the path, not the leading slash from the beginning.

Expected output: `/docs/intro`  
Actual output: `docs/intro/`

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
