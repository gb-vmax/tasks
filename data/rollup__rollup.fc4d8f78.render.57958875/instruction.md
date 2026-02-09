# Bug Report

### Describe the bug

When using `import.meta.url` with file references in my bundle, the generated code is producing invalid JavaScript. The output appears to be cut off or malformed, causing syntax errors when the bundle is executed.

### Reproduction

```js
// input.js
const fileUrl = new URL('./asset.png', import.meta.url);
console.log(fileUrl.href);
```

When bundling this code, the output contains truncated or malformed code that fails to parse. The generated bundle seems to be incomplete and doesn't produce valid JavaScript syntax.

### Expected behavior

The bundler should generate valid JavaScript code that correctly resolves the file URL. The output should be syntactically correct and executable.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This is blocking my build process as the generated bundles are not valid JavaScript and fail to load in the browser.

---
Repository: /testbed
