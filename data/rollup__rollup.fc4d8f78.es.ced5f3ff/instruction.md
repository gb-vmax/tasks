# Bug Report

### Describe the bug

When using `import.meta.ROLLUP_FILE_URL_<referenceId>` in ES module output format, the generated code produces incorrect URL strings. The file path appears to be escaped twice, resulting in malformed URLs with double-escaped characters.

### Reproduction

```js
// Input code
const url = import.meta.ROLLUP_FILE_URL_0;
console.log(url);

// Generated ES output (incorrect)
// The URL string contains double-escaped characters
// e.g., "my%5Cfile.txt" instead of "my\file.txt"
```

Steps to reproduce:
1. Use `this.emitFile()` to emit a file asset
2. Reference it via `import.meta.ROLLUP_FILE_URL_<referenceId>` 
3. Build with format: 'es'
4. The resulting URL has double-escaped special characters

### Expected behavior

The generated URL should have properly escaped characters only once, matching the behavior of other output formats like 'cjs' and 'system'. File paths with special characters should be correctly resolved without double-escaping.

### System Info
- Rollup version: latest
- Output format: es

---
Repository: /testbed
