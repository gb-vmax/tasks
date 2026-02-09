# Bug Report

### Describe the bug

I'm having an issue with navbar dropdown translations. When a navbar item has subitems (dropdown menu), the translation keys for those subitems are being resolved incorrectly. Instead of using the subitem's own label to look up the translation, it seems like the parent item's label is being used for all subitems.

### Reproduction

```js
// In my navbar config:
{
  type: 'dropdown',
  label: 'Resources',
  items: [
    { label: 'Docs', to: '/docs' },
    { label: 'Blog', to: '/blog' },
    { label: 'Community', to: '/community' }
  ]
}

// Translation keys defined:
{
  'item.label.Resources': { message: 'Ressourcen' },
  'item.label.Docs': { message: 'Dokumentation' },
  'item.label.Blog': { message: 'Blog' },
  'item.label.Community': { message: 'Gemeinschaft' }
}
```

### Expected behavior

Each subitem should use its own label to look up the correct translation key. So "Docs" should look for `item.label.Docs`, "Blog" should look for `item.label.Blog`, etc.

### Actual behavior

All subitems appear to be using the parent item's label for translation lookup. In the example above, all subitems would try to use `item.label.Resources` instead of their individual translation keys, causing them to display their original English labels instead of the translated versions.

### System Info

- Docusaurus version: Latest
- Node version: 18.x

---
Repository: /testbed
