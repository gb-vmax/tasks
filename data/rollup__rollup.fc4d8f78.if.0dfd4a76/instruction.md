# Bug Report

### Describe the bug

When using JSX with `mode: 'preserve'` and setting an `importSource`, the configuration validation is not working as expected. The bundler should require either a `factory` or `fragment` to be specified when using `importSource` with preserved JSX, but currently it's accepting invalid configurations without throwing an error.

### Reproduction

```js
{
  jsx: {
    mode: 'preserve',
    importSource: 'react',
    // Neither factory nor fragment specified - should error but doesn't
  }
}
```

This configuration should be rejected but is currently being accepted. The validation logic seems to be inverted.

### Expected behavior

When `mode: 'preserve'` is used with an `importSource`, the bundler should throw an error if neither `factory` nor `fragment` is provided. Currently, it only errors when BOTH are provided, which is backwards.

The error message states: "when preserving JSX and specifying an importSource, you also need to specify a factory or fragment" - but this error is not being triggered in the correct scenarios.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
