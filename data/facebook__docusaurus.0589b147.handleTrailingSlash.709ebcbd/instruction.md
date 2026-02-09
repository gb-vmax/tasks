# Bug Report

### Describe the bug

The `applyTrailingSlash` function is applying trailing slashes incorrectly - it's doing the opposite of what's expected. When I set `trailingSlash: true`, it removes the trailing slash, and when I set `trailingSlash: false`, it adds one.

### Reproduction

```js
import applyTrailingSlash from '@docusaurus/utils-common';

// When trailingSlash is true, expecting slash to be added
const result1 = applyTrailingSlash('/docs/intro', true);
console.log(result1); // Returns '/docs/intro' but should return '/docs/intro/'

// When trailingSlash is false, expecting slash to be removed
const result2 = applyTrailingSlash('/docs/intro/', false);
console.log(result2); // Returns '/docs/intro/' but should return '/docs/intro'
```

### Expected behavior

- When `trailingSlash` is `true`, the function should add a trailing slash to paths that don't have one
- When `trailingSlash` is `false`, the function should remove trailing slashes from paths that have one

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is breaking our site's routing configuration. Any help would be appreciated!

---
Repository: /testbed
