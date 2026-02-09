# Bug Report

### Describe the bug

Translation extraction is not working for source code files. Files that should be detected as translatable are being skipped during the translation extraction process.

### Reproduction

Create a project with the following structure:
```
src/
  components/
    MyComponent.tsx
    MyComponent.js
  pages/
    index.jsx
```

When running the translation extraction, these files are not being picked up as translatable source code files even though they have valid extensions (`.tsx`, `.js`, `.jsx`).

### Expected behavior

Files with extensions like `.js`, `.jsx`, `.ts`, `.tsx` should be detected as translatable source code and processed during translation extraction. The extension check should properly identify these file types regardless of the file path.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
