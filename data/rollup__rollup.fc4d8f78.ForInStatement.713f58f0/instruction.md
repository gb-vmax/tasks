# Bug Report

### Describe the bug

I'm experiencing an issue where `for...in` loops are being incorrectly tree-shaken in my bundle. Code that should be included in the output is getting removed, causing runtime errors in production.

### Reproduction

```js
const obj = { a: 1, b: 2, c: 3 };

for (const key in obj) {
  console.log(key, obj[key]);
}
```

After bundling, the loop body gets removed even though it has side effects (the `console.log` call). The generated code is missing the expected output statements.

### Expected behavior

The `for...in` loop and its body should be preserved in the bundle since it contains side effects. The console.log statements should appear in the final output.

### Additional context

This seems to have started happening recently. My production build is now broken because essential `for...in` loops are being stripped out. The loops work fine in development but disappear after bundling with tree-shaking enabled.

---
Repository: /testbed
