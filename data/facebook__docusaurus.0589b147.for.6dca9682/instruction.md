# Bug Report

### Describe the bug

The `findSidebarCategory` function is not working correctly when searching through sidebar items. It seems to be skipping over category items and attempting to process non-category items as if they were categories, which causes the function to fail finding the correct sidebar category.

### Reproduction

```js
const sidebar = [
  {
    type: 'category',
    label: 'Getting Started',
    items: [
      { type: 'doc', id: 'intro' },
      {
        type: 'category',
        label: 'Advanced',
        items: [{ type: 'doc', id: 'advanced-guide' }]
      }
    ]
  }
];

// Try to find a nested category
const result = findSidebarCategory(sidebar, (category) => category.label === 'Advanced');

// Expected: Should find the nested 'Advanced' category
// Actual: Returns undefined or throws error
```

### Expected behavior

The function should correctly traverse the sidebar tree and find category items that match the predicate, including deeply nested categories. Non-category items should be skipped during the search.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
