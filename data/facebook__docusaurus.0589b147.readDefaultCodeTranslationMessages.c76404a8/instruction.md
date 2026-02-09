# Bug Report

### Describe the bug

When loading translation files, the function tries to read a file that doesn't exist instead of returning an empty object when no translation files are found. This causes the application to crash with a file not found error.

### Reproduction

```js
// Set up a scenario where no translation files exist for the requested locale
const result = await readDefaultCodeTranslationMessages({
  dirPath: '/path/to/translations',
  locale: 'fr_FR',
  name: 'theme-common'
});

// Expected: returns {}
// Actual: throws error trying to read non-existent file
```

### Steps to reproduce:
1. Configure a locale that doesn't have any translation files (e.g., `fr_FR`)
2. Ensure the fallback locale files also don't exist
3. Try to load the code translations
4. Application crashes instead of gracefully returning an empty object

### Expected behavior

When no translation files are found for any of the attempted locales, the function should return an empty object `{}` instead of attempting to read a non-existent file.

### Additional context

This appears to be a regression - the previous behavior was to return an empty object when no files were found, which allowed the application to continue with default/untranslated strings.

---
Repository: /testbed
