# Bug Report

### Describe the bug

I'm experiencing an issue with trailing slash handling in URLs. When trying to remove trailing slashes from paths, the function doesn't seem to be working correctly anymore. The trailing slash remains in the URL even when it should be removed.

### Reproduction

```js
const path = '/docs/intro/';

// Expected: '/docs/intro'
// Actual: '/docs/intro/' (trailing slash not removed)
const result = applyTrailingSlash(path, false);
```

This also affects paths without trailing slashes:
```js
const path = '/docs/intro';

// Expected: '/docs/intro' (unchanged)
// Actual: behavior is inconsistent
const result = applyTrailingSlash(path, false);
```

### Expected behavior

When `applyTrailingSlash` is called with `trailingSlash: false`, it should remove any trailing slashes from the path. Paths without trailing slashes should remain unchanged.

### System Info

- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently. The trailing slash configuration doesn't appear to be respected properly anymore.

---
Repository: /testbed
