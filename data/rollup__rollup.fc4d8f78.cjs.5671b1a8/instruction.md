# Bug Report

### Describe the bug

When using `import.meta.ROLLUP_FILE_URL_referenceId` in a CommonJS bundle, the generated code produces incorrect URLs depending on the environment. The URL resolution logic appears to be inverted between Node.js and browser environments.

### Reproduction

```js
// Input code
const assetUrl = new URL('asset.png', import.meta.url);

// Bundle with format: 'cjs'
// In Node.js environment: Returns document-based URL (incorrect)
// In browser environment: Returns file:// URL (incorrect)
```

The generated code seems to swap the URL resolution mechanisms between the two environments. When `typeof document === 'undefined'` (Node.js), it's using the document-based resolution, and when document is available (browser), it's using the file:// protocol resolution.

### Expected behavior

- In Node.js (where `typeof document === 'undefined'`): Should use `file://` protocol with `pathToFileURL`
- In browser (where document is available): Should use document-based relative URL resolution

### System Info

- Rollup version: latest
- Output format: cjs
- Node version: 18.x

This is causing issues when trying to load assets in universal/isomorphic code that needs to work in both Node.js and browser environments.

---
Repository: /testbed
