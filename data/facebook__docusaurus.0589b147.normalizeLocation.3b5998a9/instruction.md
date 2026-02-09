# Bug Report

### Describe the bug

I'm experiencing an issue with URL normalization where paths ending with `.html` are being incorrectly stripped even when they match exact routes. This causes navigation to break for pages that are explicitly registered with `.html` extensions.

### Reproduction

1. Register a route with an exact `.html` path (e.g., `/page.html`)
2. Navigate to that URL
3. The `.html` extension gets stripped from the pathname
4. The page fails to render or navigates to the wrong location

For example:
```js
// Route is registered as /docs/intro.html with exact: true
// When navigating to /docs/intro.html
// Expected: pathname stays as /docs/intro.html
// Actual: pathname becomes /docs/intro
```

This seems to happen after the location normalization logic processes the pathname. The route matching works correctly and identifies it as an exact match, but then the extension still gets removed.

### Expected behavior

When a route is registered with an `.html` extension and marked as exact, the pathname should be preserved as-is without stripping the extension. The normalization should only apply to routes that aren't exact matches.

### System Info
- Docusaurus version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
