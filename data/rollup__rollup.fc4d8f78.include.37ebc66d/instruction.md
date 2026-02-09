# Bug Report

### Describe the bug

I'm encountering an issue where functions are being included in the bundle even when they shouldn't be, and the control flow analysis seems broken. After bundling, I'm seeing unexpected code being retained that should have been tree-shaken away.

### Reproduction

```js
function test() {
  return;
  console.log('unreachable'); // This should be removed
}

// Function is included even when not directly called
const result = (() => {
  test();
  return 'value';
})();
```

When I bundle this code, the unreachable code after the `return` statement is not being properly removed, and functions seem to be included in ways that don't respect the broken flow analysis.

### Expected behavior

- Dead code after `return` statements should be tree-shaken
- Control flow should be properly tracked through function bodies
- Functions should only be included when actually used

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like a regression as it was working correctly before. The bundler appears to be incorrectly analyzing control flow within function bodies.

---
Repository: /testbed
