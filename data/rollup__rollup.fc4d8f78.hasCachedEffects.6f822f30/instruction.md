# Bug Report

### Describe the bug

I'm experiencing some weird behavior with function effect caching in my rollup build. It seems like the bundler is not correctly determining whether effects have been cached for certain functions, leading to incorrect optimization decisions.

### Reproduction

```js
// Example code that triggers the issue
export function myFunction() {
  const sideEffect = performSideEffect();
  return sideEffect;
}

// When this gets processed, the effect caching logic
// doesn't work as expected
```

The bundler seems to be making incorrect assumptions about whether a function's effects have been analyzed/cached, which causes it to either:
- Re-analyze effects when it shouldn't (performance issue)
- Skip analysis when it should run (correctness issue)

### Expected behavior

The `hasCachedEffects` property should accurately reflect whether effects for a function have already been computed and cached. This should prevent redundant analysis while ensuring correctness.

### System Info
- Rollup version: latest
- Node version: 18.x

This might be related to how the internal flags are being checked. The logic for determining cached effects seems off.

---
Repository: /testbed
