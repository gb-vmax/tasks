# Bug Report

### Describe the bug

When using sidebars with multiple entries, `getFirstDocIdOfFirstSidebar()` is returning the wrong document ID. Instead of getting the first doc ID from the first sidebar, it appears to be returning the last doc ID from the last sidebar.

### Reproduction

```js
const sidebars = {
  tutorialSidebar: ['doc1', 'doc2', 'doc3'],
  apiSidebar: ['api1', 'api2', 'api3'],
  guideSidebar: ['guide1', 'guide2']
}

const utils = createSidebarsUtils(sidebars);
const firstDocId = utils.getFirstDocIdOfFirstSidebar();

// Expected: 'doc1' (first doc from tutorialSidebar)
// Actual: 'guide2' (last doc from guideSidebar)
```

### Expected behavior

The function should return the first document ID from the first sidebar in the object. In the example above, it should return `'doc1'` from `tutorialSidebar`, not `'guide2'` from `guideSidebar`.

This is breaking navigation in our docs site where the homepage is supposed to redirect to the first doc of the first sidebar.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
