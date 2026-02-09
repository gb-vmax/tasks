# Bug Report

### Describe the bug

I'm encountering an issue where `for...of` loops are being incorrectly tree-shaken from my bundle even when they have side effects. The loops are being removed during the build process, which breaks my application's functionality.

### Reproduction

```js
const items = [1, 2, 3];
let sum = 0;

for (const item of items) {
  sum += item;
  console.log(item);
}

console.log('Total:', sum);
```

When bundling this code, the `for...of` loop gets completely removed from the output, and only the final `console.log('Total:', sum)` remains (with `sum` being 0 instead of 6).

### Expected behavior

The `for...of` loop should be preserved in the bundle since it contains side effects (the `console.log` calls and the mutation of the `sum` variable). The loop should execute and produce the correct output.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The loop is being treated as if it has no effects when it clearly does.

---
Repository: /testbed
