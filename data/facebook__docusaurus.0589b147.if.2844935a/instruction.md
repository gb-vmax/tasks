# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar navigation where clicking on certain sidebar items leads to incorrect pages or broken links. It seems like the sidebar is trying to use labels as document IDs instead of the actual document IDs.

### Reproduction

```js
const sidebar = [
  {
    type: 'doc',
    id: 'getting-started',
    label: 'Getting Started Guide'
  },
  {
    type: 'category',
    label: 'Tutorials',
    items: [...]
  }
]
```

When I click on the "Getting Started Guide" item in the sidebar, I expect it to navigate to the document with ID `getting-started`, but instead it seems to be trying to navigate to a document with ID `Getting Started Guide` (the label), which doesn't exist.

### Expected behavior

Sidebar items should navigate to the correct document using the `id` field, not the `label` field. The label should only be used for display purposes in the sidebar.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is causing navigation to break completely in my documentation site. Any help would be appreciated!

---
Repository: /testbed
