# Bug Report

### Describe the bug

I'm experiencing an issue with chunk assignment when working with entry dependencies. It seems like the dependency tracking for static atoms is not working correctly - chunks that should be grouped together based on their shared dependencies are being split apart incorrectly.

### Reproduction

When building a project with multiple entry points that share common dependencies:

```js
// Entry point 1 depends on module A
// Entry point 2 depends on modules A and B
// Entry point 3 depends on module B

// Expected: Modules should be correctly assigned to chunks based on entry dependencies
// Actual: Dependency relationships appear to be incorrectly calculated
```

The chunk assignment logic doesn't seem to properly track which atoms (modules) are dependencies of which entries. This results in suboptimal chunking where shared dependencies aren't being identified correctly.

### Expected behavior

Entry points should have their static dependencies correctly tracked, and the bitmasking operations should properly set the dependency flags for each atom-entry relationship. Chunks should be assigned based on accurate dependency information.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The dependency graph calculation appears to be off, possibly related to how the atom masks are being applied to the entry dependency arrays.

---
Repository: /testbed
