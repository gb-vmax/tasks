# Bug Report

### Describe the bug

The navbar translation file generation is getting stuck in an infinite loop when processing nested navbar items. The browser becomes unresponsive when trying to load pages with nested navigation menus.

### Reproduction

```js
const navbar = {
  items: [
    {
      label: 'Docs',
      items: [
        { label: 'Getting Started' },
        { label: 'API Reference' }
      ]
    }
  ]
}

// When getNavbarTranslationFile() is called with this navbar config,
// it hangs indefinitely
```

### Steps to reproduce:
1. Create a navbar configuration with nested items
2. Try to generate translation files
3. The process hangs and never completes

### Expected behavior

The function should recursively flatten all nested navbar items and extract their labels for translation, completing in a reasonable amount of time.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is blocking our ability to use nested navigation menus with i18n support. Any help would be appreciated!

---
Repository: /testbed
