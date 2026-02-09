# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar categories that have a generated-index link but no items. After a recent update, these categories are being filtered out completely instead of being rendered as links.

### Reproduction

```js
// In sidebars.js
{
  type: 'category',
  label: 'API Reference',
  link: {
    type: 'generated-index',
    title: 'API Overview'
  },
  items: [] // Empty items array
}
```

When the category has no items (or all items are filtered as drafts), the entire category disappears from the sidebar even though it has a valid generated-index link.

### Expected behavior

The category should still be rendered as a clickable link in the sidebar when it has a generated-index link, even if there are no subitems. The generated index page should be accessible.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
