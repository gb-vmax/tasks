# Bug Report

### Describe the bug

I'm experiencing an issue with labeled `continue` statements in loops. When using a labeled continue inside nested loops, the code after the inner loop (but still inside the outer loop) is being incorrectly removed from the bundle, even though it should be executed.

### Reproduction

```js
outer: for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (j === 1) {
      continue outer;
    }
    console.log('inner', i, j);
  }
  console.log('after inner loop', i); // This gets removed but shouldn't
}
```

### Expected behavior

The code after the inner loop should be included in the bundle since the labeled `continue outer` only skips to the next iteration of the outer loop, not the code that comes after the inner loop within the same outer loop iteration.

In the example above, `console.log('after inner loop', i)` should be preserved in the output because it's reachable code - it will execute when `j === 0` before the continue statement is hit.

### System Info
- Rollup version: latest main branch
- Node version: 18.x

---
Repository: /testbed
