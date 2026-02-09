# Bug Report

### Describe the bug

I'm experiencing an issue where `for...in` loops are being incorrectly tree-shaken/removed from the output bundle even when they have side effects. The loop should be preserved in the final bundle, but it's getting eliminated during the build process.

### Reproduction

```js
const obj = { a: 1, b: 2, c: 3 };

for (const key in obj) {
  console.log(key); // This should execute but gets removed
}
```

When bundling the above code, the `for...in` loop is completely removed from the output even though it has a clear side effect (the console.log statement).

### Expected behavior

The `for...in` loop should be preserved in the bundled output when it contains side effects or when the right-hand side expression has side effects. The tree-shaking should not remove loops that perform observable actions.

### Additional context

This seems to happen specifically with `for...in` statements. Regular `for` loops and `for...of` loops appear to work correctly. The issue might be related to how side effects are being detected in the loop structure.

---
Repository: /testbed
