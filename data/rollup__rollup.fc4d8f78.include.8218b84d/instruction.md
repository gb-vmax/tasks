# Bug Report

### Describe the bug

I'm encountering an issue where `throw` statements inside conditional blocks aren't being properly included in the bundled output. The code after the throw statement gets incorrectly removed even when the throw is conditional.

### Reproduction

```js
function test(condition) {
  if (condition) {
    throw new Error('Something went wrong');
  }
  console.log('This should be included');
  return 42;
}
```

After bundling, the `console.log` and `return` statements are missing from the output, even though they're reachable when `condition` is false.

### Expected behavior

Code that is reachable (when the throw statement is inside a conditional branch) should be included in the bundle. Only code that comes after an unconditional throw statement should be treated as unreachable.

### Additional context

This seems to affect any code following a conditional throw statement. The bundler appears to be treating all code after the throw as dead code regardless of whether the throw is always executed or not.

---
Repository: /testbed
