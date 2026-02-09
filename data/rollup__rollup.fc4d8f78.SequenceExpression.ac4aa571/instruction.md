# Bug Report

### Describe the bug

I'm encountering an issue with sequence expressions where the first expression in a sequence is not being properly evaluated for side effects. This causes tree-shaking to incorrectly remove code that should be preserved.

### Reproduction

```js
// Example code that demonstrates the issue
const result = (sideEffect(), getValue());

// Where sideEffect() has important side effects that should not be removed
function sideEffect() {
  console.log('This should always execute');
  globalState.modified = true;
}

function getValue() {
  return 42;
}
```

When bundling this code, the `sideEffect()` call gets removed even though it has side effects that should be preserved. Only the last expression in the sequence is being checked.

### Expected behavior

All expressions in a sequence should be evaluated for side effects, not just the ones after the first. The bundler should preserve any expression that has side effects, regardless of its position in the sequence.

### Additional context

This seems to have started happening recently. The first expression in a comma sequence is being skipped during side effect analysis, which leads to incorrect code elimination during tree-shaking.

---
Repository: /testbed
