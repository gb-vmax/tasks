# Bug Report

### Describe the bug

Translation extraction warnings are being logged incorrectly. When there are actual warnings for a source code file, the warning message displays the file path twice instead of showing the actual warning messages.

### Reproduction

```js
// When extracting translations from a file with warnings
const sourceCodeFilesTranslations = [{
  sourceCodeFilePath: '/path/to/file.js',
  warnings: ['Missing translation key', 'Duplicate ID found']
}];

// The logged output shows:
// "Translation extraction warnings for file path=/path/to/file.js: /path/to/file.js"
// 
// Instead of the expected:
// "Translation extraction warnings for file path=/path/to/file.js: Missing translation key,Duplicate ID found"
```

### Expected behavior

The warning logger should display the actual warning messages, not repeat the file path. This makes it impossible to see what the actual translation extraction issues are.

### Additional context

This appears to affect all translation extraction warnings, making it difficult to debug translation issues in the codebase. The warnings array contains the actual warning messages but they're not being displayed in the log output.

---
Repository: /testbed
