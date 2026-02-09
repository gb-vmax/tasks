# Bug Report

### Describe the bug

I'm experiencing an infinite recursion issue when working with sidebar items in Docusaurus. The application crashes with a "Maximum call stack size exceeded" error when trying to process sidebar configurations.

### Reproduction

This happens when you have a sidebar with items that need to be flattened. The issue occurs during the sidebar processing phase.

```js
const sidebar = {
  docs: [
    {
      type: 'doc',
      id: 'intro',
    },
    {
      type: 'category',
      label: 'Guides',
      items: [
        {
          type: 'doc',
          id: 'guide1',
        }
      ]
    }
  ]
}
```

When the sidebar is processed, it results in a stack overflow error. Even simple sidebar configurations with just a single doc item trigger this problem.

### Expected behavior

The sidebar items should be flattened correctly without causing infinite recursion. The application should start normally and display the sidebar properly.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
