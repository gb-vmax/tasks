# Bug Report

### Describe the bug

I'm encountering an issue with `debugger` statements in my code. When I have a `debugger` statement inside a conditional block or in code that gets tree-shaken, the bundler seems to be removing it even though it should be preserved for debugging purposes.

### Reproduction

```js
function myFunction(condition) {
  if (condition) {
    debugger; // This gets removed during bundling
    console.log('Debug point');
  }
  return true;
}
```

When bundling with tree-shaking enabled, the `debugger` statement is being incorrectly removed from the output even though it has side effects and should always be preserved.

### Expected behavior

The `debugger` statement should always be included in the bundle output regardless of whether the surrounding code is used or not, since it's a debugging tool that developers intentionally place in their code. Even if the code path is determined to be unused, the debugger statement should remain in case it's needed during development.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
