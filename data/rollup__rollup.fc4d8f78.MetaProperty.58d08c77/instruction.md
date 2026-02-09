# Bug Report

### Describe the bug

I'm experiencing an issue with `import.meta` file references where the wrong file path is being resolved. When using `import.meta.ROLLUP_FILE_URL_*` pattern, the output seems to be incorrectly extracting the file reference ID, resulting in broken file URLs in the generated bundle.

### Reproduction

```js
// In my source file:
const fileUrl = import.meta.ROLLUP_FILE_URL_abc123;

// Expected: Should resolve to the correct file URL for reference 'abc123'
// Actual: Getting incorrect or malformed URL
```

This appears to happen specifically when using the `ROLLUP_FILE_URL_` prefix pattern. The `import.meta.url` works fine, but the file URL references are broken.

### Expected behavior

The file reference ID should be correctly extracted from the meta property string, and the corresponding file URL should be properly resolved in the output.

### Additional context

This seems to have started recently. Not sure if it's related to a recent change in how meta properties are parsed, but the file references are definitely not being handled correctly anymore.

---
Repository: /testbed
