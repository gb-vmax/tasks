# Bug Report

### Describe the bug

The sidebar flattening function is not working as expected. When flattening nested sidebar categories, the parent category items are being excluded from the flattened result, and non-category items are being wrapped in an extra array instead of being returned directly.

### Reproduction

```js
const items = [
  {
    type: 'category',
    label: 'Parent',
    items: [
      { type: 'link', label: 'Child 1' },
      { type: 'link', label: 'Child 2' }
    ]
  }
];

const flattened = flattenSidebarItems(items);
// Expected: [parent category, child 1, child 2]
// Actual: [child 1 wrapped in array, child 2 wrapped in array]
```

The function should return a flat array where category items appear before their children, but currently:
1. Category items themselves are missing from the output
2. Non-category items are incorrectly wrapped in nested arrays

### Expected behavior

The flattened array should include all items with parent categories appearing before their child elements. For nested categories, the structure should be fully flattened while maintaining the parent-first order.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
