# Bug Report

### Describe the bug

When tree-shaking async functions, the bundler is not correctly detecting side effects for promise rejection handlers. This causes code with `.catch()` handlers to be incorrectly removed during tree-shaking optimization, even when those handlers have side effects that should be preserved.

### Reproduction

```js
async function fetchData() {
  return fetch('/api/data')
    .catch(error => {
      console.error('Error fetching data:', error);
      trackError(error); // This side effect should be preserved
    });
}

// After bundling with tree-shaking enabled, the catch handler 
// and its side effects are removed
```

### Expected behavior

The bundler should detect that the `.catch()` handler contains side effects (like logging and error tracking) and preserve the async function in the output bundle. Currently, it only checks `.then()` for property read side effects but misses `.catch()`.

### System Info
- Rollup version: latest
- Tree-shaking: enabled with `propertyReadSideEffects` option

---
Repository: /testbed
