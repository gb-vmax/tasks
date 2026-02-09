# Bug Report

### Describe the bug

I'm experiencing an issue with empty imports not being properly trimmed from the dependency list. It seems like dependencies that have either imports OR reexports are being incorrectly removed, when they should only be removed if they have BOTH empty imports AND empty reexports.

### Reproduction

```js
// Bundle configuration with dependencies that have either imports or reexports
const dependencies = [
  { imports: null, reexports: ['someExport'] },  // Has reexports only
  { imports: ['someImport'], reexports: null },  // Has imports only
  { imports: null, reexports: null }             // Empty dependency
];

// After trimming, dependencies with imports or reexports are incorrectly removed
```

### Expected behavior

Dependencies should only be trimmed if they have BOTH empty imports AND empty reexports. If a dependency has either imports or reexports (but not both), it should be kept in the final output.

Currently it appears that dependencies with only imports OR only reexports are being removed from the bundle, which causes missing imports/reexports in the final output.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
