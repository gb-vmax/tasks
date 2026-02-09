# Bug Report

### Describe the bug

I'm experiencing an issue with URL path handling where the trailing slash behavior is completely broken. When I try to apply trailing slash settings to paths, the output is completely wrong - it seems like the path components are getting swapped or replaced incorrectly.

### Reproduction

```js
import applyTrailingSlash from '@docusaurus/utils-common';

const result = applyTrailingSlash('/docs/intro', {
  trailingSlash: true,
  baseUrl: '/'
});

console.log(result); 
// Expected: '/docs/intro/'
// Actual: Something completely wrong
```

The function appears to be replacing parts of the URL in the wrong order. For example:
- Input: `/docs/intro?search=test`
- Expected with `trailingSlash: true`: `/docs/intro/?search=test`
- Actual: The pathname and query string seem to get mixed up

### Steps to reproduce

1. Call `applyTrailingSlash` with any path that has query parameters or hash
2. Set `trailingSlash` to `true` or `false`
3. Observe that the returned path is malformed

This is breaking URL generation across the site. Paths with query strings or anchors are particularly affected.

### Expected behavior

The function should correctly add or remove trailing slashes from the pathname portion of the URL while preserving query strings and hash fragments in their original positions.

### System Info

- @docusaurus/utils-common: latest
- Node: 18.x

---
Repository: /testbed
