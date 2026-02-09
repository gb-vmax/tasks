# Bug Report

### Describe the bug

When using a switch statement where the first case is the default case, the tree-shaking/dead code elimination doesn't work correctly. Code that should be included in the bundle is being incorrectly removed.

### Reproduction

```js
switch (value) {
  default:
    console.log('default case');
    sideEffect();
    break;
  case 1:
    console.log('case 1');
    break;
  case 2:
    console.log('case 2');
    break;
}
```

When the default case is the first case in the switch statement, the code in the default case gets incorrectly excluded from the output bundle even though it has side effects and should be preserved.

### Expected behavior

The default case should be properly included in the bundle regardless of its position in the switch statement. All cases with side effects should be preserved during tree-shaking.

### Additional context

This seems to only happen when the default case is at index 0 (the first case). When the default case is in any other position, everything works as expected.

---
Repository: /testbed
