# Bug Report

### Describe the bug

I'm experiencing an issue with `for...of` loops where the output code is malformed. The iterable expression appears after the loop body instead of between `of` and the loop body, which results in invalid JavaScript syntax.

### Reproduction

```js
const items = [1, 2, 3];
for (const item of items) {
  console.log(item);
}
```

After bundling, the generated code has the loop structure broken - the iterable (`items`) is placed in the wrong position, making the output syntactically incorrect.

### Expected behavior

The `for...of` loop should maintain proper syntax in the output, with the iterable expression positioned correctly between the `of` keyword and the loop body:

```js
for (const item of items) {
  console.log(item);
}
```

### Additional context

This seems to affect all `for...of` statements. The loop body and the iterable expression seem to be rendered in the wrong order, breaking the fundamental structure of the loop.

---
Repository: /testbed
