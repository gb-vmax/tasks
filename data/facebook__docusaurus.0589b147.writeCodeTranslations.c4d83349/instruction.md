# Bug Report

### Describe the bug

The `writeCodeTranslations` function seems to be passing incorrect parameters to `writeTranslationFileContent`. When trying to write code translations, the function is using `options` instead of `context` to get the file path, and it's also modifying the content object in an unexpected way by merging `context` into it.

### Reproduction

```js
// When calling writeCodeTranslations
await writeCodeTranslations(
  translationContent,
  context,
  options
);

// The file path is computed from options instead of context
// And the content gets merged with context object
```

### Expected behavior

The function should:
1. Use `context` parameter to determine the correct file path via `getCodeTranslationsFilePath(context)`
2. Pass the `content` directly without modifying it

### System Info
- Docusaurus version: latest
- Node version: 18.x

This appears to have broken the translation file generation, as the files are being written to incorrect locations and with malformed content structure.

---
Repository: /testbed
