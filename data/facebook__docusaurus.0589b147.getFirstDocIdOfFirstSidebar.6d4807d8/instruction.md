# Bug Report

### Describe the bug

When trying to access the first document in a sidebar configuration, the wrong document ID is being returned. Instead of getting the first document from the first sidebar, it seems like the function is returning undefined or an incorrect value.

### Reproduction

```js
const sidebars = {
  tutorialSidebar: ['doc1', 'doc2', 'doc3'],
  apiSidebar: ['api1', 'api2']
}

// Expected: 'doc1' (first doc of first sidebar)
// Actual: undefined or wrong value
const firstDocId = getFirstDocIdOfFirstSidebar()
```

### Expected behavior

`getFirstDocIdOfFirstSidebar()` should return the first document ID from the first sidebar in the configuration. In the example above, it should return `'doc1'`.

### System Info

- Docusaurus version: latest
- Node version: 18.x

This is breaking navigation to the first page when no specific document is specified. The function appears to be looking at the wrong part of the sidebar structure.

---
Repository: /testbed
