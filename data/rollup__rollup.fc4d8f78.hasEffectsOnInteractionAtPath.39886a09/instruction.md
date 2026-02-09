# Bug Report

### Describe the bug

I'm experiencing an issue with conditional expressions where side effects are not being properly detected in both branches. It seems like the bundler is incorrectly tree-shaking code that has side effects when used in ternary operations.

### Reproduction

```js
// example.js
const obj = { value: 0 };

function incrementValue() {
  obj.value++;
  return obj;
}

function decrementValue() {
  obj.value--;
  return obj;
}

// This conditional expression has side effects in both branches
const result = someCondition ? incrementValue() : decrementValue();

export { result };
```

When bundling this code, the functions with side effects are being removed even though they should be preserved because both branches of the ternary operator modify `obj.value`.

### Expected behavior

Both `incrementValue()` and `decrementValue()` should be recognized as having side effects and should not be tree-shaken away. The bundler should preserve code that has side effects in conditional expressions, regardless of which branch is taken.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to be a regression as this worked correctly in previous versions. The issue appears to be specific to how side effects are tracked through conditional/ternary expressions.

---
Repository: /testbed
