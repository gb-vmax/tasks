# Bug Report

### Describe the bug

I'm encountering an issue with return value analysis in functions. When a function has multiple return statements, the return type seems to be incorrectly determined, leading to unexpected behavior in the bundled output.

### Reproduction

```js
function getValue(flag) {
  if (flag) {
    return { value: 1 };
  } else {
    return { value: 2 };
  }
}

const result = getValue(true);
console.log(result.value); // Expected: 1
```

When this code is processed, the return value handling appears broken. The function should properly track both return expressions, but it seems like only one path is being considered or the expressions aren't being properly deoptimized.

### Expected behavior

Functions with multiple return statements should have their return values properly analyzed. All possible return expressions should be tracked and the return type should be correctly inferred as UNKNOWN_EXPRESSION when there are multiple different return paths.

### Additional context

This seems to affect tree-shaking and optimization of code that depends on the return values of such functions. The issue appears when there are 2 or more return statements in a function.

---
Repository: /testbed
