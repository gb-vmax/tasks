# Bug Report

### Describe the bug

When using localized content paths in the pages plugin, the content loading order seems to be reversed. The localized content path is being checked before the main content path, which causes unexpected behavior when files exist in both locations.

### Reproduction

```js
// Setup with both content paths:
// - contentPath: 'src/pages'
// - contentPathLocalized: 'i18n/en/docusaurus-plugin-content-pages/current'

// If a page exists in both locations:
// src/pages/example.md
// i18n/en/docusaurus-plugin-content-pages/current/example.md

// The localized version is loaded instead of the main content path version
```

### Expected behavior

The main `contentPath` should take precedence over `contentPathLocalized`, or at minimum they should be processed in a consistent order. Currently it appears the localized path is checked first, which seems backwards.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This might be affecting how pages are resolved when both localized and non-localized versions exist.

---
Repository: /testbed
