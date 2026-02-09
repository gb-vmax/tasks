# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar category configuration in the docs plugin. When defining a category in the sidebar, the properties from the category object are not being preserved correctly. Instead of spreading the category item itself, it seems like only the items array is being spread, which causes the category configuration (like `label`, `collapsed`, `collapsible`, etc.) to be lost.

### Reproduction

```js
// sidebars.js
module.exports = {
  docs: [
    {
      type: 'category',
      label: 'Getting Started',
      collapsed: false,
      collapsible: true,
      items: ['intro', 'installation']
    }
  ]
}
```

After building, the category appears but without the correct label or collapsed state. The category metadata seems to be missing.

### Expected behavior

The category should maintain all its properties (label, collapsed, collapsible, etc.) and display correctly in the sidebar with the specified configuration.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
