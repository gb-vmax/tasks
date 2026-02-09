# Bug Report

### Describe the bug

When using the watch mode with include/exclude filters, the file filtering behavior appears to be inverted. Files that should be watched are being ignored, and files that should be excluded are being watched instead.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'es'
  },
  watch: {
    include: 'src/**',
    exclude: 'node_modules/**'
  }
}
```

Steps to reproduce:
1. Set up a rollup config with watch mode
2. Configure include patterns to watch only `src/**`
3. Configure exclude patterns to ignore `node_modules/**`
4. Start watch mode
5. Make changes to files in `src/` - they are not detected
6. Make changes to files in `node_modules/` - they trigger rebuilds

### Expected behavior

Files matching the `include` pattern should be watched and trigger rebuilds. Files matching the `exclude` pattern should be ignored and not trigger rebuilds.

Currently experiencing the opposite behavior where included files are ignored and excluded files are watched.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
