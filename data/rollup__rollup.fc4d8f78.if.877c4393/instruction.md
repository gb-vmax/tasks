# Bug Report

### Describe the bug

I'm encountering an issue with the `manualChunks` and `preserveModules` options. When I try to use `manualChunks` together with `preserveModules: false`, I'm getting an error saying that `manualChunks` is not supported with `preserveModules`, even though `preserveModules` is actually disabled.

### Reproduction

```js
export default {
  input: 'src/index.js',
  output: {
    dir: 'dist',
    format: 'es',
    preserveModules: false,
    manualChunks: {
      vendor: ['lodash']
    }
  }
}
```

Running the build with this configuration throws an error:
```
Invalid option "output.manualChunks" - this option is not supported for "output.preserveModules"
```

### Expected behavior

The build should succeed without errors when `preserveModules` is set to `false`. The error should only appear when `preserveModules` is `true`, since that's when the two options are actually incompatible.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
