# Bug Report

### Describe the bug

I'm encountering an issue with switch statement handling where cases with side effects are not being properly evaluated. It seems like the control flow analysis for switch statements is producing incorrect results, causing some cases to be unexpectedly included or excluded during tree-shaking.

### Reproduction

```js
// Example switch statement that demonstrates the issue
switch (condition) {
  case 'a':
    sideEffect1();
    break;
  case 'b':
    sideEffect2();
    // fallthrough
  case 'c':
    sideEffect3();
    break;
  default:
    sideEffect4();
}
```

When bundling code with switch statements like above, the control flow analysis doesn't correctly determine which cases can be safely removed. This affects dead code elimination and can result in either:
- Cases with side effects being incorrectly removed
- Unreachable cases being incorrectly included in the bundle

### Expected behavior

Switch statements should be analyzed correctly with proper handling of:
- Break statements and control flow
- Fall-through cases
- Side effects in each case block

The bundler should accurately determine which cases are reachable and preserve necessary side effects while removing dead code.

### System Info
- Rollup version: latest
- Node version: 18.x

This appears to be related to how the switch statement AST node evaluates effects and determines broken flow through the cases. The issue is particularly noticeable when dealing with complex switch statements that have multiple fall-through cases.

---
Repository: /testbed
