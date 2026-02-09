# Bug Report

### Describe the bug

I'm experiencing an issue with throw statements in my code. When a throw statement is used, the code that's being thrown appears to be getting included in the output even after the control flow has been marked as broken. This seems to affect tree-shaking behavior.

### Reproduction

```js
function example() {
  throw new Error('test');
  // dead code below should be tree-shaken
}
```

The argument expression in the throw statement is being processed after the control flow is marked as broken, which might be causing issues with how dead code is detected and removed.

### Expected behavior

The throw statement should properly mark the control flow as broken before including its argument expression, so that any subsequent dead code analysis works correctly.

### Additional context

This appears to be related to how the AST processes throw statements and when it marks the control flow as broken. The order of operations seems incorrect - the argument is being included before the broken flow flag is set.

---
Repository: /testbed
