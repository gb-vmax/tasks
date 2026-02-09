# Bug Report

### Describe the bug

Debugger statements are being incorrectly removed during the tree-shaking/optimization process. When building for production, `debugger;` statements that should be preserved are getting stripped out of the final bundle.

### Reproduction

```js
function myFunction() {
  console.log('before debugger');
  debugger;
  console.log('after debugger');
}
```

After bundling, the `debugger;` statement is completely removed from the output, even though it should be preserved as it has side effects (pauses execution when devtools are open).

### Expected behavior

The `debugger;` statement should be treated as having side effects and preserved in the bundle, similar to how `console.log` or other statements with observable effects are handled. It should only be removed if explicitly configured to do so via tree-shaking options.

### Additional context

This is particularly problematic when trying to debug production builds or when debugger statements are intentionally left in the code for troubleshooting purposes. The statement should be considered as having effects since it modifies program execution flow when a debugger is attached.

---
Repository: /testbed
