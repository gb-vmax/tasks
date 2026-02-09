# Bug Report

### Describe the bug

I've encountered an issue where accessing properties on undefined objects in my code is not being properly handled during the bundling process. The bundler seems to be treating undefined member expressions differently than expected, which leads to incorrect optimization behavior.

### Reproduction

```js
const obj = undefined;

// Accessing properties on undefined should be handled correctly
const result = obj?.someProperty?.nestedProperty;

// But the bundler appears to be optimizing this incorrectly
function test() {
  return obj.property;
}
```

When bundling code that accesses properties on potentially undefined objects, the tree-shaking and optimization passes don't seem to recognize these cases properly anymore. This affects how the code is analyzed and optimized.

### Expected behavior

The bundler should correctly identify and handle member expressions on undefined values, ensuring proper deoptimization occurs when necessary. Code that accesses properties on undefined should be treated as potentially side-effectful and not be incorrectly optimized away or transformed.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
