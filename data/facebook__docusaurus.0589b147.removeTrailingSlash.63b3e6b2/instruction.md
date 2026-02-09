# Bug Report

### Describe the bug

The `applyTrailingSlash` function is not handling trailing slashes correctly. When trying to remove a trailing slash from a path, the function produces completely wrong output - it seems to be doing the opposite of what it should do.

### Reproduction

```js
import applyTrailingSlash from '@docusaurus/utils-common';

// Try to remove trailing slash
const result = applyTrailingSlash('/docs/intro/', false);
console.log(result); // Expected: '/docs/intro', Actual: 'docs/intro/'

// Another example
const result2 = applyTrailingSlash('/api/users/', false);
console.log(result2); // Expected: '/api/users', Actual: 'api/users/'
```

When `trailingSlash` option is set to `false`, paths that have trailing slashes should have them removed. Instead, the leading slash is being removed and a trailing slash is being added.

### Expected behavior

When `trailingSlash` is `false`:
- `/docs/intro/` should become `/docs/intro`
- `/api/users/` should become `/api/users`
- `/path/` should become `/path`

The function should only remove the trailing slash, not modify the rest of the path.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
