# Bug Report

### Describe the bug

The `findSidebarCategory` function is not working correctly when searching for sidebar categories. It seems like the function is failing to find categories that should match the predicate, even when they exist in the sidebar structure.

### Reproduction

```js
const sidebar = [
  {
    type: 'category',
    label: 'Getting Started',
    items: [
      { type: 'doc', id: 'intro' }
    ]
  },
  {
    type: 'category',
    label: 'Advanced',
    items: [
      {
        type: 'category',
        label: 'Nested Category',
        items: []
      }
    ]
  }
];

// Try to find a category by label
const result = findSidebarCategory(sidebar, (category) => category.label === 'Getting Started');

// Expected: Should return the 'Getting Started' category object
// Actual: Returns undefined
```

### Expected behavior

The function should correctly identify and return sidebar items of type 'category' that match the given predicate. It should also properly traverse nested categories to find matches at any depth level.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
