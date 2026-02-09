# Bug Report

### Describe the bug

I'm encountering an issue with `continue` statements in loops where code after the `continue` is being incorrectly included in the bundle or not properly tree-shaken. It seems like the dead code elimination isn't recognizing that code following a `continue` statement is unreachable.

### Reproduction

```js
function test() {
  for (let i = 0; i < 10; i++) {
    if (i % 2 === 0) {
      continue;
      console.log('This should be removed'); // Unreachable code
    }
    console.log(i);
  }
}
```

When bundling this code, the unreachable `console.log` after the `continue` statement appears to be included in the output when it should be eliminated as dead code.

### Expected behavior

Code that appears after a `continue` statement (and before the end of the loop iteration block) should be recognized as unreachable and removed during tree-shaking/dead code elimination.

### Additional context

This might be related to how the control flow analysis handles `continue` statements, particularly when checking if subsequent code has effects or should be included in the bundle.

---
Repository: /testbed
