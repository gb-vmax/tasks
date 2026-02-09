# Bug Report

### Describe the bug

I'm experiencing an issue with translation extraction where source code files are not being properly detected for translation. After some investigation, it seems like the files that should be translatable are being excluded instead of included.

### Reproduction

```js
// When trying to extract translations from source files
const dirPaths = ['src/pages', 'src/components'];
const result = await globSourceCodeFilePaths(dirPaths);

// Expected: Should return translatable files like .js, .jsx, .tsx files
// Actual: Returns empty array or non-translatable files
```

### Steps to reproduce:
1. Set up a Docusaurus project with some translatable content in source files
2. Run translation extraction on directories containing source code
3. Notice that translatable source files are not being picked up

### Expected behavior

The `globSourceCodeFilePaths` function should return all translatable source code files (like .js, .jsx, .tsx files) from the specified directories. These files should then be processed for translation extraction.

### Actual behavior

The function appears to be filtering out the translatable files instead of keeping them, resulting in no source files being extracted for translations.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
