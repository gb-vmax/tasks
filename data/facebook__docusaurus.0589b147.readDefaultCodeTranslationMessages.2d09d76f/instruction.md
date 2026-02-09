# Bug Report

### Describe the bug

Translation files are not being loaded correctly. After updating, the application fails to load any translation messages and falls back to default language even when translation files exist.

### Reproduction

```js
// Setup translation files in the following structure:
// locales/
//   en.json
//   fr.json
//   fr_FR.json

// Try to load French translations
const messages = await readDefaultCodeTranslationMessages({
  locale: 'fr_FR',
  dirPath: './locales',
  name: 'common'
});

// Expected: Should load fr_FR.json or fall back to fr.json
// Actual: Returns empty/undefined, no translations loaded
```

### Expected behavior

When requesting translations for a locale like `fr_FR`, the system should:
1. First try to load `fr_FR.json`
2. If not found, fall back to `fr.json`
3. Return the translation messages from the first file that exists

Currently, translation files that exist are being ignored and the function returns nothing.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
