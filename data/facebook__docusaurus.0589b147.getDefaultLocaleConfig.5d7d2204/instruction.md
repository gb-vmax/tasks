# Bug Report

### Describe the bug

I'm experiencing an issue with locale configuration where the `path` property is being set incorrectly. Instead of using the locale code (e.g., 'en', 'fr', 'ar'), it appears to be using the text direction value ('ltr' or 'rtl').

### Reproduction

When initializing i18n with a locale, the generated locale config has the wrong path:

```js
const localeConfig = getDefaultLocaleConfig('ar');
// Expected: { path: 'ar', direction: 'rtl', ... }
// Actual: { path: 'rtl', direction: 'rtl', ... }
```

This affects URL generation and routing for localized pages. For example, Arabic content should be accessible at `/ar/...` but instead tries to use `/rtl/...`.

### Expected behavior

The `path` property in the locale config should be set to the actual locale code, not the text direction. Each locale should have its own unique path based on its locale identifier.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
