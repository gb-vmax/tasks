# Bug Report

### Describe the bug

When using sidebar configuration with doc items, the sidebar link generation appears to be using the wrong field for the document ID. Instead of using the actual document ID, it seems to be using the label field, which causes links to break when the label differs from the ID.

### Reproduction

```js
// sidebars.js
module.exports = {
  docs: [
    {
      type: 'doc',
      id: 'getting-started',
      label: 'Getting Started Guide'
    }
  ]
}
```

In this case, the sidebar should link to the document with ID `getting-started`, but it appears to be trying to link to a document with ID `Getting Started Guide` instead, resulting in broken navigation.

### Expected behavior

The sidebar should use the `id` field to generate links to documents, not the `label` field. The label should only be used for display purposes in the sidebar.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is breaking our documentation site navigation. Any help would be appreciated!

---
Repository: /testbed
