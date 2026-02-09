# Bug Report

### Describe the bug

I'm experiencing an issue with the sidebar generation where category items are missing from the flattened sidebar structure. When I use `flattenSidebarItems()`, only the leaf items (docs/links) are returned, but the category items themselves are not included in the output.

### Reproduction

```js
const sidebarItems = [
  {
    type: 'category',
    label: 'Getting Started',
    items: [
      { type: 'doc', id: 'intro' },
      { type: 'doc', id: 'installation' }
    ]
  }
];

const flattened = flattenSidebarItems(sidebarItems);
// Expected: category item + doc items
// Actual: only doc items are returned
```

### Expected behavior

The flattened array should include both category items and their children, with categories appearing before their child elements as mentioned in the function documentation. Currently, the category items are being excluded from the result.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
