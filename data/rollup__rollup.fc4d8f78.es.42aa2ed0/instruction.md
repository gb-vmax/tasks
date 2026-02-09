# Bug Report

### Describe the bug

When using `import.meta.url` with relative file URLs in ES module format, the generated code is incorrect. The `import.meta.url` is being treated as a string literal instead of an actual reference to the meta property, and the boolean flag for object conversion appears to be inverted.

### Reproduction

```js
// In an ES module bundle with import.meta.ROLLUP_FILE_URL_referenceId
// The generated output incorrectly wraps import.meta.url in quotes
// and inverts the asObject parameter

// Example: Using new URL with import.meta.url
const fileUrl = new URL('./asset.png', import.meta.url);

// Expected generated code should reference import.meta.url directly
// But instead it's generating code with 'import.meta.url' as a string
```

### Expected behavior

The generated code should:
1. Reference `import.meta.url` directly without wrapping it in quotes
2. Preserve the correct boolean value for the asObject parameter (not inverted)

This affects any code that uses `import.meta.ROLLUP_FILE_URL_*` patterns in ES module output format.

### System Info
- Rollup version: latest
- Output format: ES modules

---
Repository: /testbed
