# Bug Report

### Describe the bug

When using the docs plugin with a valid sidebar configuration, I'm getting an error saying the document ID couldn't be found, even though the document exists and is properly referenced. The error message is being thrown incorrectly for documents that should be valid.

### Reproduction

```js
// sidebars.js
module.exports = {
  docs: [
    {
      type: 'doc',
      id: 'intro', // This document exists
    },
  ],
};
```

When building the site with this configuration, it throws an error:
```
Invalid sidebars file. The document with id "intro" was used in the sidebar, but no document with this id could be found.
```

However, the document with id "intro" definitely exists in the docs folder.

### Expected behavior

The build should succeed when referencing valid document IDs in the sidebar. The error should only be thrown when a document ID is actually missing, not when it exists.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started recently. Any valid document ID referenced in sidebars now causes this error during build.

---
Repository: /testbed
