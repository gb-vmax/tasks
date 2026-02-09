# Bug Report

### Describe the bug

I'm experiencing a crash when using certain array mutation methods in my code. The bundler throws an error about accessing properties on undefined when it tries to optimize the code.

### Reproduction

```js
const arr = [1, 2, 3];
arr.shift(); // This causes the bundler to crash
```

The error occurs during the build process when Rollup tries to analyze side effects of array methods that mutate their arguments.

### Expected behavior

The code should bundle successfully without errors. Array mutation methods like `shift()`, `pop()`, etc. should be handled correctly during the optimization phase.

### Additional context

This seems to happen specifically with array methods that don't take arguments but still mutate the array. Methods like `push()` and `splice()` that take arguments work fine, but `shift()` and `pop()` trigger the crash.

The error message suggests something about trying to access a property on an undefined value during the deoptimization phase.

---
Repository: /testbed
