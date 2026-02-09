# Bug Report

### Describe the bug

I'm experiencing an issue with `getFirstDocIdOfFirstSidebar()` where it returns `undefined` instead of the first document ID from the first sidebar. It seems like the function is trying to access a nested property incorrectly.

### Reproduction

```js
// Given a sidebars structure like:
const sidebars = {
  docs: ['doc1', 'doc2', 'doc3'],
  api: ['api1', 'api2']
}

// When calling getFirstDocIdOfFirstSidebar()
const firstDocId = getFirstDocIdOfFirstSidebar()

// Expected: 'doc1'
// Actual: undefined
```

The function should return the first document ID from the first sidebar, but instead it's returning `undefined`.

### Expected behavior

`getFirstDocIdOfFirstSidebar()` should return the first document ID (e.g., `'doc1'`) from the first sidebar in the sidebars object.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
