# Bug Report

### Describe the bug

I'm experiencing an issue with translation file paths in Docusaurus. The code translations file is being written to an incorrect location - it appears to be going to the parent directory of the localization directory instead of inside it.

### Reproduction

```js
// When the localizationDir is set to something like:
// /my-project/i18n/en

// The code translations file ends up at:
// /my-project/code.json/
// instead of:
// /my-project/i18n/en/code.json
```

Steps to reproduce:
1. Set up a Docusaurus project with i18n enabled
2. Configure localization directory (e.g., `i18n/en`)
3. Try to write code translations
4. Check where the `code.json` file is created

### Expected behavior

The code translations file should be created inside the localization directory (e.g., `/i18n/en/code.json`), not in its parent directory with a trailing separator appended to the filename.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems like it might have been introduced in a recent change. The file path construction looks off.

---
Repository: /testbed
