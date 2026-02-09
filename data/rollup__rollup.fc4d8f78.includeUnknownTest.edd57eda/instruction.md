# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking behavior when using if-statements with certain control flow patterns. It appears that code after an if-statement is being incorrectly removed from the bundle even though it should be reachable.

### Reproduction

```js
function example(condition) {
  if (condition) {
    return;
  }
  
  console.log('This should be in the bundle');
}

example(true);
```

When bundling this code, the `console.log` statement is being removed from the output even though it's reachable when `condition` is false. The bundler seems to be treating the code after the if-statement as unreachable in cases where it should be preserved.

### Expected behavior

The code following an if-statement should be included in the bundle when it's potentially reachable. In the example above, since we can't statically determine the value of `condition`, the `console.log` should be preserved in the output.

### Additional context

This seems to be related to how the bundler tracks control flow through if-statements. The issue appears when:
1. The if-statement has a consequent that might break control flow (like a return statement)
2. There's an alternate branch or code following the if-statement
3. The test condition cannot be statically evaluated

The bundler appears to be too aggressive in determining what code is unreachable.

---
Repository: /testbed
