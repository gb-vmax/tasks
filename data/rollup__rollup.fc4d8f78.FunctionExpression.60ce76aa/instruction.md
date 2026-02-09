# Bug Report

### Describe the bug

I'm experiencing an issue with function expressions where the scope resolution appears to be broken. When using named function expressions, I'm getting unexpected behavior with variable references inside the function body.

### Reproduction

```js
const fn = function myFunc() {
  // Variable references inside named function expressions
  // are not resolving correctly
  const x = 10;
  return x;
}
```

The scope chain seems to be incorrectly configured for function expressions. This is causing issues with:
1. Variable resolution within the function body
2. Access to the function's own name identifier
3. Closure variable references

### Expected behavior

Named function expressions should properly resolve variables in their scope chain, including references to their own identifier and parent scope variables.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like it might be related to how the scope hierarchy is being set up for function expressions. The issue doesn't occur with regular function declarations, only function expressions.

---
Repository: /testbed
