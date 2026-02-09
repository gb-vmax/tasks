# Bug Report

### Describe the bug

When navigating to pages with `.html` extensions or `index.html` in the pathname, the location normalization is caching incorrectly. After the first visit to a page like `/docs/intro.html`, subsequent navigations to the same path return the wrong pathname from the cache.

### Reproduction

```js
// First navigation
navigate('/docs/intro.html')
// location.pathname correctly normalized to '/docs/intro'

// Second navigation to the same URL
navigate('/docs/intro.html')
// location.pathname incorrectly returns '/docs/intro.html' instead of '/docs/intro'
```

The issue seems to be with how pathnames are being cached. The cache lookup works, but it's returning the original pathname with `.html` instead of the normalized version.

### Expected behavior

All navigations to `/docs/intro.html` should consistently normalize to `/docs/intro`, regardless of whether it's the first visit or a cached lookup.

### Additional context

This affects any page accessed with `.html` extension or `/index.html` suffix. The first visit works fine, but subsequent visits to the same URL path don't apply the normalization properly.

---
Repository: /testbed
