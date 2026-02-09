# Bug Report

### Describe the bug

When using external modules with `renormalizeRenderPath` enabled, the path normalization logic appears to be inverted. Instead of normalizing the path when `renormalizeRenderPath` is true, it's normalizing when it's false, resulting in incorrect file paths for external chunks.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/main.js',
  external: ['some-external-lib'],
  output: {
    file: 'dist/bundle.js',
    format: 'es',
    paths: {
      'some-external-lib': './custom/path/lib.js'
    }
  },
  // ... other config with renormalizeRenderPath enabled
}
```

When bundling, the external module path gets incorrectly normalized/not normalized depending on the `renormalizeRenderPath` setting.

### Expected behavior

When `renormalizeRenderPath` is enabled, the path should be normalized relative to the input base. When disabled, it should use the module ID as-is. The current behavior seems backwards - paths are being normalized when they shouldn't be and vice versa.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
