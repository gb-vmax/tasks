# Bug Report

### Describe the bug

I'm encountering an issue with `for...in` loops where the generated output has incorrect syntax. The loop variable and the iterable expression appear to be in the wrong order, resulting in invalid JavaScript code.

### Reproduction

```js
const obj = { a: 1, b: 2, c: 3 };

for (const key in obj) {
  console.log(key);
}
```

After bundling, the output becomes malformed with the variable and object positions swapped, which breaks the code.

### Expected behavior

The `for...in` statement should maintain the correct syntax in the output:
```js
for (const key in obj) {
  console.log(key);
}
```

Instead, it seems like the left side (loop variable) and right side (iterable) are being rendered in the wrong order.

### Additional context

This appears to have started recently. The generated code is syntactically invalid and causes runtime errors when executed.

---
Repository: /testbed
