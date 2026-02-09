# Bug Report

### Issue with circular reexports causing infinite recursion

I've encountered a problem with circular `export *` statements that's causing unexpected behavior in my build. When modules have circular reexports (e.g., module A exports * from B, and module B exports * from A), the reexport resolution doesn't work correctly.

### Reproduction

```js
// moduleA.js
export * from './moduleB.js';
export const a = 1;

// moduleB.js
export * from './moduleA.js';
export const b = 2;
```

When trying to build a project with this setup, the reexports aren't being tracked properly. It seems like the circular reference detection might not be working as intended.

### Expected behavior

The bundler should handle circular `export *` statements gracefully and correctly resolve which exports come from which module, avoiding infinite recursion.

### Additional context

This used to work in previous versions, so it might be a recent regression. The issue appears to be related to how transitiveReexports are being cached and returned.

---
Repository: /testbed
