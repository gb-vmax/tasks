# Bug Report

### Describe the bug

I'm experiencing an issue with labeled continue statements in loops. When a labeled continue is used, the code after the loop that should be unreachable is being incorrectly included in the bundle.

### Reproduction

```js
outer: for (let i = 0; i < 5; i++) {
  for (let j = 0; j < 5; j++) {
    if (j === 2) {
      continue outer;
    }
    console.log('inner', i, j);
  }
  console.log('This should not be in the bundle');
}
```

The line `console.log('This should not be in the bundle')` is being included in the output even though it's unreachable due to the labeled continue statement. This causes unnecessary code bloat in the final bundle.

### Expected behavior

Code that comes after a labeled continue statement (but before the loop end) should be recognized as unreachable and tree-shaken from the bundle, similar to how unlabeled continue statements work.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
