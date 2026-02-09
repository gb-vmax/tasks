# Bug Report

### Describe the bug

I'm experiencing an issue where `debugger` statements are being removed from my bundled code even when tree-shaking is disabled or when the debugger statement should clearly have side effects. This is causing problems during development as breakpoints set via `debugger` statements are not being preserved in the output.

### Reproduction

```js
// input.js
function myFunction() {
  debugger;
  console.log('This should stop at debugger');
}

export { myFunction };
```

When bundling this code, the `debugger` statement gets stripped out completely from the final bundle, even though it should be preserved as it has runtime effects (pausing execution in dev tools).

### Expected behavior

The `debugger` statement should be included in the bundled output since it has observable side effects when running code in a debugging environment. It should not be tree-shaken away.

### Additional context

This seems to have started happening recently. Previously, debugger statements were correctly preserved in the output. This is particularly problematic during development when trying to debug bundled code.

---
Repository: /testbed
