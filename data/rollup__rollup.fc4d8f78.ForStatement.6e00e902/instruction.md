# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking behavior in for-loops. It seems like code inside for-loop initializers is being incorrectly removed during the bundling process, even when the initialization expression has side effects.

### Reproduction

```js
let sideEffect = false;

for (let i = (sideEffect = true, 0); i < 5; i++) {
  console.log(i);
}

console.log(sideEffect); // Should be true
```

After bundling, the side effect in the for-loop initializer appears to be getting stripped out. The initialization expression contains a side effect that should be preserved, but it looks like the bundler is treating it as if it has no effects.

### Expected behavior

The bundler should detect and preserve side effects in for-loop initializers. Any expressions with side effects in the `init` part of a for-statement should not be removed during tree-shaking, regardless of whether the rest of the loop body is used.

### Additional context

This seems to be affecting any for-loop where the initialization contains function calls, assignments, or other operations that have side effects. The loop body executes correctly, but the side effects from the init expression are lost.

---
Repository: /testbed
