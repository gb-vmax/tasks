# Bug Report

### Describe the bug

I'm experiencing an issue where `getFirstDocIdOfFirstSidebar()` returns undefined or an incorrect value instead of returning the first document ID from the first sidebar. This appears to be affecting sidebar navigation and potentially causing issues when trying to determine the initial/landing page for documentation.

### Reproduction

```js
const sidebars = {
  tutorialSidebar: ['doc1', 'doc2', 'doc3'],
  apiSidebar: ['api1', 'api2']
}

// When calling getFirstDocIdOfFirstSidebar()
// Expected: 'doc1'
// Actual: undefined or wrong value
```

### Expected behavior

The function should return the first document ID from the first sidebar (in the example above, it should return `'doc1'`). This is important for determining the default landing page when navigating to documentation.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
