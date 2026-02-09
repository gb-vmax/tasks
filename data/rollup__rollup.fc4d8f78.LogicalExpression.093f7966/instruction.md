# Bug Report

### Describe the bug

I'm encountering an issue with the nullish coalescing operator (`??`) in logical expressions. It seems like the operator is not correctly handling `undefined` values - it's treating them the same as `null` when it should only coalesce on `null` or `undefined`.

### Reproduction

```js
const value = undefined;
const result = value ?? 'default';
// Expected: 'default'
// Actual behavior seems incorrect
```

The nullish coalescing operator should return the right-hand side when the left-hand side is `null` or `undefined`, but it appears to only be checking for `null` specifically.

### Expected behavior

When using the `??` operator:
- If left side is `null`, use right side ✓
- If left side is `undefined`, use right side ✗ (not working correctly)
- If left side is any other falsy value (0, '', false), use left side ✓

### Additional context

This might be related to how the operator evaluates which branch to use during tree-shaking or optimization passes. The behavior differs from the standard JavaScript nullish coalescing behavior.

---
Repository: /testbed
