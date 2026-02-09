# Bug Report

### Describe the bug

When loading a config file, relative imports starting with `./` are being incorrectly treated as external dependencies instead of being resolved locally. This causes the config loading to fail or behave unexpectedly.

### Reproduction

Create a rollup config file that imports a local module:

```js
// rollup.config.js
import myPlugin from './my-plugin.js';

export default {
  plugins: [myPlugin()]
}
```

When trying to load this config, the `./my-plugin.js` import is not resolved correctly and is treated as an external dependency.

### Expected behavior

Local relative imports (starting with `./` or `../`) should be resolved and bundled with the config file, not marked as external. The config file should load successfully with all local dependencies included.

### Additional context

This seems to affect any relative import in config files. Absolute paths and non-relative imports work fine, but relative paths with `./` prefix don't get resolved properly.

---
Repository: /testbed
