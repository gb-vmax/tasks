# Bug Report

### Describe the bug

I'm experiencing an issue where the last argument in a `new` expression constructor call is not being properly evaluated for side effects. When I have a constructor call with multiple arguments where the final argument has side effects, those side effects are being ignored during the bundling process.

### Reproduction

```js
let sideEffect = false;

function setSideEffect() {
  sideEffect = true;
  return 'value';
}

// The side effect from the last argument is not detected
new MyClass(
  'arg1',
  'arg2',
  setSideEffect()  // This side effect is ignored
);
```

In the above code, the `setSideEffect()` function should be recognized as having side effects, but it appears to be skipped during analysis when it's the last argument.

This seems to happen specifically with constructor calls (`new` expressions) - regular function calls work fine. The issue only affects the last argument in the arguments list.

### Expected behavior

All arguments passed to a constructor should be evaluated for side effects, including the last one. The bundler should detect and preserve side effects in any argument position.

### Additional context

This is causing issues in production where important initialization code in the last constructor argument is being tree-shaken away incorrectly.

---
Repository: /testbed
