# Bug Report

### Describe the bug

The `applyTrailingSlash` function is not working correctly - it's adding leading slashes instead of trailing slashes when the `trailingSlash` option is set to `true`.

### Reproduction

```js
import applyTrailingSlash from '@docusaurus/utils-common';

// This should add a trailing slash
const result = applyTrailingSlash('docs/intro', true);
console.log(result); // Expected: 'docs/intro/', Actual: '/docs/intro'

// Another example
const result2 = applyTrailingSlash('blog', true);
console.log(result2); // Expected: 'blog/', Actual: '/blog'
```

### Expected behavior

When `trailingSlash` is `true`, the function should append a `/` at the end of the path if it doesn't already have one. Instead, it's prepending a `/` at the beginning of the path.

### System Info

- Docusaurus version: latest
- Node version: 18.x

This is breaking URL generation in my site - all internal links are getting leading slashes added instead of trailing slashes, which is causing navigation issues.

---
Repository: /testbed
