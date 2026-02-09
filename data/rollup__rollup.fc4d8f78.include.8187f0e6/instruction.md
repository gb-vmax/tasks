# Bug Report

### Describe the bug

I'm experiencing an issue with `for...in` loops in my code. It seems like the loop body is being included in the bundle even when it shouldn't be. The bundler appears to be treating the loop as always included, regardless of whether it's actually used in the final output.

### Reproduction

```js
function unusedFunction() {
  const obj = { a: 1, b: 2, c: 3 };
  for (const key in obj) {
    console.log(key, obj[key]);
  }
}

// This function is never called, so the for-in loop should be tree-shaken
```

When bundling this code, the `for...in` loop body is included in the output even though `unusedFunction` is never called anywhere in the codebase.

### Expected behavior

The `for...in` statement and its body should be properly tree-shaken when the containing function is not used. The loop should only be included in the bundle when it's actually reachable in the code.

### Additional context

This might be related to how the inclusion logic handles loop statements. The issue doesn't seem to occur with regular `for` loops or `while` loops, only specifically with `for...in` statements.

---
Repository: /testbed
