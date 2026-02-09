# Bug Report

### Describe the bug

When trying to load ES module config files, Rollup is incorrectly setting the `cannotLoadEsm` flag. The logic appears to be inverted - warnings about ES module loading are being ignored when they should trigger the flag, and unrelated warnings are setting the flag instead.

### Reproduction

```js
// rollup.config.mjs (ES module format)
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  }
}
```

When running Rollup with this config:
1. Create an ES module config file (`.mjs` extension)
2. Try to load it in an environment that emits ES module warnings
3. The config loader incorrectly handles the warning messages

### Expected behavior

The `cannotLoadEsm` flag should be set to `true` when warnings contain "To load an ES module" or "Failed to load the ES module". Currently it's doing the opposite - setting the flag when these messages are NOT present.

### System Info
- Rollup version: latest
- Node.js version: 18.x
- OS: Linux

This seems like a logic error in the warning handler that's causing ES module detection to fail.

---
Repository: /testbed
