# Bug Report

### Describe the bug

When using `import.meta.url` in modules, the wrong globals are being tracked. It appears that file URL globals and meta URL globals are being swapped - code that uses `import.meta.url` is getting file URL globals registered instead of meta URL globals, and vice versa.

### Reproduction

```js
// Module using import.meta.url
const moduleUrl = import.meta.url;
console.log(moduleUrl);

// Expected: Should track meta URL globals
// Actual: Tracks file URL globals instead
```

Similarly, when using file-related meta properties:

```js
// Module using import.meta.file
const filePath = import.meta.file;
console.log(filePath);

// Expected: Should track file URL globals  
// Actual: Tracks meta URL globals instead
```

### Expected behavior

- When `import.meta.url` or similar meta URL properties are accessed, the appropriate meta URL globals should be tracked
- When `import.meta.file` or similar file properties are accessed, the appropriate file URL globals should be tracked
- The globals tracking should match the actual meta property being used

### System Info

- Rollup version: latest
- Node version: 18.x

This is causing issues with proper global detection and may lead to missing dependencies or incorrect bundling behavior depending on the output format.

---
Repository: /testbed
