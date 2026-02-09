# Bug Report

### Describe the bug

I'm encountering an issue with global variable detection where accessing properties on global objects is not being handled correctly. It seems like the deoptimization logic isn't properly checking the path when determining if a global exists.

### Reproduction

```js
// When accessing a property on a global object like this:
const value = Math.floor(5.5);

// Or accessing nested properties:
const result = console.log.apply(null, args);
```

The bundler appears to be incorrectly determining whether these globals exist, which affects tree-shaking and optimization behavior. Properties on known global objects should be recognized as safe to access without deoptimization.

### Expected behavior

When accessing properties on well-known global objects (like `Math.floor`, `console.log`, etc.), the bundler should correctly identify that these are valid global paths and handle them appropriately during optimization.

The current behavior seems to be checking an incorrect slice of the property path, which causes valid global property accesses to trigger unnecessary deoptimization.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
