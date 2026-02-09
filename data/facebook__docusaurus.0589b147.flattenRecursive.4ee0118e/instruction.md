# Bug Report

### Describe the bug

The sidebar items are appearing in the wrong order after a recent update. Category items are now showing up **after** their child items instead of before them, which breaks the expected hierarchy in the documentation sidebar.

### Reproduction

```js
const sidebarConfig = {
  items: [
    {
      type: 'category',
      label: 'Parent Category',
      items: [
        { type: 'doc', id: 'child-doc-1' },
        { type: 'doc', id: 'child-doc-2' }
      ]
    }
  ]
};

// After flattening, the order is now:
// 1. child-doc-1
// 2. child-doc-2  
// 3. Parent Category  <-- should be first!
```

### Expected behavior

When flattening sidebar items, parent category items should appear **before** their children in the flattened array. The current behavior has them appearing after, which reverses the expected document structure.

The flattened output should be:
1. Parent Category
2. child-doc-1
3. child-doc-2

But instead we're getting them in reverse order.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
