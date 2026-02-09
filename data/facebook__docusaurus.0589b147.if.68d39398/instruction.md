# Bug Report

### Describe the bug

When passing a string path to `babelOptions` in the webpack configuration, the babel configuration is not being loaded correctly. Instead of using the custom babel config file specified by the string path, it seems to be falling back to default behavior or using an incorrect configuration.

### Reproduction

```js
const webpackConfig = {
  // ... other config
  babelOptions: '/path/to/custom/babel.config.js'
}

// Expected: Should use the custom babel config from the specified path
// Actual: The custom babel config is ignored
```

### Steps to reproduce:
1. Create a custom babel configuration file
2. Pass the file path as a string to `babelOptions`
3. Build the project
4. Notice that the custom babel transformations are not being applied

### Expected behavior

When `babelOptions` is provided as a string path to a babel config file, that config file should be loaded and used for babel transformations. The `babelrc` should be disabled and `configFile` should point to the specified path.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
