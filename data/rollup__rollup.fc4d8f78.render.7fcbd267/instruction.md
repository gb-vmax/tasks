# Bug Report

### Describe the bug

When using `for...of` loops with certain variable names, the generated code has incorrect spacing between the `of` keyword and the iterable expression. This results in malformed output that causes syntax errors.

### Reproduction

```js
// Input code
for (const item of items) {
  console.log(item);
}

// Expected output
for (const item of items) {
  console.log(item);
}

// Actual output (missing space after 'of')
for (const item ofitems) {
  console.log(item);
}
```

This appears to happen specifically when the iterable expression starts immediately after the `of` keyword without extra whitespace in the original source.

### Expected behavior

The bundler should preserve or add the necessary space between the `of` keyword and the iterable expression in `for...of` loops, ensuring valid JavaScript syntax in the output.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
