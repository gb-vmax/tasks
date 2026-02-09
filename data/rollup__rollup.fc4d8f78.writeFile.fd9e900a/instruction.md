# Bug Report

### Describe the bug

When loading a config file, I'm experiencing a race condition where the import statement tries to read the file before it's fully written to disk. This causes intermittent failures when the config file is being loaded.

### Reproduction

```js
// Create a rollup.config.js with some configuration
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  }
}

// Run rollup with this config
// Sometimes it works, sometimes it fails with "Cannot find module" or similar errors
```

The issue seems to happen randomly, especially on slower file systems or under heavy I/O load. The config file import occasionally fails because the file hasn't been completely written yet.

### Expected behavior

The config file should be reliably loaded every time, with the import waiting for the file write to complete before attempting to read it.

### System Info
- Rollup version: latest
- Node.js version: 18.x
- OS: Various (reproduced on Windows and Linux)

---
Repository: /testbed
