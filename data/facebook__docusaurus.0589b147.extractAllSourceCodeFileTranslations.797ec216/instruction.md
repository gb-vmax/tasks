# Bug Report

### Describe the bug

After a recent update, translation extraction is only processing a single source file instead of all source files in the project. It appears that only one translation file is being generated, and the rest are being ignored completely.

### Reproduction

```js
// Given multiple source files with translations:
// - src/pages/index.js (has translations)
// - src/pages/about.js (has translations)
// - src/components/Header.js (has translations)

// Run translation extraction
// Expected: All 3 files should have their translations extracted
// Actual: Only 1 file's translations are extracted (seemingly random which one)
```

Steps to reproduce:
1. Have multiple source files with `<Translate>` components or translation calls
2. Run the translation extraction process
3. Check the generated translation files
4. Notice that translations from most files are missing

### Expected behavior

All source code files should be processed and their translations should be extracted. Previously, translations from all files were being collected correctly.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

This is blocking our i18n workflow as we can't extract translations from all our source files anymore.

---
Repository: /testbed
