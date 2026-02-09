# Bug Report

### Describe the bug

I'm encountering an issue with version translation files where versions without a name property are causing problems. After a recent update, it seems like the translation file generation is not working correctly when dealing with multiple versions.

### Reproduction

```js
const versions = [
  { name: 'current', docs: [...] },
  { name: '', docs: [...] },  // Empty name
  { name: 'v1.0', docs: [...] }
]

// When generating translation files
const translationFiles = getVersionsTranslationFiles(versions)
```

### Expected behavior

The function should handle all versions correctly and return a flat array of translation files, even when some versions have empty or missing name properties. Currently it seems like the logic has changed and versions are being filtered instead of processed, which might cause translation files to be missing.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
