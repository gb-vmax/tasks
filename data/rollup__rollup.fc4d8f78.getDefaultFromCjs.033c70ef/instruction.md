# Bug Report

### Describe the bug

I'm experiencing an issue where loading CommonJS config files causes the rollup CLI to hang indefinitely. The process doesn't exit or throw an error - it just freezes after attempting to load the configuration.

### Reproduction

1. Create a `rollup.config.js` file (CommonJS format):
```js
module.exports = {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'cjs'
  }
}
```

2. Run rollup with this config file
3. The CLI hangs and never completes

This seems to happen specifically with CommonJS configs. ESM configs work fine. It started happening recently and I'm not sure what changed.

### Expected behavior

The config file should load successfully and rollup should proceed with the build process.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
