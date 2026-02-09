# Bug Report

### Describe the bug

I'm encountering an issue with the nullish coalescing operator (`??`) where it's not behaving correctly in logical expressions. When the left-hand side is `null` or `undefined`, the operator seems to be selecting the wrong branch.

### Reproduction

```js
const a = null;
const b = 'fallback';

// Using nullish coalescing
const result = a ?? b;

// Expected: 'fallback'
// Actual behavior suggests it's treating this incorrectly
```

The issue appears when the left operand is `null` or `undefined` - instead of falling back to the right operand as expected, the behavior is inverted.

### Expected behavior

The nullish coalescing operator should:
- Return the right operand when the left operand is `null` or `undefined`
- Return the left operand for all other values (including `0`, `false`, `''`, etc.)

This is standard behavior for the `??` operator in JavaScript.

### Additional context

This seems to affect tree-shaking and optimization passes where the operator determines which branch is "used". The wrong branch is being marked as used, which could lead to incorrect code elimination or inclusion during the build process.

---
Repository: /testbed
