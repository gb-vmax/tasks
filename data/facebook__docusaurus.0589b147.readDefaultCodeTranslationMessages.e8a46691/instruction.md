# Bug Report

### Describe the bug

The translation system is not loading locale-specific translation files correctly. When trying to load translations for a specific locale (e.g., `fr_FR`), the system fails to check the correct file paths and returns an empty object immediately instead of trying fallback locales.

### Reproduction

```js
// Attempting to load translations for French (France)
const translations = await readDefaultCodeTranslationMessages({
  dirPath: '/path/to/translations',
  locale: 'fr_FR',
  name: 'theme-common'
});

// Expected: Should try fr_FR/theme-common.json, then fr/theme-common.json
// Actual: Only checks theme-common.json in the base directory, then returns empty object
```

### Expected behavior

The translation loading should follow the locale fallback chain:
1. First try the exact locale file (e.g., `fr_FR/theme-common.json`)
2. If not found, try the base locale (e.g., `fr/theme-common.json`)
3. Only return empty object if none of the fallback locales have the file

Currently it seems to be ignoring the locale directory structure entirely and just checking for files in the base directory.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is breaking our multi-locale site where we have region-specific translations organized in subdirectories.

---
Repository: /testbed
