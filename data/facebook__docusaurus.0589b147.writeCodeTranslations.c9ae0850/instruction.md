# Bug Report

### Describe the bug

Getting a runtime error when trying to write code translations. The translation file generation is failing because an incorrect parameter is being passed to `getCodeTranslationsFilePath()`.

### Reproduction

```js
await writeCodeTranslations(
  context,
  {
    'theme.common.skipToMainContent': {
      message: 'Skip to main content',
      description: 'The skip to content label used for accessibility'
    }
  },
  { messagePrefix: 'custom' }
);
```

The function crashes because `content` (the translations object) is being passed to `getCodeTranslationsFilePath()` instead of `context` (the site context object).

### Expected behavior

The function should successfully write the translation file using the correct context parameter to determine the file path.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
