# Bug Report

### Describe the bug

I'm experiencing an issue with document navigation links in my docs. When a document doesn't have a previous or next document (i.e., when `docId` is `null` or `undefined`), the navigation is returning an empty string `""` instead of being properly hidden or returning `undefined`.

This is causing unexpected behavior in the UI where navigation elements are being rendered incorrectly - instead of no link appearing, there's an empty/broken link element.

### Reproduction

```js
// When a document is the first in the sidebar (no previous doc)
// Or last in the sidebar (no next doc)
// The navigation link returns "" instead of undefined

const doc = {
  id: 'first-doc',
  // no previous document
}

// Expected: previous navigation link should be undefined
// Actual: previous navigation link returns ""
```

### Expected behavior

When there's no previous or next document (when `docId` is `null` or `undefined`), the function should return `undefined` so that no navigation link is rendered. Currently it's returning an empty string which causes rendering issues.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
