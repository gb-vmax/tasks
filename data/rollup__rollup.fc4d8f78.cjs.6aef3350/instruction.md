# Bug Report

### Describe the bug

When using `import.meta.ROLLUP_FILE_URL_<referenceId>` in a CommonJS build targeting Node.js environment, the generated code produces incorrect URL format. The URL is being resolved relative to `document.baseURI` instead of using the file protocol, which causes issues since `document` is not available in Node.js.

### Reproduction

```js
// Input code
const url = import.meta.ROLLUP_FILE_URL_0;
console.log(url);

// Build with format: 'cjs'
// When running the output in Node.js (where document is undefined),
// the URL should use file:// protocol but instead tries to use document-based resolution
```

The generated code seems to have the fallback logic reversed - it's trying to use document-based resolution when document is undefined (Node.js environment) instead of using the file protocol approach.

### Expected behavior

In a Node.js environment (where `typeof document === 'undefined'`), the code should generate file:// protocol URLs. In browser environments, it should use document.baseURI for relative URL resolution.

### System Info
- Rollup version: latest
- Output format: cjs
- Environment: Node.js

---
Repository: /testbed
