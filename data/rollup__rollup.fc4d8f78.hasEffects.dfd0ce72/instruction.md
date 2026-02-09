# Bug Report

### Describe the bug

I'm experiencing an issue with named exports where side effects are not being properly detected. When I have a named export statement without a declaration (like `export { foo } from './module'`), the bundler seems to be treating it incorrectly in terms of side effect analysis.

### Reproduction

```js
// module.js
export { something } from './other-module';
```

When bundling this code, the behavior around tree-shaking and side effect detection appears to be inverted from what I'd expect. Exports that should be kept are being removed, and vice versa.

### Expected behavior

Named export statements (especially re-exports) should be analyzed correctly for side effects. The bundler should properly determine whether these exports can be safely tree-shaken or if they need to be preserved.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
