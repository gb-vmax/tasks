# Bug Report

### Describe the bug

I'm experiencing unexpected behavior with switch statements when checking for side effects. It seems like the order in which switch cases are evaluated might be incorrect, causing issues with control flow analysis.

When I have a switch statement with multiple cases, the side effect detection doesn't work as expected. Cases that should be recognized as having effects are being skipped or evaluated in the wrong order.

### Reproduction

```js
switch (value) {
  case 1:
    sideEffect1();
    break;
  case 2:
    sideEffect2();
    // falls through
  case 3:
    sideEffect3();
    break;
  default:
    defaultEffect();
}
```

In the above code, the side effects should be properly detected for each case, but it appears that the evaluation order is causing some cases to be missed or incorrectly analyzed.

### Expected behavior

All switch cases should be evaluated in the correct order to properly detect side effects and control flow. The analysis should correctly handle:
- Cases with break statements
- Fall-through cases
- Default cases

The current behavior seems to process cases in reverse or skip certain evaluations entirely.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
