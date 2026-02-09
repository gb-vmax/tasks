# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where variable declarations are being incorrectly removed from the bundle even when they have side effects or are being used later in the code.

### Reproduction

```js
// input.js
const sideEffectVar = performSideEffect();
const unused = 'test';

export function myFunction() {
  return sideEffectVar;
}
```

When bundling this code, the `sideEffectVar` declaration gets tree-shaken out even though it's clearly being referenced in the exported function. This breaks the output bundle.

### Expected behavior

Variable declarations that are referenced or have side effects should be preserved in the bundle. The bundler should recognize that `sideEffectVar` is needed and include it in the output.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
