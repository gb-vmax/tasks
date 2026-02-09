# Bug Report

### Describe the bug

When a translation file doesn't exist, the system is throwing an error instead of handling it gracefully. This breaks the build process when optional translation files are missing.

### Reproduction

```js
// Try to read a translation file that doesn't exist
const translationContent = await readTranslationFileContent('/path/to/missing/translation.json');
// Expected: undefined
// Actual: throws Error "Translation file not found at path=..."
```

### Expected behavior

When a translation file doesn't exist, `readTranslationFileContent` should return `undefined` to allow the system to handle missing translations gracefully. This was the previous behavior and many setups rely on translation files being optional.

### Additional context

This seems to have started happening recently. The function used to return `undefined` when a file didn't exist, but now it's throwing an error which causes builds to fail when translation files are not present.

---
Repository: /testbed
