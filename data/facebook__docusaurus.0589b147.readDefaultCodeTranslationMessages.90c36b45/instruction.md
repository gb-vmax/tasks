# Bug Report

### Describe the bug

When loading translation files, the fallback locale mechanism is not working correctly. The system checks for the existence of translation files using one locale path but then attempts to read from a different locale path, causing translations to fail to load even when fallback files exist.

### Reproduction

```js
// Assume we have the following file structure:
// locales/
//   fr/
//     code.json (exists)
//   fr_FR/
//     (no code.json)

// When trying to load translations for fr_FR locale
await readDefaultCodeTranslationMessages({
  locale: 'fr_FR',
  dirPath: 'locales',
  name: 'code'
});

// Expected: Should fall back to fr/code.json
// Actual: Fails to load translations even though fr/code.json exists
```

### Steps to reproduce

1. Set up a translations directory with a base locale file (e.g., `fr/code.json`)
2. Don't create the regional variant file (e.g., `fr_FR/code.json`)
3. Try to load translations for the regional variant locale (`fr_FR`)
4. The translation loading fails despite the fallback file being available

### Expected behavior

The system should properly fall back to the base locale translation file (e.g., `fr/code.json`) when the regional variant (e.g., `fr_FR/code.json`) doesn't exist. The fallback chain should work as documented: `fr_FR.json` => `fr.json` => nothing.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
