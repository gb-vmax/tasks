# Bug Report

### Describe the bug

I'm experiencing an issue with `for...of` loops where the loop variable isn't being properly tracked for tree-shaking purposes. When using destructuring or object patterns in the loop variable, the bundler seems to be incorrectly optimizing away code that should be kept.

### Reproduction

```js
const items = [{ value: 1 }, { value: 2 }, { value: 3 }];

for (const { value } of items) {
  console.log(value);
}
```

When bundling this code, properties that are accessed through the destructured loop variable are being incorrectly removed during tree-shaking, even though they're clearly being used in the loop body.

### Expected behavior

The loop variable (left side of the `for...of` statement) should be properly deoptimized so that tree-shaking doesn't remove code that depends on it. The bundler should treat assignments to the loop variable correctly and not optimize away necessary code paths.

### Additional context

This appears to be related to how the AST node handles deoptimization paths for `for...of` statements. The issue manifests when the loop variable has side effects or when it's used in ways that require tracking mutations.

---
Repository: /testbed
