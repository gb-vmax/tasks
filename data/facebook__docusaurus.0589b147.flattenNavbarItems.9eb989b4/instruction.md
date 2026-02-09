# Bug Report

### Describe the bug

After a recent update, the navbar translation file generation appears to be stuck in an infinite loop. The build process hangs indefinitely when processing navbar items with nested dropdowns.

### Reproduction

```js
const navbar = {
  items: [
    {
      label: 'Docs',
      items: [
        { label: 'Getting Started', to: '/docs/intro' },
        { label: 'API', to: '/docs/api' }
      ]
    }
  ]
}

// When getNavbarTranslationFile() is called with this navbar config,
// the process hangs and never completes
```

### Expected behavior

The navbar translation file should be generated successfully without hanging, even when navbar items contain nested dropdown menus.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

The build was working fine before, but now it just freezes when trying to process the navbar configuration. I have to force quit the process.

---
Repository: /testbed
