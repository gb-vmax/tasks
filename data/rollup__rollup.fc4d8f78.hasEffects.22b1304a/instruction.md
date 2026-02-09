# Bug Report

### Describe the bug

I'm experiencing an issue with switch case statements where all case consequents are being executed regardless of whether there's a break statement or not. It seems like the control flow analysis is inverted - cases that should stop executing are continuing, and vice versa.

### Reproduction

```js
let sideEffect = false;

switch (someValue) {
  case 'a':
    doSomething();
    break;
  case 'b':
    sideEffect = true;  // This shouldn't execute if case 'a' matched and broke
    break;
}
```

When `someValue` is `'a'`, the code in case `'b'` is still being treated as if it has effects, even though the flow should have been broken by the break statement in case `'a'`.

### Expected behavior

The bundler should correctly recognize that once a break statement is encountered, subsequent case statements in the switch should not be evaluated for side effects. Only the matching case and any fall-through cases (those without breaks) should be considered.

### Additional context

This appears to be affecting tree-shaking behavior - code that should be removed as unreachable is being kept in the bundle because the control flow analysis thinks it can still be reached.

---
Repository: /testbed
