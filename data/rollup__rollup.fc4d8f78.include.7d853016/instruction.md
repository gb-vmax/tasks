# Bug Report

### Describe the bug

I'm experiencing an issue with `for...of` loops where the loop body is being included in the output even when it shouldn't be. It seems like the tree-shaking logic isn't working correctly for `for...of` statements - code that should be eliminated as dead code is still appearing in the final bundle.

### Reproduction

```js
// This for...of loop should be tree-shaken out since it has no side effects
// and its result is never used, but it's appearing in the output

for (const item of [1, 2, 3]) {
  const unused = item * 2;
}

// The loop body ends up in the bundle even though it's unreachable/unused
```

### Expected behavior

The `for...of` loop and its body should be removed during tree-shaking when the code has no observable side effects and the results are not used anywhere. The final bundle should not include this dead code.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. Previously, unused `for...of` loops were being correctly eliminated from the output.

---
Repository: /testbed
