# Bug Report

### Describe the bug

I'm experiencing an issue with navbar items that have nested subitems. It seems like only the first subitem in each dropdown menu is being processed/translated, while all other subitems are being ignored.

### Reproduction

```js
// navbar configuration with nested items
const navbar = {
  items: [
    {
      label: 'Docs',
      items: [
        { label: 'Getting Started', to: '/docs/intro' },
        { label: 'API Reference', to: '/docs/api' },
        { label: 'Guides', to: '/docs/guides' }
      ]
    }
  ]
}
```

When using the above configuration, only "Getting Started" appears to be included in the translation file generation, while "API Reference" and "Guides" are missing.

### Expected behavior

All navbar items and their subitems should be flattened and included for translation, regardless of how deeply nested they are or how many subitems exist at each level.

### System Info
- Docusaurus version: latest
- Theme: classic

---
Repository: /testbed
