# Bug Report

### Describe the bug

Translation extraction is not working properly for source code files. It appears that files with translatable extensions (like `.js`, `.jsx`, `.ts`, `.tsx`) are being incorrectly filtered out and not processed for translation extraction.

### Reproduction

```js
// Given a project structure with translatable source files:
// src/components/MyComponent.tsx
// src/pages/index.js

// When running translation extraction, these files are skipped
// even though they have valid translatable extensions
```

Steps to reproduce:
1. Create a Docusaurus site with source files that should be translatable (`.js`, `.jsx`, `.ts`, `.tsx`)
2. Add translatable content to these files using the translation APIs
3. Run the translation extraction process
4. Notice that translations from these source files are not being extracted

### Expected behavior

Source code files with extensions in the `TranslatableSourceCodeExtension` set (`.js`, `.jsx`, `.ts`, `.tsx`) should be included in the translation extraction process. The filter should correctly identify these files and process them for extracting translation strings.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
