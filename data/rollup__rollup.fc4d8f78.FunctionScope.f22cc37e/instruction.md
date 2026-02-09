# Bug Report

### Describe the bug

I'm experiencing an issue where function arguments are not being included correctly in the bundle. When a function is called with multiple arguments, it seems like the first argument is being skipped during the inclusion process, and arguments are only being processed when the `arguments` variable is already included (which appears to be the opposite of what should happen).

### Reproduction

```js
function myFunction(a, b, c) {
  // Function body
}

// When called with multiple arguments
myFunction(arg1, arg2, arg3);
```

In this scenario, the first argument (`arg1`) doesn't get properly included in the bundle, while `arg2` and `arg3` are processed. Additionally, the logic seems inverted - arguments are only being included when the `arguments` variable is already marked as included, rather than when it's not included.

### Expected behavior

All function call arguments should be included in the bundle starting from index 0 (the first argument), and the inclusion should happen when the `arguments` variable is NOT already included.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing issues with tree-shaking and proper dependency tracking in my build output. Some required code is being incorrectly removed from the final bundle.

---
Repository: /testbed
