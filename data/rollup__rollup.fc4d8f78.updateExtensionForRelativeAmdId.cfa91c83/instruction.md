# Bug Report

### Describe the bug

I'm experiencing an issue with AMD module IDs where the `.js` extension handling seems to be inverted. When `forceJsExtensionForImports` is enabled, relative imports are getting their extensions removed instead of added, and vice versa.

### Reproduction

```js
// With forceJsExtensionForImports: true
// Relative import like './module'
// Expected: './module.js'
// Actual: './module' (extension not added)

// With forceJsExtensionForImports: false  
// Relative import like './module.js'
// Expected: './module'
// Actual: './module.js' (extension not removed)
```

Additionally, non-relative imports (those not starting with `.`) seem to be affected when they shouldn't be - they're having extension logic applied to them when they should be left unchanged.

### Expected behavior

- When `forceJsExtensionForImports` is `true`, relative AMD imports should have `.js` extensions added
- When `forceJsExtensionForImports` is `false`, relative AMD imports should have `.js` extensions removed  
- Non-relative imports should pass through unchanged regardless of the setting

### System Info
- Rollup version: latest
- Format: AMD

---
Repository: /testbed
