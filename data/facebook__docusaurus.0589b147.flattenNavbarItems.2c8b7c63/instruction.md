# Bug Report

### Describe the bug

The navbar translation extraction is not working correctly for nested navbar items. When I have dropdown menus or nested navigation structures, only the top-level items appear to be processed, and the nested/child items are being skipped or duplicated infinitely.

### Reproduction

```js
const navbar = {
  items: [
    {
      label: 'Docs',
      items: [
        { label: 'Getting Started', to: '/docs/intro' },
        { label: 'API Reference', to: '/docs/api' }
      ]
    },
    {
      label: 'Community',
      items: [
        { label: 'Discord', href: 'https://discord.gg/...' }
      ]
    }
  ]
}

// When extracting translations, nested items under 'Docs' and 'Community' 
// are not being included properly
```

### Expected behavior

All navbar items, including deeply nested dropdown items, should be extracted for translation. The flattening function should recursively process all levels of the navigation hierarchy.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
