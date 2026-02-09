# Bug Report

### Describe the bug

When using nested navbar items with translations, the sub-items are not getting translated correctly. It seems like the translation system is looking up the wrong key for nested menu items - it's using the parent item's label instead of the sub-item's label for the translation lookup.

### Reproduction

```js
// In your navbar config
navbar: {
  items: [
    {
      label: 'Docs',
      items: [
        { label: 'Getting Started', to: '/docs/intro' },
        { label: 'API Reference', to: '/docs/api' }
      ]
    }
  ]
}

// In your translation file
{
  "item.label.Getting Started": { "message": "Démarrage" },
  "item.label.API Reference": { "message": "Référence API" }
}
```

### Expected behavior

The sub-items should use their own labels for translation lookups. So "Getting Started" should be translated to "Démarrage" and "API Reference" should be translated to "Référence API".

### Actual behavior

All sub-items are trying to use the parent item's label ("Docs") for translation lookup, so they don't get translated at all and just show the default English labels.

This is affecting multi-language sites where dropdown menus need to be localized properly.

---
Repository: /testbed
