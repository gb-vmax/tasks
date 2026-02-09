# Bug Report

### Describe the bug

The `applyTrailingSlash` function is producing incorrect results when handling URL paths. It seems like the logic for adding/removing trailing slashes got inverted somewhere, causing paths to get the opposite treatment of what's expected.

### Reproduction

```js
import applyTrailingSlash from '@docusaurus/utils-common';

// When trailingSlash is true, expecting to ADD a slash
const result1 = applyTrailingSlash('/docs/intro', true);
console.log(result1); // Expected: '/docs/intro/' but getting '/docs/intro'

// When trailingSlash is false, expecting to REMOVE a slash
const result2 = applyTrailingSlash('/docs/intro/', false);
console.log(result2); // Expected: '/docs/intro' but getting '/docs/intro/'
```

### Expected behavior

- When `trailingSlash` is `true`, the function should ensure the path ends with a `/`
- When `trailingSlash` is `false`, the function should ensure the path does NOT end with a `/`

Currently getting the opposite behavior - paths that should have trailing slashes don't have them, and paths that shouldn't have trailing slashes do have them.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
