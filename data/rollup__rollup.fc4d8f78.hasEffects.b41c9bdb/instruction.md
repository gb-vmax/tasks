# Bug Report

### Describe the bug

I'm experiencing an issue with `continue` statements in labeled loops. When using a `continue` with a label, the code is being incorrectly tree-shaken even though it should be preserved.

### Reproduction

```js
outer: for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (j === 1) {
      continue outer;
    }
    console.log(i, j);
  }
}
```

In this case, the `continue outer` statement should break the flow and continue to the next iteration of the outer loop, but it seems like the bundler is not correctly handling the labeled continue statement. The output is different than expected.

### Expected behavior

The labeled `continue` statement should properly affect tree-shaking and control flow analysis. Code after the `continue` in the inner loop should be recognized as unreachable, and the statement itself should be preserved in the output.

### Additional context

This seems to be related to how labeled statements interact with the control flow analysis. Regular unlabeled `continue` statements appear to work fine, but adding a label causes the issue.

---
Repository: /testbed
