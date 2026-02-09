# Bug Report

### Describe the bug

When using `manualChunks` together with `inlineDynamicImports`, the validation logic appears to be inverted. The error is now thrown when `inlineDynamicImports` is set to `false` instead of `true`, which is the opposite of the expected behavior.

### Reproduction

```js
// This configuration should work fine but throws an error
export default {
  output: {
    inlineDynamicImports: false,
    manualChunks: {
      vendor: ['react', 'react-dom']
    }
  }
}

// Error: "output.inlineDynamicImports" is not supported for "output.inlineDynamicImports"
```

Meanwhile, this configuration (which should error) doesn't throw:

```js
// This should throw an error but doesn't
export default {
  output: {
    inlineDynamicImports: true,
    manualChunks: {
      vendor: ['react', 'react-dom']
    }
  }
}
```

### Expected behavior

The validation should throw an error when both `manualChunks` and `inlineDynamicImports: true` are used together, since these options are incompatible. When `inlineDynamicImports` is `false` or not set, `manualChunks` should work normally without any errors.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
