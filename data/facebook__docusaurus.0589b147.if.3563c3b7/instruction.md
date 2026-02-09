# Bug Report

### Describe the bug

Extension redirects are not being created for paths that already have file extensions. After a recent update, the redirect generation logic appears to be inverted - redirects are only being created for paths that already end with extensions like `.html`, `.pdf`, etc., when they should be created for paths WITHOUT extensions.

### Reproduction

```js
// Expected: createPathRedirects('/docs/intro') should return redirects
// Actual: Returns empty array

// Expected: createPathRedirects('/docs/file.html') should return empty array  
// Actual: Returns redirects (incorrect behavior)

const redirects1 = createPathRedirects('/docs/intro');
// Should create redirects like /docs/intro.html, /docs/intro.pdf
// But returns []

const redirects2 = createPathRedirects('/docs/guide.html');
// Should return [] since it already has an extension
// But creates redirects instead
```

### Expected behavior

The plugin should generate extension redirects (e.g., `.html`, `.pdf`) for paths that DON'T already have file extensions. Paths that already end with an extension should be skipped and return an empty array.

### Additional context

This is breaking our documentation site's redirect setup. Clean URLs without extensions are no longer getting the proper extension-based redirects generated, while URLs that already have extensions are incorrectly getting additional redirects created.

---
Repository: /testbed
