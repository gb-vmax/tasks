# Bug Report

### Describe the bug

I'm experiencing unexpected behavior with sidebar categories in Docusaurus. Categories that should be collapsible are being forced to have `collapsed = false`, and categories without subitems are being filtered out incorrectly.

### Reproduction

```js
// Sidebar configuration
{
  type: 'category',
  label: 'My Category',
  collapsible: true,
  collapsed: true,
  items: [
    // ... some items
  ]
}
```

When I set `collapsible: true` and `collapsed: true`, the category always renders as expanded (`collapsed: false`). It seems like collapsible categories are being forced to stay open.

Also, I have some categories with a link but no subitems:

```js
{
  type: 'category',
  label: 'External Link',
  link: {
    type: 'doc',
    id: 'some-doc'
  },
  items: []
}
```

These categories are disappearing from the sidebar entirely, even though they have a valid link. Only categories with `generated-index` type links seem to be getting removed now.

### Expected behavior

- Categories with `collapsible: true` should respect the `collapsed` property
- Categories without subitems but with a valid doc link should still render in the sidebar
- Only empty categories with `generated-index` links (or no link) should be filtered out

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
