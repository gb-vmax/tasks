# Bug Report

### Describe the bug

I'm experiencing an issue where valid documents are being rejected when building the sidebar. The error message says the document ID couldn't be found, but the document actually exists and should be available.

### Reproduction

```js
// sidebars.js
module.exports = {
  docs: [
    {
      type: 'doc',
      id: 'intro',
    },
  ],
};

// docs/intro.md exists and has proper frontmatter
```

When building the site, I get an error like:
```
Invalid sidebars file. The document with id "intro" was used in the sidebar, but no document with this id could be found.
```

But the document clearly exists in the docs folder.

### Expected behavior

The sidebar should build successfully when referencing valid document IDs. Documents that exist should be found and included in the sidebar without throwing errors.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is blocking my documentation site from building. Any help would be appreciated!

---
Repository: /testbed
