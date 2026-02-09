# Bug Report

### Describe the bug

When using `new` expressions with constructor arguments, the first argument is being ignored during side effect analysis. This causes the bundler to incorrectly tree-shake code where the first constructor argument has important side effects.

### Reproduction

```js
class MyClass {
  constructor(a, b) {
    // constructor logic
  }
}

function sideEffect() {
  console.log('This should be preserved');
  return 'value';
}

// The sideEffect() call in the first argument position is not being detected
const instance = new MyClass(sideEffect(), 'second arg');
```

In this case, the `sideEffect()` function call should be detected as having side effects and preserved in the output, but it's being skipped during the analysis.

### Expected behavior

All constructor arguments should be checked for side effects, including the first one. The bundler should correctly identify and preserve side effects in any argument position.

### Additional context

This appears to affect any `new` expression where the first argument has side effects - function calls, property accesses with getters, etc. Arguments in positions 2 and beyond are correctly analyzed.

---
Repository: /testbed
