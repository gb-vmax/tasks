# Bug Report

### Describe the bug

I'm experiencing an issue with `import.meta.url` and `import.meta.ROLLUP_FILE_URL_*` where the necessary global variables are not being properly tracked/injected in the output. This seems to affect certain module formats where these meta properties should be accessing document or URL-related globals.

### Reproduction

When using `import.meta.url` in a module:

```js
// input.js
const moduleUrl = import.meta.url;
console.log(moduleUrl);
```

The bundled output is missing the required global variable declarations that should be added for the target format. This causes runtime errors when the code tries to access these properties.

Similarly, when using file URL references:

```js
const fileUrl = import.meta.ROLLUP_FILE_URL_0;
```

The expected globals are not being injected into the output bundle.

### Expected behavior

The bundler should automatically inject the necessary global variable declarations (like `document.currentScript`, `URL`, etc.) when `import.meta.url` or `import.meta.ROLLUP_FILE_URL_*` are used, depending on the output format.

### System Info

- Rollup version: latest
- Output format: multiple formats affected (cjs, iife, umd)

This seems like it might be related to how the meta properties are being resolved during the bundling process.

---
Repository: /testbed
