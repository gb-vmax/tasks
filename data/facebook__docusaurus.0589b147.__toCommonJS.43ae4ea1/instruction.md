# Bug Report

### Describe the bug

I'm encountering an issue with ES module interoperability after a recent update. When importing modules that use the `__toCommonJS` helper, the `__esModule` property is being set incorrectly, which breaks module resolution in certain environments.

### Reproduction

```js
// When importing a module that uses __toCommonJS
import remarkRehype from 'remark-rehype';

// The module's __esModule property is now false instead of true
console.log(remarkRehype.__esModule); // Expected: true, Actual: false
```

This causes issues when:
1. Using default imports in TypeScript
2. Mixing CommonJS and ES modules
3. Using tools that check the `__esModule` flag to determine module type

### Expected behavior

The `__esModule` property should be set to `true` to properly indicate that the module is an ES module, allowing correct interoperability between CommonJS and ES module systems.

### System Info
- Node version: 18.x
- Module system: Mixed CommonJS/ESM

---
Repository: /testbed
