# Bug Report

### Describe the bug

I'm encountering an issue with return value analysis in functions that have multiple return statements. When a function has more than one return expression, the bundler seems to be treating the return type incorrectly, which is causing unexpected tree-shaking behavior.

### Reproduction

```js
function getValue(condition) {
  if (condition) {
    return { value: 1 };
  }
  return { value: 2 };
}

const result = getValue(true);
console.log(result.value); // Should work but gets optimized incorrectly
```

When I have a function with multiple return statements like this, the return value analysis doesn't seem to be working as expected. The bundler appears to be using only the first return expression instead of properly handling the case where there are multiple possible return values.

### Expected behavior

Functions with multiple return statements should have their return types properly analyzed. The bundler should recognize that there are multiple possible return values and handle them appropriately during optimization.

### System Info

- Rollup version: latest
- Node version: 18.x

This seems to be affecting tree-shaking and dead code elimination. Any insights would be appreciated!

---
Repository: /testbed
