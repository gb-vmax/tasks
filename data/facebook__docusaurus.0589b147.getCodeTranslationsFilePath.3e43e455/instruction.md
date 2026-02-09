# Bug Report

### Describe the bug

I'm experiencing an issue with translation files not being read from the correct directory. After a recent update, the code translation file path seems to be resolved incorrectly, causing translations to fail loading.

### Reproduction

```js
// Set up a Docusaurus site with i18n configured
// Project structure:
// my-site/
//   ├── i18n/
//   │   └── fr/
//   │       └── code.json
//   └── docusaurus.config.js

// Expected: code.json should be read from i18n/fr/
// Actual: code.json is being looked up in the wrong directory
```

When trying to use translations, the system appears to be looking for `code.json` in the base directory instead of the localization directory (e.g., `i18n/fr/`).

### Expected behavior

The translation file should be read from `i18n/<locale>/code.json` where the localization directory is properly resolved relative to the project structure.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is breaking our internationalization setup. Any help would be appreciated!

---
Repository: /testbed
