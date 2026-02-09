# Bug Report

### Describe the bug

I'm experiencing an issue with inline sourcemaps generation. When `sourcemap: 'inline'` is configured, the generated sourcemap comment appears to be malformed or incorrect. The inline sourcemap doesn't seem to be properly encoded as a data URI.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'es',
    sourcemap: 'inline'
  }
}
```

After building, the generated bundle contains an invalid sourcemap comment. The inline sourcemap should be a base64-encoded data URI but it appears to be using the wrong format.

### Expected behavior

When `sourcemap: 'inline'` is set, the output file should contain a properly formatted inline sourcemap comment like:
```
//# sourceMappingURL=data:application/json;charset=utf-8;base64,...
```

Instead, the sourcemap comment seems to be using an incorrect method for generating the inline data URI.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
