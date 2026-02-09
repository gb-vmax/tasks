# Bug Report

### Describe the bug

When using sidebar items with nested categories, the flattened sidebar structure is incomplete. Some sidebar items are missing from the flattened output, causing navigation links to disappear from the documentation.

### Reproduction

```js
const sidebarItems = [
  {
    type: 'category',
    label: 'Getting Started',
    items: [
      {
        type: 'category',
        label: 'Installation',
        items: [
          { type: 'doc', id: 'install-npm' },
          { type: 'doc', id: 'install-yarn' }
        ]
      },
      { type: 'doc', id: 'quickstart' }
    ]
  }
];

// After flattening, some doc items are missing
const flattened = flattenSidebarItems(sidebarItems);
// Expected all items to be present but some are gone
```

### Expected behavior

All sidebar items (categories, docs, links) should be present in the flattened structure. The flattening should preserve all nested items regardless of their type.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
