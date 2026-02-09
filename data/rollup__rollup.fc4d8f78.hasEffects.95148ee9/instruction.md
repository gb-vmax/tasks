# Bug Report

### Describe the bug

I'm experiencing an issue with switch statement dead code elimination. When a switch case contains code after a `break` statement, it's not being properly tree-shaken even though it should be unreachable.

### Reproduction

```js
switch (x) {
  case 1:
    console.log('reachable');
    break;
    console.log('unreachable'); // This should be removed but isn't
    break;
  case 2:
    doSomething();
    break;
}
```

The unreachable code after the first `break` statement in case 1 is being included in the bundle when it should be eliminated. This is causing unnecessary code bloat in the final output.

### Expected behavior

Code that appears after a `break` statement within a switch case should be recognized as unreachable and removed during tree-shaking/dead code elimination.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
