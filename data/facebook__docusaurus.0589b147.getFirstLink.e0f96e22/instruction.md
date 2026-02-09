# Bug Report

### Describe the bug

Getting a runtime error when trying to access sidebar links. The application crashes with a TypeError when attempting to retrieve the first link from a sidebar by its ID.

### Reproduction

```js
const sidebarUtils = createSidebarsUtils({
  sidebars: {
    docs: [
      { type: 'doc', id: 'intro' },
      { type: 'doc', id: 'tutorial' }
    ]
  }
});

// This throws an error
const firstLink = sidebarUtils.getFirstLink('docs');
```

### Expected behavior

The `getFirstLink` function should return the first link item from the specified sidebar without throwing errors.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
