# Bug Report

### Describe the bug

I'm experiencing an issue with external module path resolution. When using external modules with custom path configurations, the import paths in the generated output are not being normalized correctly.

### Reproduction

```js
// rollup.config.js
export default {
  external: ['some-external-lib'],
  output: {
    format: 'es',
    paths: {
      'some-external-lib': './custom/path/to/lib'
    }
  }
}
```

When bundling, the generated import statements for external modules are using the wrong path format. It seems like the path normalization logic is inverted - paths that should be normalized are being left as-is, and paths that shouldn't be normalized are being processed.

### Expected behavior

External module imports should respect the `renormalizeRenderPath` setting and apply path normalization only when appropriate. The `paths` option should work correctly to remap external module paths in the output.

### System Info
- Rollup version: latest
- Node version: 18.x

This is affecting my build output and causing import resolution failures in the browser. Any help would be appreciated!

---
Repository: /testbed
