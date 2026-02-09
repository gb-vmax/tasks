# Bug Report

### Describe the bug

When using stdin input without a file extension, the plugin doesn't load the content properly. The stdin data is not being read when using the bare `'-'` identifier.

### Reproduction

```js
// rollup.config.js
export default {
  input: '-',
  output: {
    file: 'bundle.js',
    format: 'es'
  }
}
```

Then pipe content to rollup:
```bash
echo "export default 42" | rollup -c
```

### Expected behavior

The stdin content should be loaded and bundled when using `'-'` as the input without any extension. Currently it seems like only `'-.js'` or similar patterns with extensions work, but the plain `'-'` identifier is not being resolved/loaded correctly.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
