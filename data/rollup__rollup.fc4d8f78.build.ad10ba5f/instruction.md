# Bug Report

### Describe the bug

When building with multiple output configurations, only the first output is being generated. If I specify multiple output formats (e.g., both ESM and CJS), the build process completes successfully but only creates files for the first output option.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: [
    {
      file: 'dist/bundle.esm.js',
      format: 'esm'
    },
    {
      file: 'dist/bundle.cjs.js',
      format: 'cjs'
    }
  ]
}
```

After running the build:
- `dist/bundle.esm.js` is created ✓
- `dist/bundle.cjs.js` is NOT created ✗

### Expected behavior

All configured output files should be generated when multiple output options are specified. Both ESM and CJS bundles should be written to disk.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
