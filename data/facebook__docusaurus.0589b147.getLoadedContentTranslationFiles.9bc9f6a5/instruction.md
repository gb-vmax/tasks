# Bug Report

### Describe the bug

After updating to the latest version, the docs plugin is not loading any translation files. When I check the loaded content, the translation files array is completely empty even though I have properly configured translation files in my project.

### Reproduction

```js
// In my docusaurus.config.js I have:
i18n: {
  defaultLocale: 'en',
  locales: ['en', 'fr', 'es'],
}

// And I have translation files in:
// i18n/fr/docusaurus-plugin-content-docs/current.json
// i18n/es/docusaurus-plugin-content-docs/current.json
```

When building or starting the dev server, none of the translation files are being loaded. The build completes without errors but the translated versions of the docs are missing all the translated sidebar labels and version labels.

### Expected behavior

The translation files should be loaded and applied to the docs. The sidebar and version labels should appear in the correct language when switching locales.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This was working fine in the previous version. I suspect something changed in how translation files are being filtered or loaded.

---
Repository: /testbed
