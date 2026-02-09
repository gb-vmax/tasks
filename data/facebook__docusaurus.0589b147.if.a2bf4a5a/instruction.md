# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar category items where nested items are not being processed correctly. The sidebar structure appears broken when using categories with multiple levels of nesting.

### Reproduction

```js
// sidebars.js
module.exports = {
  docs: [
    {
      type: 'category',
      label: 'Guides',
      items: [
        'intro',
        {
          type: 'category',
          label: 'Advanced',
          items: ['advanced/topic1', 'advanced/topic2']
        }
      ]
    }
  ]
}
```

When the sidebar is rendered, the nested category items show up as Promise objects instead of the actual processed items. The sidebar navigation is completely broken - clicking on categories doesn't expand them properly and the nested links are not clickable.

### Expected behavior

Categories should properly display their nested items, and the sidebar should be fully navigable with all nested categories and documents accessible.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
