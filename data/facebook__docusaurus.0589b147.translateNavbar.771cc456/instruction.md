# Bug Report

### Describe the bug

After a recent update, navbar items are showing `undefined` labels when translations are missing, instead of falling back to the original label text. This breaks the navbar display for items that don't have explicit translations defined.

### Reproduction

```js
// theme config
navbar: {
  items: [
    {
      label: 'Docs',
      to: '/docs'
    },
    {
      label: 'Blog',
      to: '/blog'
    }
  ]
}

// No translations provided for these labels
```

When the navbar renders, items without translations now show as blank/undefined instead of displaying their original label values.

### Expected behavior

Navbar items should fall back to their original `label` property when no translation is available, maintaining backwards compatibility with sites that don't have all translations defined.

### System Info
- Docusaurus version: latest
- Theme: @docusaurus/theme-classic

---
Repository: /testbed
