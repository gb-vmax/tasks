# Bug Report

### Describe the bug

I'm encountering an issue with `exportAllSources` where the exported bindings are being set incorrectly. When using `export * from 'module'` syntax, the binding value appears to be the source module name instead of the wildcard `'*'`.

### Reproduction

```js
// module.js
export * from './other-module';

// When inspecting exportedBindings
const bindings = module.exportedBindings;
// Expected: { './other-module': ['*'] }
// Actual: { './other-module': ['./other-module'] }
```

### Expected behavior

For `export *` statements, the `exportedBindings` object should map the source module to an array containing `'*'` to indicate all exports are re-exported, not the source name itself.

### Additional context

This seems to have broken after a recent change. The wildcard export tracking is not working as intended - instead of storing `'*'` to represent "all exports", it's storing the source module path.

---
Repository: /testbed
