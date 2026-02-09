# Bug Report

### Describe the bug

I'm experiencing an issue with switch statement optimization where cases with side effects after a break statement are being incorrectly removed from the output bundle. It seems like code that should be included is being tree-shaken away.

### Reproduction

```js
let result = '';

switch (value) {
  case 1:
    sideEffect1();
    break;
    unreachableCode(); // This is correctly removed
  case 2:
    sideEffect2();
    break;
  case 3:
    sideEffect3();
}

// Expected: all three sideEffect calls should be in the bundle
// Actual: some cases might be missing from the output
```

The problem occurs when there are multiple switch cases with consequent statements. After a break is encountered in one case, subsequent cases are not being processed correctly during the bundling phase.

### Expected behavior

All switch cases with side effects should be included in the final bundle, even if a previous case contains a break statement. The break should only affect the control flow within that specific case, not the analysis of subsequent cases.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
