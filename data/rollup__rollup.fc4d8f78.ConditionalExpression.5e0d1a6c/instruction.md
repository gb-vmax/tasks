# Bug Report

### Describe the bug

I'm experiencing an issue with conditional expressions (ternary operators) where the bundler seems to be incorrectly optimizing branches. When both the consequent and alternate branches of a ternary expression should evaluate to the same boolean value, the bundler is returning `UnknownValue` instead of the expected value.

### Reproduction

```js
const result = condition ? true : 1;
// Both branches are truthy, so this should be optimized to a truthy value
// But instead it's being treated as unknown

const result2 = condition ? false : 0;
// Both branches are falsy, so this should be optimized to a falsy value
// But instead it's being treated as unknown
```

This affects tree-shaking and dead code elimination since the bundler can't properly determine the truthiness of these expressions.

### Expected behavior

When both branches of a conditional expression cast to the same boolean value (both truthy or both falsy), the bundler should recognize this and optimize accordingly. It should only return `UnknownValue` when the branches have different boolean values.

### Additional context

This seems to have broken recently. The logic for determining when to return `UnknownValue` appears to be inverted.

---
Repository: /testbed
