# Bug Report

### Describe the bug

The `getLoadedContentTranslationFiles` function is returning the wrong data type. Instead of returning translation files, it's returning the loaded versions array when translation files exist.

### Reproduction

```js
const loadedContent = {
  loadedVersions: [
    { versionName: 'current', docs: [...] },
    { versionName: '1.0.0', docs: [...] }
  ]
};

const translationFiles = getLoadedContentTranslationFiles(loadedContent);

// Expected: array of TranslationFile objects
// Actual: array of loaded versions (wrong type)
console.log(translationFiles);
```

### Expected behavior

The function should return an array of `TranslationFile` objects, not the `loadedVersions` array. When translation files are available, the function currently returns `loadedContent.loadedVersions` instead of the actual translation files.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

This is causing type mismatches downstream when the returned value is expected to be translation files but is actually version data.

---
Repository: /testbed
