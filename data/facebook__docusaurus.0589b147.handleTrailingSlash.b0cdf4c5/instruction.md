# Bug Report

### Describe the bug

I'm experiencing an issue with trailing slash handling in URLs. It appears that the `applyTrailingSlash` function is applying the opposite behavior of what's expected - it's adding trailing slashes when they should be removed, and removing them when they should be added.

### Reproduction

```js
import applyTrailingSlash from '@docusaurus/utils-common';

// When trailingSlash is true, expecting to add a trailing slash
const result1 = applyTrailingSlash('/docs/intro', true);
console.log(result1); // Expected: '/docs/intro/', Actual: '/docs/intro'

// When trailingSlash is false, expecting to remove trailing slash
const result2 = applyTrailingSlash('/docs/intro/', false);
console.log(result2); // Expected: '/docs/intro', Actual: '/docs/intro/'
```

### Expected behavior

- When `trailingSlash` option is set to `true`, URLs should have a trailing slash added
- When `trailingSlash` option is set to `false`, URLs should have trailing slashes removed

### System Info

- Docusaurus version: latest
- Node version: 18.x

This is causing issues with my site's routing and SEO as URLs are not being formatted correctly. Any help would be appreciated!

---
Repository: /testbed
