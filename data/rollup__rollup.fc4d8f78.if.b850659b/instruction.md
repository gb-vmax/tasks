# Bug Report

### Describe the bug

When trying to load ES module config files, Rollup is not properly detecting when a config file cannot be loaded as an ES module. The warning detection logic appears to be broken, causing the CLI to fail to handle ES module loading errors correctly.

### Reproduction

1. Create a config file that triggers an ES module loading warning
2. Try to load it with Rollup CLI
3. The warning about "To load an ES module" is not being caught properly
4. The fallback behavior doesn't trigger as expected

```js
// rollup.config.js (as CommonJS in an ES module context)
module.exports = {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  }
}
```

When running this in a project with `"type": "module"` in package.json, the warning should be detected but it's not working correctly.

### Expected behavior

Rollup should properly detect warnings that contain "To load an ES module" and set the appropriate flag to handle the error gracefully, allowing it to try alternative loading strategies.

### System Info

- Rollup version: latest
- Node.js version: 18.x
- OS: Linux/macOS

---
Repository: /testbed
