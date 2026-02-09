# Bug Report

### Describe the bug

Translation files are not being loaded correctly. When trying to use localized translations, the system fails to read the translation JSON files even when they exist in the correct directory structure.

### Reproduction

```js
// Set up a locale directory with translation files
// locales/fr/common.json exists and contains valid translations

await readDefaultCodeTranslationMessages({
  dirPath: './locales',
  locale: 'fr',
  name: 'common'
});

// Expected: Returns the translations from fr/common.json
// Actual: Returns undefined/empty, translations not loaded
```

### Steps to reproduce:
1. Create a translation file in the proper locale directory (e.g., `locales/fr/common.json`)
2. Call `readDefaultCodeTranslationMessages` with the correct parameters
3. The function fails to return the translation content even though the file exists

### Expected behavior

The function should read and return the content of the first matching translation file. For example, when requesting `fr_FR` locale, it should try `fr_FR.json` first, then fall back to `fr.json`, and return the content of whichever file exists.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have broken recently - translations were working fine before. The fallback logic for locale matching doesn't seem to be functioning as expected.

---
Repository: /testbed
