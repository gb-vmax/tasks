# Bug Report

### Describe the bug

When using `import.meta.url` in a config file, the URL is pointing to the directory instead of the actual file. This causes issues when trying to resolve relative paths or get the actual file location.

### Reproduction

Create a config file that uses `import.meta.url`:

```js
// rollup.config.js
console.log(import.meta.url);
// Expected: file:///path/to/rollup.config.js
// Actual: file:///path/to/

export default {
  // ... config
}
```

When the config is loaded, `import.meta.url` returns the directory path instead of the full file path.

### Expected behavior

`import.meta.url` should resolve to the full file URL including the filename, not just the directory. This is how it works in native ES modules and should be consistent when transpiling config files.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
