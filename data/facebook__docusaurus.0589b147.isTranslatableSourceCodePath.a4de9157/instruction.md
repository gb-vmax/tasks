# Bug Report

### Describe the bug

Translation extraction is not working for source code files with uppercase file extensions. Files like `component.JS`, `module.TS`, or `page.TSX` are being skipped during the translation extraction process, even though they contain translatable content.

### Reproduction

1. Create a TypeScript/JavaScript file with an uppercase extension (e.g., `MyComponent.TSX`)
2. Add translatable content using the `translate` API:
```tsx
// MyComponent.TSX
import Translate from '@docusaurus/Translate';

export default function MyComponent() {
  return <Translate>Hello World</Translate>;
}
```
3. Run the translation extraction
4. The translations from `MyComponent.TSX` are not extracted

### Expected behavior

Translation extraction should work regardless of the case of the file extension. Both `.tsx` and `.TSX` (or `.js`/`.JS`, `.ts`/`.TS`, etc.) should be treated the same way and have their translations extracted.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: Windows/macOS

This seems to affect Windows users more commonly since Windows file systems are case-insensitive but the file extensions can still be displayed in uppercase.

---
Repository: /testbed
