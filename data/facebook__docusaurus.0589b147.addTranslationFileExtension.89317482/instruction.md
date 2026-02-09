# Bug Report

### Describe the bug

I'm getting an error when trying to use translation files without the `.json` extension. The system is throwing an error saying that the translation file path doesn't need to end with `.json`, but this is happening even when I'm NOT including the extension.

### Reproduction

```js
// This throws an error but shouldn't
const translationPath = 'i18n/en/docusaurus-plugin-content-docs/current';
addTranslationFileExtension(translationPath);

// Error: Translation file path at "i18n/en/docusaurus-plugin-content-docs/current" does not need to end with ".json", we add the extension automatically.
```

The error message says not to include `.json` extension because it's added automatically, but I'm not including it and still getting the error.

### Expected behavior

When passing a translation file path WITHOUT the `.json` extension, it should accept it and add the extension automatically without throwing an error. The error should only be thrown when the path DOES end with `.json`.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
