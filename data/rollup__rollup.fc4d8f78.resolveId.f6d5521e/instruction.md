# Bug Report

### Issue with config file loading - relative imports not resolved correctly

I'm experiencing an issue where certain relative imports in my config file are not being resolved properly. It seems like the logic for determining whether an import is external or not has changed.

### Reproduction

Create a rollup config file with imports starting with `./`:

```js
// rollup.config.js
import plugin from './my-plugin.js';

export default {
  // ... config
}
```

When running the build, the import fails to resolve. The error suggests it's treating the relative import as external when it shouldn't be.

This also affects imports starting with `../` for parent directories.

### Expected behavior

Relative imports (those starting with `./` or `../`) should be resolved normally and not treated as external dependencies. Only actual external packages (like `'rollup'` or `'@rollup/plugin-node-resolve'`) should be marked as external.

### Additional context

This might be related to how the path resolution logic checks for relative vs absolute paths. It worked fine in previous versions but started failing recently.

---
Repository: /testbed
