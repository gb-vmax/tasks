# Bug Report

### Describe the bug

The `findSidebarCategory` function seems to have a recursion issue. When searching through nested sidebar categories, the function gets stuck in an infinite loop and causes the application to hang/crash with a stack overflow error.

### Reproduction

```js
const sidebar = [
  {
    type: 'category',
    label: 'Parent',
    items: [
      {
        type: 'category',
        label: 'Child',
        items: []
      }
    ]
  }
];

// This causes infinite recursion
const result = findSidebarCategory(sidebar, (category) => category.label === 'Child');
```

### Expected behavior

The function should traverse the nested sidebar structure without getting stuck in an infinite loop. It should find the matching category or return `undefined` if no match is found.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
