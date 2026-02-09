# Bug Report

### Describe the bug

I'm experiencing an issue where function calls inside conditional blocks or certain control flow structures are not being properly included in the output bundle. It seems like the tree-shaking logic is incorrectly removing code that should be retained.

### Reproduction

```js
function foo() {
  console.log('This should be included');
}

if (someCondition) {
  foo();
}
```

When bundling this code, the `foo()` function call and potentially the entire conditional block are being removed from the output even though they should be preserved.

### Expected behavior

The function call and its containing logic should be included in the bundle when it's part of the reachable code path. The tree-shaking should correctly identify that this code is needed and include it in the final output.

### Additional context

This appears to affect nested function calls and might be related to how the inclusion logic handles recursive child nodes. The issue manifests inconsistently depending on the structure of the code.

---
Repository: /testbed
