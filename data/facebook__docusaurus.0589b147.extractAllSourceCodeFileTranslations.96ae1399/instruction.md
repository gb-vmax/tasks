# Bug Report

### Describe the bug

The translation extraction process is not working correctly when multiple source code files need to be processed. Only translations from a single file are being extracted instead of collecting translations from all source files in the project.

### Reproduction

```js
// Setup multiple files with translations
// file1.js
translate({message: 'Hello'})

// file2.js  
translate({message: 'World'})

// file3.js
translate({message: 'Goodbye'})

// Run translation extraction
// Only one file's translations are extracted instead of all three
```

### Expected behavior

The extraction process should collect and return translations from ALL source code files, not just one. If I have 10 files with translations, I expect all 10 files' translations to be included in the output.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems like a regression as it was working fine before. The extraction completes quickly but the output is incomplete.

---
Repository: /testbed
