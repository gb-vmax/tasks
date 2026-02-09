# Bug Report

### Describe the bug

I'm experiencing an issue with translation file loading where accessing translation files results in a ReferenceError. The application crashes when trying to read translation files, even when the files exist and are valid.

### Reproduction

```js
// When readTranslationFileContent is called with a valid translation file path
const translationContent = await readTranslationFileContent('/path/to/i18n/en/translation.json');
// ReferenceError: content is not defined
```

This happens when:
1. A translation file exists at the specified path
2. The file contains valid JSON
3. The function attempts to return the content

### Expected behavior

The function should successfully read and return the translation file content without throwing a ReferenceError. Valid translation files should be loaded properly and made available to the application.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
