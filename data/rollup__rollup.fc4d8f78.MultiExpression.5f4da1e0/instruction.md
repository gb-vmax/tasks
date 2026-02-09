# Bug Report

### Issue with side effects detection in sequence expressions

I'm encountering an issue where side effects in sequence expressions (comma operator) are not being properly detected. It seems like only the first expression in a sequence is being checked for side effects, while subsequent expressions are being ignored.

### Reproduction

```js
// Example code that demonstrates the issue
const result = (
  sideEffect1(),
  sideEffect2(),
  sideEffect3()
);
```

In the above code, only `sideEffect1()` is being analyzed for side effects. The bundler is not detecting that `sideEffect2()` and `sideEffect3()` also have side effects, which leads to incorrect tree-shaking behavior.

### Expected behavior

All expressions in a sequence should be checked for side effects. If any expression in the sequence has side effects, the entire sequence should be considered as having side effects.

### Current behavior

Only the first expression in the sequence is being evaluated for side effects. This causes the bundler to incorrectly optimize away code that should be preserved due to side effects in later expressions.

This seems like it might be a regression - I don't recall seeing this behavior in earlier versions.

---
Repository: /testbed
