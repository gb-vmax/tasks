# Bug Report

### Describe the bug

I'm encountering an issue with `for...of` loop syntax when bundling code. The output is malformed when there's no space between the `of` keyword and the iterable expression.

### Reproduction

```js
// Input code
for (const item of[1, 2, 3]) {
  console.log(item);
}
```

After bundling, the output becomes invalid:

```js
for (const item o f[1, 2, 3]) {
  console.log(item);
}
```

The space is being inserted in the wrong position, breaking the `of` keyword instead of adding a space between `of` and the array literal.

### Expected behavior

The bundler should correctly handle `for...of` loops even when there's no space between `of` and the iterable. The output should be valid JavaScript:

```js
for (const item of [1, 2, 3]) {
  console.log(item);
}
```

### Additional context

This seems to affect cases where the iterable expression starts immediately after the `of` keyword without whitespace. The issue appears to be with how the bundler detects and fixes the spacing around the `of` keyword.

---
Repository: /testbed
