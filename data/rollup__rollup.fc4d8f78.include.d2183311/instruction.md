# Bug Report

### Describe the bug

When using conditional expressions (ternary operators) in code that gets tree-shaken, the test condition is not being included in the output even when only one branch is used. This causes runtime errors when the bundled code tries to evaluate the condition.

### Reproduction

```js
// Input code
const result = someCondition ? consequent() : alternate();

// When tree-shaking determines only one branch is used,
// the test condition (someCondition) gets dropped from the output
// causing a ReferenceError at runtime
```

The issue occurs when:
1. A conditional expression has a determinable branch at build time
2. Tree-shaking optimization is applied
3. The test expression is not marked as having side effects

### Expected behavior

Even when tree-shaking can determine which branch will be taken, the test condition should still be included in the output to ensure the code executes correctly at runtime.

### Additional context

This seems to happen specifically with ternary operators where the condition itself needs to be evaluated. The bundler is optimizing too aggressively and removing necessary code.

---
Repository: /testbed
