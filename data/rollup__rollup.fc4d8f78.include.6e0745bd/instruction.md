# Bug Report

### Describe the bug

Switch statements with default cases are not being handled correctly during tree-shaking. When a switch statement has a default case that appears before the last case, the code inclusion logic produces incorrect results.

### Reproduction

```js
switch (condition) {
  case 'a':
    sideEffect1();
    break;
  default:
    sideEffect2();
    break;
  case 'b':
    sideEffect3();
    break;
}
```

In this scenario, the switch statement's cases are not being processed in the correct order, leading to incorrect tree-shaking behavior. The issue seems to affect switches where the default case is not at the end.

### Expected behavior

The bundler should correctly analyze and include switch statement cases regardless of where the default case is positioned. All reachable code should be properly included in the bundle, and unreachable code should be eliminated.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
