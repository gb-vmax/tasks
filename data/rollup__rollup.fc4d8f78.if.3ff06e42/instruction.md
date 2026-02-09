# Bug Report

### Describe the bug

I'm getting an error when trying to use `manualChunks` with `inlineDynamicImports: false` in my rollup config. The error message says that `output.dynamicImportInCss` is not supported with `inlineDynamicImports`, which doesn't make sense since I'm not even using `dynamicImportInCss` and `inlineDynamicImports` is set to `false`.

### Reproduction

```js
export default {
  input: 'src/index.js',
  output: {
    dir: 'dist',
    format: 'esm',
    inlineDynamicImports: false,
    manualChunks: {
      vendor: ['react', 'react-dom']
    }
  }
}
```

When I run the build with this configuration, I get an error about `output.dynamicImportInCss` not being supported with `inlineDynamicImports`, even though:
1. I'm not using `dynamicImportInCss` anywhere
2. My `inlineDynamicImports` is set to `false`, not `true`

### Expected behavior

The build should work fine when `inlineDynamicImports` is `false` and `manualChunks` is configured. According to the docs, `manualChunks` should only conflict with `inlineDynamicImports: true`.

The error message is also confusing - it mentions `dynamicImportInCss` when the actual issue is with `manualChunks`.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
