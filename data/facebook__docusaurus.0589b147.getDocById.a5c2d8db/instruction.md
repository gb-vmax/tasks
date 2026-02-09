# Bug Report

### Describe the bug

I'm experiencing an issue where sidebar document links are not rendering correctly. When I have a valid document ID in my sidebars configuration, the sidebar appears to be empty or the document metadata is missing.

### Reproduction

```js
// sidebars.js
module.exports = {
  docs: [
    {
      type: 'doc',
      id: 'intro', // This is a valid document that exists
    },
  ],
};
```

With a valid `intro.md` file in my docs folder, the sidebar item doesn't display properly. The document metadata seems to be missing even though the document exists.

### Expected behavior

When a document with a valid ID exists and is referenced in the sidebar configuration, it should display correctly with all its metadata (title, permalink, etc.).

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
