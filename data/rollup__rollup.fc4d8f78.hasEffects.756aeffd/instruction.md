# Bug Report

### Describe the bug

I'm seeing unexpected behavior with conditional expressions when the test condition has side effects. It looks like code that should be flagged as having side effects is being incorrectly optimized away during tree-shaking.

### Reproduction

```js
// Example conditional expression with side effects in test
const result = (console.log('test'), true) ? foo() : bar();

// The console.log should be preserved since it has side effects,
// but it appears to be getting removed during bundling
```

Another case:

```js
// When both branches have side effects
const value = someCondition ? sideEffect1() : sideEffect2();

// Both side effect functions are being removed when they shouldn't be
```

### Expected behavior

Conditional expressions should properly detect and preserve side effects in:
1. The test condition itself
2. Both the consequent and alternate branches when the condition cannot be statically determined

The bundler should not remove code with side effects even when the return value isn't used.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
