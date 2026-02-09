# Bug Report

### Describe the bug

I'm experiencing an issue where side effects in class property keys are not being properly detected. When a class property has a key with side effects (like a function call), those side effects are being ignored during the tree-shaking process, leading to incorrect code elimination.

### Reproduction

```js
let sideEffect = false;

function withSideEffect() {
  sideEffect = true;
  return 'key';
}

class MyClass {
  [withSideEffect()] = 'value';
}

// The side effect in the property key should be preserved
// but it's being removed during bundling
```

In this example, the `withSideEffect()` function should be called when the class is evaluated, but it appears to be getting tree-shaken away incorrectly.

### Expected behavior

Side effects in computed property keys should always be detected and preserved, even if the property itself is not used. The bundler should not remove code that has observable side effects.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
