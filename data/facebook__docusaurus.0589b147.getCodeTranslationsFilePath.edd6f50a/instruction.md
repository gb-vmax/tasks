# Bug Report

### Describe the bug

The code translations file path is being resolved incorrectly, causing translations to fail loading from the expected location. After a recent change, the translation files are not being found in the localization directory where they should be.

### Reproduction

```js
const context = {
  localizationDir: '/project/i18n/en'
}

// The path should be: /project/i18n/en/code.json
// But it's resolving to something else entirely
const filePath = getCodeTranslationsFilePath(context)
```

When trying to load translations:
1. Set up a localization directory (e.g., `i18n/en`)
2. Place a `code.json` file in that directory
3. Try to load the translations
4. The file is not found because the path resolution is wrong

### Expected behavior

The translation file path should be constructed as `<localizationDir>/code.json`, so for a localization directory of `/project/i18n/en`, it should resolve to `/project/i18n/en/code.json`.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
