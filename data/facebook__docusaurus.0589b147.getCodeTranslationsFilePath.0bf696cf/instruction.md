# Bug Report

Title: Translation file path resolves incorrectly - only using directory name instead of full path

### Describe the bug
I'm experiencing an issue with translation file paths in my Docusaurus site. The code translation files are not being found at the expected location. It seems like the path is being constructed using only the directory name instead of the full path.

### Reproduction
```js
// Set up a localization directory like:
// /path/to/my/project/i18n/fr/

// When trying to load code translations, the system looks for:
// fr/code.json
// instead of:
// /path/to/my/project/i18n/fr/code.json
```

Steps to reproduce:
1. Set up a Docusaurus project with i18n enabled
2. Create a localization directory with a full path (e.g., `/absolute/path/to/i18n/fr`)
3. Try to use code translations
4. The translation files are not found because the path only includes the basename

### Expected behavior
The code translation file path should use the complete localization directory path, not just the directory name. The system should be able to locate translation files regardless of where the localization directory is located in the filesystem.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is blocking our i18n implementation as translation files cannot be loaded properly.

---
Repository: /testbed
