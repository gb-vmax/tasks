# Bug Report

### Describe the bug

I'm experiencing an issue with external module re-exports. When using `export * from 'external-module'`, the generated output appears to be incorrect. The external module identifier seems to be malformed in the re-export tracking.

### Reproduction

```js
// lib.js
export * from 'external-package';

// When bundling, the re-export identifier for the external module
// is generated incorrectly
```

The issue manifests when:
1. You have a module that re-exports everything from an external module
2. The bundler processes the re-exports
3. The external module identifier gets tracked with incorrect formatting

### Expected behavior

External module re-exports should be tracked with the correct identifier format. The module ID should maintain its proper structure when being added to the re-exports set.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to affect how external modules are referenced in the re-export tracking system. The identifier format appears to be reversed or malformed compared to what it should be.

---
Repository: /testbed
