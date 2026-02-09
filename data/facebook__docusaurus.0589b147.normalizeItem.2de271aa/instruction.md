# Bug Report

### Describe the bug

When using categories in sidebars configuration, the normalization process doesn't return the expected normalized items. After processing a categories shorthand, the normalized result is not being returned, which causes the sidebar items to be undefined or missing.

### Reproduction

```js
const sidebar = [
  {
    type: 'category',
    label: 'My Category',
    items: [
      'doc1',
      'doc2'
    ]
  }
]

// After normalization, the category items are lost
```

### Expected behavior

The sidebar normalization should properly handle and return normalized category items. Categories shorthand should be expanded and returned as normalized sidebar items.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
