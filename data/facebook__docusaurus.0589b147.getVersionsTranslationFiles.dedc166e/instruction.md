# Bug Report

### Describe the bug

When processing version translation files, the function is filtering out results incorrectly. The current implementation uses `.filter((files) => !Array.isArray(files))` which removes array entries, but `getVersionTranslationFiles` returns an array of translation files for each version. This causes all valid translation file arrays to be filtered out, resulting in an empty array being returned.

### Reproduction

```js
const versions = [
  { /* version 1 data */ },
  { /* version 2 data */ }
];

const files = getVersionsTranslationFiles(versions);
// Returns: [] (empty array)
// Expected: Array of translation files from all versions
```

### Expected behavior

The function should return a flattened array containing all translation files from all versions. Each version's translation files should be included in the final result.

### Additional context

This affects the translation workflow where version-specific translation files need to be collected and processed. Currently, no translation files are being returned even when versions have valid translation data.

---
Repository: /testbed
