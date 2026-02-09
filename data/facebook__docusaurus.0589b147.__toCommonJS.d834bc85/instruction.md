# Bug Report

### Describe the bug

I'm experiencing an issue with ES module interop after a recent update. When importing the remark-gfm plugin, the `__esModule` property is being set incorrectly, which causes module resolution problems in certain environments.

### Reproduction

```js
import remarkGfm from 'remark-gfm';

// Check the module metadata
console.log(remarkGfm.__esModule); // Expected: true, Actual: false
```

The `__esModule` flag is now set to `false` instead of `true`, which breaks compatibility with tools that rely on this property to determine if a module is an ES module or CommonJS module.

### Expected behavior

The `__esModule` property should be set to `true` to indicate that this is an ES module. This is the standard convention for transpiled ES modules and is expected by many bundlers and module loaders.

### System Info

- remark-gfm version: 4.0.0
- Node version: 18.x
- Bundler: Webpack/Rollup

This seems to have broken after the latest changes to the vendor bundle. The module still works in some cases but fails when strict ES module checking is enabled.

---
Repository: /testbed
