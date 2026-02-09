# Bug Report

### Describe the bug

I'm encountering incorrect behavior with conditional expressions (ternary operators) in my code. It seems like the branches are being swapped - when the condition is true, the false branch is being executed, and vice versa.

### Reproduction

```js
const result = condition ? consequent : alternate;
```

When `condition` evaluates to `true`, the code is executing the `alternate` branch instead of the `consequent` branch. Similarly, when `condition` is `false`, it executes the `consequent` instead of the `alternate`.

For example:
```js
const value = true ? 'should be this' : 'not this';
// Expected: 'should be this'
// Actual: 'not this'
```

This is breaking all my conditional logic and causing unexpected runtime behavior. The wrong branch is consistently being selected regardless of the test condition value.

### Expected behavior

When a conditional expression evaluates, it should:
- Execute the consequent (first branch) when the test is truthy
- Execute the alternate (second branch) when the test is falsy

### Additional context

This appears to affect tree-shaking and dead code elimination as well, since the wrong branches are being marked as used/unused during optimization.

---
Repository: /testbed
