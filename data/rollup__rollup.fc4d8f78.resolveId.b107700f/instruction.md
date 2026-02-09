# Bug Report

### Describe the bug

I'm experiencing an issue with config file loading where JSON imports are being treated incorrectly. When my rollup config file imports a JSON file, it's not being resolved as expected and the build fails.

### Reproduction

Create a rollup config file that imports a JSON file:

```js
// rollup.config.js
import pkg from './package.json';

export default {
  input: 'src/index.js',
  output: {
    file: pkg.main,
    format: 'cjs'
  }
};
```

When running rollup with this config, the JSON import is not being handled properly and causes the config loading to fail.

### Expected behavior

JSON files should be treated as external dependencies and resolved correctly during config file loading. The config should load successfully with the imported JSON data available.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
