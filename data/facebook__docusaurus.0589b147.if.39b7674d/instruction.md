# Bug Report

### Describe the bug

When trying to load translation files, I'm getting unexpected behavior where the system attempts to read JSON files that don't exist. This results in errors being thrown when the translation file path doesn't exist on the filesystem.

### Reproduction

```js
// Attempt to load a translation file that doesn't exist
const translationContent = await readTranslationFileContent('/path/to/nonexistent/translation.json');

// Expected: Should return undefined
// Actual: Throws an error trying to read a non-existent file
```

### Expected behavior

When a translation file path doesn't exist, the function should return `undefined` without attempting to read the file. The system should only try to read and parse JSON when the file actually exists.

### Additional context

This seems to be causing issues during the build process when optional translation files are missing. The build fails instead of gracefully handling missing translation files.

---
Repository: /testbed
