# Bug Report

### Describe the bug

The `findSidebarCategory` function is not working correctly when searching for categories in the sidebar. It appears that category items are being skipped entirely and the function is only processing non-category items, which causes it to fail when trying to access the `items` property on non-category sidebar items.

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
const result = findSidebarCategory(sidebar, (cat) => cat.label === 'Advanced');
// Expected: Should return the 'Advanced' category object
// Actual: Returns undefined or throws an error
```

### Expected behavior

The function should recursively search through sidebar categories and their nested items to find a category matching the predicate. It should correctly identify category items and only recurse into their items property.

### System Info
- Package: @docusaurus/theme-common
- Version: latest

---
Repository: /testbed
