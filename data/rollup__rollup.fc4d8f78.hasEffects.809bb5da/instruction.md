# Bug Report

### Describe the bug

I'm experiencing an issue where `for...of` loops are being completely removed from my bundle even when they have side effects. The loop body contains function calls and mutations that should be preserved, but the entire loop is getting tree-shaken out.

### Reproduction

```js
const items = [1, 2, 3];

for (const item of items) {
  console.log(item);
  doSomethingImportant(item);
}

// The entire for...of loop disappears from the output
```

This also happens with more complex scenarios:

```js
for (const entry of myArray) {
  globalState.count++;
  performSideEffect(entry);
}
```

### Expected behavior

The `for...of` loop should be included in the bundle when it contains code with side effects. The loop body clearly has side effects (console.log, function calls, state mutations) that need to be preserved.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
