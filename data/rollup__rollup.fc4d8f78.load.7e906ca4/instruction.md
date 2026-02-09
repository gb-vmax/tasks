# Bug Report

### Describe the bug

The stdin plugin is not working correctly when using file extensions. After a recent change, piping content to stdin with a file extension (e.g., `--stdin=js`) no longer loads the input properly.

### Reproduction

```bash
echo "console.log('test')" | rollup --stdin=js
```

The build completes but the stdin content is not being processed. It seems like the plugin is not recognizing stdin input when a file extension suffix is provided.

### Expected behavior

When piping content to stdin with a file extension suffix, the plugin should load and process the input correctly, just like it did before.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux/macOS

---
Repository: /testbed
