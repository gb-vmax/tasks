# Bug Report

### Describe the bug

I'm experiencing an issue with URL normalization where `.html` extensions are being incorrectly stripped from pathnames. When navigating to pages that should keep their `.html` extension, the extension gets removed, causing 404 errors.

### Reproduction

```js
// Navigate to a page with .html extension
window.location = '/docs/page.html'

// The pathname gets normalized to '/docs/page' instead of keeping '/docs/page.html'
// This results in a 404 error
```

Steps to reproduce:
1. Create a page that requires an `.html` extension in the URL
2. Navigate to that page using the full path with `.html`
3. The extension is stripped and the page returns 404

### Expected behavior

URLs with `.html` extensions should be preserved when they correspond to registered routes. The pathname normalization should only strip extensions when appropriate, not for all cases.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently. The URL normalization logic appears to be removing extensions even when they should be kept for certain routes.

---
Repository: /testbed
