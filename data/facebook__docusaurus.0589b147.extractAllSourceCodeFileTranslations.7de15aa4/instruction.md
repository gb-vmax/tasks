# Bug Report

### Describe the bug

When extracting translations from multiple source code files, only the first file to complete is being processed. All other translation files are being ignored, resulting in incomplete translation extraction across the codebase.

### Reproduction

```js
// Create multiple files with translations
// file1.js
<Translate>Hello World</Translate>

// file2.js
<Translate>Goodbye World</Translate>

// file3.js
<Translate>Welcome</Translate>

// Run translation extraction
// Only translations from the fastest file to process are extracted
// Other files' translations are missing from the output
```

### Expected behavior

All translation strings from all source code files should be extracted and included in the translation output. The extraction process should wait for all files to be processed, not just the first one that completes.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is causing major issues with our i18n setup as most of our translations are not being detected.

---
Repository: /testbed
