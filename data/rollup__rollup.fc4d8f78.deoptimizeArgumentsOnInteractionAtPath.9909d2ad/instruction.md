# Bug Report

### Describe the bug

I'm experiencing an issue where global variable properties are not being tracked correctly during tree-shaking. It seems like the bundler is incorrectly removing code that accesses nested properties on global objects, resulting in runtime errors or unexpected behavior.

### Reproduction

```js
// input.js
const result = globalThis.someGlobal.nestedProperty.method();
console.log(result);
```

When bundling this code, the access to `globalThis.someGlobal.nestedProperty.method()` is being treated as side-effect-free and the code gets optimized away incorrectly, even though it should be preserved.

This also happens with other global objects like `window` or `global`:

```js
window.myLib.config.setValue('test');
```

The above code gets removed during the build even though it has clear side effects.

### Expected behavior

Accesses to properties on global variables should be properly tracked and preserved when they have side effects. The bundler should not remove code that interacts with nested properties of global objects.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
