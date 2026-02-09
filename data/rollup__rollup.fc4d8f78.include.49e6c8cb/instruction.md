# Bug Report

### Describe the bug

I'm encountering an issue where update expressions (like `++` and `--`) are not being included in the output bundle correctly. It seems like code containing these operators is being incorrectly tree-shaken or not included when it should be.

### Reproduction

```js
let counter = 0;

function increment() {
  counter++;
  return counter;
}

// The increment function gets tree-shaken even though it has side effects
export { increment };
```

When bundling this code, the update expression and potentially the entire function may be incorrectly excluded from the output, even though it clearly has side effects that should be preserved.

### Expected behavior

Update expressions should always be included in the bundle since they modify variables and have side effects. The tree-shaking logic should recognize that `counter++`, `counter--`, `++counter`, and `--counter` all mutate state and must be preserved.

### Additional context

This appears to affect both prefix and postfix update operators. The issue manifests when the updated variable is used elsewhere in the code - the updates don't seem to be properly tracked as having side effects during the inclusion phase.

---
Repository: /testbed
