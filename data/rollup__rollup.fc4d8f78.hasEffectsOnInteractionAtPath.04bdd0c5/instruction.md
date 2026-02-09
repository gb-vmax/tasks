# Bug Report

### Describe the bug

I'm encountering an issue where pure function calls are being incorrectly tree-shaken when their return values are assigned to variables. The assignment operation seems to be treated as having no side effects even when it should be preserved.

### Reproduction

```js
// This gets incorrectly removed during tree-shaking
const result = pureFunction();

// Expected: the assignment should be preserved
// Actual: the entire line gets removed
```

The problem appears to be related to how assignment interactions are evaluated for pure function calls. When a pure function's return value is assigned, the bundler treats it as if the assignment has no effects and removes it entirely.

### Expected behavior

Assignments of pure function call results should be preserved in the output, even if the assigned variable isn't used later. The function call itself might have been intentional (e.g., for initialization side effects or future use).

### Additional context

This seems to have started happening recently. The logic for determining whether an interaction has effects might be inverted for assignment cases with pure functions.

---
Repository: /testbed
