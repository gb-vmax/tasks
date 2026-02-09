# Bug Report

### Describe the bug

The `findSidebarCategory` function is returning the wrong category when searching through nested sidebar structures. It appears to be returning child categories instead of parent categories when both match the search predicate.

### Reproduction

```js
const sidebar = [
  {
    type: 'category',
    label: 'Parent Category',
    items: [
      {
        type: 'category',
        label: 'Child Category',
        items: []
      }
    ]
  }
];

// If both parent and child match the predicate, 
// the function returns the child instead of the parent
const result = findSidebarCategory(sidebar, (cat) => cat.label.includes('Category'));

// Expected: Parent Category
// Actual: Child Category
```

### Expected behavior

When multiple categories match the predicate in a nested structure, the function should return the first matching category in depth-first order (parent before children). Currently it seems to prioritize child categories over their parents.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
