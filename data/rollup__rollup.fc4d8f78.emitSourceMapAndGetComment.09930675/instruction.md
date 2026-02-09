# Bug Report

### Describe the bug

When generating bundles with sourcemaps enabled, the sourcemap comment is not being added to the output files. The generated code is missing the `//# sourceMappingURL=` comment that should point to the sourcemap file.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'es',
    sourcemap: true  // or 'inline', 'external'
  }
}
```

After building, the output file `dist/bundle.js` doesn't contain the sourcemap comment at the end, even though the `.map` file is generated correctly.

### Expected behavior

The generated bundle should include the sourcemap comment like:
```js
//# sourceMappingURL=bundle.js.map
```

This worked correctly in previous versions. The sourcemap files are being created, but the reference comment in the bundle is missing, which breaks debugging in browser DevTools.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
