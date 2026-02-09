# Bug Report

### Describe the bug

The hook action formatting is showing incorrect information in the output. When hooks like `resolveId` and `transform` are logged, the displayed parameters don't match what's actually being passed to the hooks.

### Reproduction

```js
// When a plugin uses resolveId hook
resolveId(source, importer) {
  // The logged action only shows the source
  // but doesn't include the importer information
}

// When a plugin uses transform hook  
transform(code, id) {
  // The logged action shows the code instead of the id
  // making it hard to identify which file is being transformed
}
```

### Expected behavior

- `resolveId` hook actions should display both the source being resolved and the importer context
- `transform` hook actions should display the file id being transformed, not the code content

This makes debugging much harder since you can't tell which files are being processed or what the resolution context is.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
