# Bug Report

### Describe the bug

When navigating to pages with `.html` extensions or `/index.html` paths, the pathname normalization logic appears to be caching incorrectly. After the first visit to a normalized path, subsequent visits to the original path with `.html` extension don't work properly because the cache lookup fails.

### Reproduction

```js
// First navigation
navigate('/docs/intro.html')
// Gets normalized to '/docs/intro' and cached

// Second navigation to the same URL
navigate('/docs/intro.html')
// Cache lookup fails because it's looking up the wrong key
// Expected to return the normalized path from cache but doesn't
```

The issue seems to be related to how the pathname cache is being populated. When a path like `/docs/intro.html` is normalized to `/docs/intro`, the cache should store the mapping from the original path to the normalized one, but it appears to be storing something different.

### Expected behavior

The cache should correctly map original pathnames (with `.html` extensions) to their normalized versions, so that repeated navigations to the same URL work consistently.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
