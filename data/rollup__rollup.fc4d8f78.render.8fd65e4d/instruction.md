# Bug Report

### Describe the bug

I'm encountering an issue with `yield` expressions where the spacing between `yield` and its argument is being handled incorrectly. When there's already whitespace between `yield` and the argument, an extra space is being added, resulting in double spaces in the output.

### Reproduction

```js
function* generator() {
  yield value;
}
```

After bundling/processing, the output becomes:

```js
function* generator() {
  yield  value; // notice the double space
}
```

### Expected behavior

The spacing should be preserved as-is when there's already whitespace between `yield` and its argument. Only when `yield` is directly followed by the argument (like `yieldvalue`) should a space be added.

Expected output:
```js
function* generator() {
  yield value; // single space maintained
}
```

### Additional context

This seems to affect all yield expressions where there's existing whitespace. The logic appears to be inverted - it's adding spaces when they already exist rather than when they're missing.

---
Repository: /testbed
