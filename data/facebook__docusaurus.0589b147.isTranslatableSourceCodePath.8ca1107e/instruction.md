# Bug Report

### Describe the bug

Translation extraction is failing for source code files with certain file extensions. After a recent update, files that should be detected as translatable are being skipped during the translation extraction process.

### Reproduction

Create a source file with a translatable extension:

```
src/
  components/
    MyComponent.tsx
    AnotherComponent.js
```

When running the translation extraction, these files are not being recognized as translatable source code files even though `.tsx` and `.js` are in the supported extensions list.

### Expected behavior

Files with extensions `.js`, `.jsx`, `.ts`, `.tsx` should be detected as translatable source code and processed for translation extraction.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
