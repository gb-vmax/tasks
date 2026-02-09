# Bug Report

### Describe the bug

When using modules with `moduleSideEffects: 'no-treeshake'`, the tree-shaking behavior seems inconsistent. The `hasTreeShakingPassStarted` flag is not being set correctly for modules that go through the regular `include()` path instead of `includeAllInBundle()`.

### Reproduction

```js
// Module with regular tree-shaking
const regularModule = {
  isExecuted: true,
  info: {
    moduleSideEffects: true
  }
}

// Module with no-treeshake
const noTreeshakeModule = {
  isExecuted: true,
  info: {
    moduleSideEffects: 'no-treeshake'
  }
}
```

When the tree-shaking pass runs:
1. Modules with `moduleSideEffects: 'no-treeshake'` correctly set `hasTreeShakingPassStarted = true`
2. Regular modules that use `module.include()` don't have this flag set
3. This causes inconsistent behavior in subsequent passes

### Expected behavior

All executed modules should have `hasTreeShakingPassStarted` set to `true` during the tree-shaking pass, regardless of whether they use `includeAllInBundle()` or `include()`.

### Additional context

This affects the tree-shaking logic and may cause modules to be processed incorrectly in multi-pass scenarios. The flag should be set before either inclusion method is called to ensure consistent state.

---
Repository: /testbed
