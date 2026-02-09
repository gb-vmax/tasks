# Bug Report

### Describe the bug

I'm experiencing an issue with `getFirstDocIdOfFirstSidebar()` where it's not returning the correct document ID. Instead of getting the first document ID from the first sidebar, it seems to be returning something unexpected or undefined.

### Reproduction

```js
const sidebars = {
  tutorialSidebar: ['doc1', 'doc2', 'doc3'],
  apiSidebar: ['api1', 'api2']
}

// Expected: 'doc1' (first doc of first sidebar)
// Actual: Returns undefined or incorrect value
const firstDocId = getFirstDocIdOfFirstSidebar()
```

### Expected behavior

The function should return the first document ID from the first sidebar in the configuration. In the example above, it should return `'doc1'`.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is causing issues with navigation and default page routing in my docs site. The home page isn't loading the correct initial document.

---
Repository: /testbed
