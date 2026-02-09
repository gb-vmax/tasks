# Bug Report

### Describe the bug

I'm experiencing an issue where object property side effects aren't being properly detected during tree-shaking. When I have an object with properties that have side effects in their values, those side effects are being incorrectly eliminated from the bundle.

### Reproduction

```js
const obj = {
  key: computedKey(),
  value: sideEffectFunction()
}
```

In this case, `sideEffectFunction()` should be preserved in the output bundle since it has side effects, but it's being removed during the tree-shaking process.

### Expected behavior

Both the key computation and the value expression should be evaluated for side effects. If either has side effects, the entire property should be preserved in the bundle.

### Additional context

This seems to affect any object property where the value expression contains side effects. The bundler is not correctly analyzing the value part of the property and is incorrectly marking it as pure/removable.

---
Repository: /testbed
