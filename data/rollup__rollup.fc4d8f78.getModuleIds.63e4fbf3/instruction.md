# Bug Report

### Describe the bug

When using `manualChunks` function with the `getModuleIds()` API, the list of module IDs returned appears to be incomplete. It seems like one module ID is missing from the iteration, which causes issues when trying to analyze or organize all modules into manual chunks.

### Reproduction

```js
export default {
  input: 'src/index.js',
  output: {
    dir: 'dist',
    format: 'esm',
    manualChunks(id, { getModuleIds }) {
      const allIds = Array.from(getModuleIds());
      console.log('Total modules:', allIds.length);
      
      // Expected to see all module IDs, but one is missing
      // This affects chunk assignment logic that depends on 
      // having the complete list of modules
    }
  }
}
```

### Expected behavior

`getModuleIds()` should return an iterator containing ALL module IDs in the bundle graph. Every module that's part of the build should be included in the iteration.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
